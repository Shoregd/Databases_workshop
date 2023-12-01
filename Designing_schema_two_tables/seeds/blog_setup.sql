DROP TABLE IF EXISTS comments;
DROP SEQUENCE IF EXISTS comments_id_seq;
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title text,
    content text
);

CREATE SEQUENCE IF NOT EXISTS comments_id_seq;
CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    author_name text,
    content text,
    posts_id INTEGER,
    constraint fk_posts foreign key(posts_id) references posts(id) on delete cascade
);

INSERT INTO posts (title,content) VALUES('Test Title', 'This is some test content.');
INSERT INTO posts (title,content) VALUES('Test Title', 'This is some test content.');

INSERT INTO comments (author_name,content,posts_id) VALUES('Terry','Test comment',1);
INSERT INTO comments (author_name,content,posts_id) VALUES('Greg','Test comment',1);
INSERT INTO comments (author_name,content,posts_id) VALUES('Paul','Test comment',1);
INSERT INTO comments (author_name,content,posts_id) VALUES('Terry','Test comment',2);
INSERT INTO comments (author_name,content,posts_id) VALUES('Greg','Test comment',2);
INSERT INTO comments (author_name,content,posts_id) VALUES('Paul','Test comment',2);