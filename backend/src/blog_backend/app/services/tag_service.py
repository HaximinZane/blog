async def list_tags(conn):
    rows = await conn.fetch("SELECT name FROM tags")
    rows = [dict(row)["name"] for row in rows]
    return rows

