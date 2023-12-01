DROP TABLE IF EXISTS posts_tags;
DROP SEQUENCE IF EXISTS post_id_seq;
DROP SEQUENCE IF EXISTS tags_id_seq;
DROP TABLE IF EXISTS tags;
DROP SEQUENCE IF EXISTS tag_id_seq;
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;


CREATE TABLE posts(
    id SERIAL PRIMARY KEY,
    title text
);
CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    name text
);
CREATE TABLE posts_tags(
    post_id int,
    tag_id int,
    constraint fk_post foreign key(post_id) references posts(id) on delete cascade,
    constraint fk_tag foreign key(tag_id) references tags(id) on delete cascade,
    PRIMARY KEY (post_id,tag_id)
);

INSERT INTO posts (title) VALUES
('How to use Git'),
('Fun classes'),
('Using a REPL'),
('My weekend in Edinburgh'),
('The best chocolate cake EVER'),
('A foodie week in Spain'),
('SQL basics');

INSERT INTO tags (name) VALUES
('coding'),
('travel'),
('cooking'),
('education');

INSERT INTO posts_tags (post_id, tag_id) VALUES
(1, 1),
(2, 1),
(3, 1),
(4, 2),
(5, 3),
(6, 2),
(7, 1),
(6, 3),
(2, 4),
(3, 4);