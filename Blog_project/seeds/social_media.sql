DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;
DROP TABLE IF EXISTS user_accounts;
DROP SEQUENCE IF EXISTS user_accounts_id_seq;
-- Create the table without the foreign key first.
CREATE TABLE user_accounts (
  id SERIAL PRIMARY KEY,
  username text,
  email_address text
);

-- Then the table with the foreign key second.
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  content text,
  views int,
-- The foreign key name is always {other_table_singular}_id
  useraccount_id int,
  constraint fk_useraccount foreign key(useraccount_id)
    references user_accounts(id)
    on delete cascade
);

INSERT INTO user_accounts (username,email_address) VALUES('TestUsername1','testemailaddress@fakemail.com');
INSERT INTO user_accounts (username,email_address) VALUES('TestUsername2','testemailaddress2@fakemail.com');

INSERT INTO posts (title,content,views,useraccount_id) VALUES('Test Title1','This is some test content',1337,1);
INSERT INTO posts (title,content,views,useraccount_id) VALUES('Test Title2','This is some test content',1337,1);
INSERT INTO posts (title,content,views,useraccount_id) VALUES('Test Title1','This is some test content',1337,2);
INSERT INTO posts (title,content,views,useraccount_id) VALUES('Test Title2','This is some test content',1337,2);
