from ..models.post import PostCreate
import re

async def list_public_posts(conn,skip:int = 0,limit:int | None = None,):
    limit = limit or 100000
    rows = await conn.fetch("SELECT * FROM posts WHERE status = $1 ORDER BY id OFFSET $2 LIMIT $3",'published',skip,limit)
    tmp = [ dict(row) for row in rows]
    return tmp

async def get_public_post(conn,post_id : int):
    row = await conn.fetchrow("SELECT * FROM posts WHERE id = $1 AND status = $2",post_id,'published')
    if row:
        return dict(row)
    return None

"""
 id           | bigint                   |           | not null | generat
ed always as identity
 author_id    | bigint                   |           | not null | 
 title        | text                     |           | not null | 
 summary      | text                     |           |          | 
 status       | character varying(10)    |           | not null | 'draft'
::character varying
 published_at | timestamp with time zone |           |          | 
 created_at   | timestamp with time zone |           | not null | now()
 update_at    | timestamp with time zone |           | not null | now()
 category     | character varying(50)    |           | not null | 
 sub_category | character varying(50)    |           |          | NULL::c
haracter varying
 content      | text                     |           | not null |
"""

async def clean_tags(tags:list):
    slugs = []
    tags = [t.strip() for t in tags]
    for tag in tags:
        slug = re.sub(r"\s+", "_", tag.lower())   
        slug = re.sub(r"-+", "-", slug).strip("-")
        slugs.append(slug)
    return tags,slugs


async def create_post(conn,post : PostCreate):
    author_id = post.author_id
    tags,slugs = await clean_tags(post.tags)
    if await conn.fetchval("SELECT author_id from posts where author_id = $1",author_id) is None:
        raise ValueError("No such author")
    
    if post.status != "published":
        new_id = await conn.fetchval("INSERT INTO posts "
        "(author_id,title,summary,status,content)" \
        "VALUES ($1,$2,$3,$4,$5)" \
        "RETURNING id",
        post.author_id,post.title,post.summary,post.status,post.content)
    else:
        new_id = await conn.fetchval("INSERT INTO posts "
        "(author_id,title,summary,status,content,published_at)" \
        "VALUES ($1,$2,$3,$4,$5,now())" \
        "RETURNING id",
        post.author_id,post.title,post.summary,post.status,post.content)
    # 先往tags库里插入，如果已有tag，就不插入，没有就插入
    for tag,slug in zip(tags,slugs):
        await conn.execute("INSERT INTO tags (name,slug) VALUES ($1,$2) ON CONFLICT DO NOTHING",tag,slug)
        await conn.execute("INSERT INTO post_tags (post_id,tag_id) " \
        "VALUES ($1,(SELECT id FROM tags WHERE slug = $2))",new_id,slug)
    return new_id

    