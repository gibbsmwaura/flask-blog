import sqlite3

with sqlite3.connect("blog.db") as connection:
	c = connection.cursor()
	c.execute(""" CREATE TABLE posts(title TEXT, post TEXT)""")
	c.execute('INSERT INTO posts VALUES("Good","I\'m Good")')
	c.execute('INSERT INTO posts VALUES("Well","I\'m Well")')
	c.execute('INSERT INTO posts VALUES("Excellent","I\'m Excellent")')
	c.execute('INSERT INTO posts VALUES("Ok","I\'m Ok")')

