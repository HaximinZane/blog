CREATE TABLE users(
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    username VARCHAR(100) UNIQUE,
    email VARCHAR(100) NOT NULL,
    hash_password text NOT NULL,
    role VARCHAR(10) CHECK (role in ('reader','author','admin')),
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE posts(
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    author_id BIGINT NOT NULL REFERENCES users(id),
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    summary TEXT,
    category VARCHAR(50) NOT NULL,
    sub_category VARCHAR(50),
    status VARCHAR(10) NOT NULL
        CHECK ( status in ('draft','published','archived') )
        DEFAULT 'draft',
    published_at timestamptz,
    created_at timestamptz NOT NULL DEFAULT now(),
    update_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE tags(
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    slug text UNIQUE NOT NULL
);

DROP TABLE post_tags;
CREATE TABLE post_tags(
    post_id BIGINT NOT NULL REFERENCES posts(id) ON DELETE CASCADE ,
    tag_id BIGINT NOT NULL REFERENCES tags(id) ON DELETE CASCADE ,
    PRIMARY KEY (post_id,tag_id)
);