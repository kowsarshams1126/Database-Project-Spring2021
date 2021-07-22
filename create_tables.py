
import sqlite3

con = sqlite3.connect('linkedin_db.db')

cur = con.cursor()

# Create table
cur.execute('''
CREATE TABLE user
(
  user_id integer NOT NULL,
  name VARCHAR(100) NOT NULL,
  gender INT,
  email VARCHAR(100) NOT NULL,
  introducion VARCHAR(10000) ,
  about VARCHAR(10000) ,
  birthday DATE ,
  company VARCHAR(10000) ,
  location VARCHAR(10000) ,
  username VARCHAR(100) NOT NULL,
  password VARCHAR(100) NOT NULL,
  PRIMARY KEY (user_id)
);
               ''')

cur.execute('''
CREATE TABLE connection
(
  connection_id integer NOT NULL,
  user_id1 INT NOT NULL,
  user_id2 INT NOT NULL,
  PRIMARY KEY (connection_id),
  FOREIGN KEY (user_id1) REFERENCES user(user_id),
  FOREIGN KEY (user_id2) REFERENCES user(user_id)
);
               ''')

cur.execute('''
CREATE TABLE invitation
(
  invitation_id integer NOT NULL,
  user_idT INT NOT NULL,
  user_idR INT NOT NULL,
  PRIMARY KEY (invitation_id),
  FOREIGN KEY (user_idT) REFERENCES user(user_id),
  FOREIGN KEY (user_idR) REFERENCES user(user_id)
);
               ''')

cur.execute('''
CREATE TABLE conversation
(
  conversation_id integer NOT NULL,
  read INT NOT NULL,
  archive INT NOT NULL,
  user_idT INT NOT NULL,
  user_idR INT NOT NULL,
  PRIMARY KEY (conversation_id),
  FOREIGN KEY (user_idT) REFERENCES user(user_id),
  FOREIGN KEY (user_idR) REFERENCES user(user_id)
);
               ''')

cur.execute('''
CREATE TABLE message
(
  message_id integer NOT NULL,
  content VARCHAR(100000) NOT NULL,
  date DATE,
  f VARCHAR(100000) NOT NULL,
  conversation_id INT NOT NULL,
  PRIMARY KEY (message_id),
  FOREIGN KEY (conversation_id) REFERENCES conversation(conversation_id)
);
               ''')

cur.execute('''
CREATE TABLE post
(
  post_id integer NOT NULL,
  content VARCHAR(10000) NOT NULL,
  date DATE,
  user_id INT NOT NULL,
  PRIMARY KEY (post_id),
  FOREIGN KEY (user_id) REFERENCES user(user_id)
);
               ''')

cur.execute('''
CREATE TABLE share_post
(
  share_post_id integer NOT NULL,
  comment VARCHAR(10000),
  date DATE,
  post_id INT NOT NULL,
  user_id INT NOT NULL,
  PRIMARY KEY (share_post_id),
  FOREIGN KEY (post_id) REFERENCES post(post_id),
  FOREIGN KEY (user_id) REFERENCES user(user_id)
);
               ''')

cur.execute('''
CREATE TABLE like_post
(
  like_post_id integer NOT NULL,
  date DATE,
  post_id INT NOT NULL,
  user_id INT NOT NULL,
  PRIMARY KEY (like_post_id),
  FOREIGN KEY (post_id) REFERENCES post(post_id),
  FOREIGN KEY (user_id) REFERENCES user(user_id)
);
               ''')

cur.execute('''
CREATE TABLE comment
(
  comment_id integer NOT NULL,
  date DATE,
  content VARCHAR(10000) NOT NULL,
  post_id INT NOT NULL,
  user_id INT NOT NULL,
  PRIMARY KEY (comment_id),
  FOREIGN KEY (post_id) REFERENCES post(post_id),
  FOREIGN KEY (user_id) REFERENCES user(user_id)
);
               ''')

cur.execute('''
CREATE TABLE like_comment
(
  like_comment_id integer NOT NULL,
  user_id INT NOT NULL,
  date Date,
  comment_id INT NOT NULL,
  PRIMARY KEY (like_comment_id),
  FOREIGN KEY (user_id) REFERENCES user(user_id),
  FOREIGN KEY (comment_id) REFERENCES comment(comment_id)
);
               ''')

cur.execute('''
CREATE TABLE reply_comment
(
  reply_comment_id integer NOT NULL,
  comment_id1 INT NOT NULL,
  comment_id2 INT NOT NULL,
  PRIMARY KEY (reply_comment_id),
  FOREIGN KEY (comment_id1) REFERENCES comment(comment_id),
  FOREIGN KEY (comment_id2) REFERENCES comment(comment_id)
);
               ''')

cur.execute('''
CREATE TABLE language
(
  language_id integer NOT NULL,
  content VARCHAR(10000) NOT NULL,
  user_id INT NOT NULL,
  PRIMARY KEY (language_id),
  FOREIGN KEY (user_id) REFERENCES user(user_id)
);
               ''')

cur.execute('''
CREATE TABLE skill
(
  skill_id integer NOT NULL,
  content VARCHAR(10000) NOT NULL,
  user_id INT NOT NULL,
  PRIMARY KEY (skill_id),
  FOREIGN KEY (user_id) REFERENCES user(user_id)
);
               ''')

cur.execute('''
CREATE TABLE background
(
  background_id integer NOT NULL,
  type VARCHAR(10) NOT NULL,
  location VARCHAR(100) NOT NULL,
  field VARCHAR(100) NOT NULL,
  f DATE,
  t DATE,
  user_id INT NOT NULL,
  PRIMARY KEY (background_id),
  FOREIGN KEY (user_id) REFERENCES user(user_id)
);
               ''')

cur.execute('''
CREATE TABLE accomplishment
(
  accomplishment_id integer NOT NULL,
  content VARCHAR(100000) NOT NULL,
  user_id INT NOT NULL,
  PRIMARY KEY (accomplishment_id),
  FOREIGN KEY (user_id) REFERENCES user(user_id)
);
               ''')

cur.execute('''
CREATE TABLE notification
(
  notification_id integer NOT NULL,
  read INT NOT NULL,
  date DATE NOT NULL,
  type INT NOT NULL,
  user_idT INT NOT NULL,
  user_idR INT NOT NULL,
  PRIMARY KEY (notification_id),
  FOREIGN KEY (user_idT) REFERENCES user(user_id),
  FOREIGN KEY (user_idR) REFERENCES user(user_id)
);
               ''')

cur.execute('''
CREATE TABLE post_notification
(
  post_notification_id integer NOT NULL,
  notification_id INT NOT NULL,
  post_id INT NOT NULL,
  PRIMARY KEY (post_notification_id),
  FOREIGN KEY (notification_id) REFERENCES notification(notification_id),
  FOREIGN KEY (post_id) REFERENCES post(post_id)
);
               ''')

cur.execute('''
CREATE TABLE comment_notification
(
  comment_notification_id integer NOT NULL,
  notification_id INT NOT NULL,
  comment_id INT NOT NULL,
  PRIMARY KEY (comment_notification_id),
  FOREIGN KEY (notification_id) REFERENCES notification(notification_id),
  FOREIGN KEY (comment_id) REFERENCES comment(comment_id)
);
               ''')

cur.execute('''
CREATE TABLE feature
(
  feature_id integer NOT NULL,
  content VARCHAR(10000) NOT NULL,
  user_id INT NOT NULL,
  PRIMARY KEY (feature_id),
  FOREIGN KEY (user_id) REFERENCES user(user_id)
);
               ''')

# Save (commit) the changes
con.commit()

con.close()