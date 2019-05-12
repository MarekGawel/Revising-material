import sqlite3

subjectname = "durability_of_the_materials"


db = sqlite3.connect('testing.db')
curs = db.cursor()



curs.execute('DROP TABLE '+subjectname)
curs.execute('''CREATE TABLE IF NOT EXISTS '''+subjectname+''' ( id INT PRIMARY KEY,  name VARCHAR, rate INT)''')

curs.execute('''INSERT INTO '''+subjectname+''' VALUES (1, "Durability od rod systems", 4)''')
curs.execute('''INSERT INTO '''+subjectname+''' VALUES (2, "Basics of calculations of statically indeterminate systems", 2)''')
curs.execute('''INSERT INTO '''+subjectname+''' VALUES (3, "Basics of linear theory of elasticity", 0)''')
curs.execute('''INSERT INTO '''+subjectname+''' VALUES (4, "Strength of circular plates and axially symmetrical coatings", 4)''')
curs.execute('''INSERT INTO '''+subjectname+''' VALUES (5, "Durability hypotheses", 1)''')
db.commit()
curs.execute("SELECT * FROM "+subjectname+" ORDER BY rate")

rows = curs.fetchone()

print(rows)

print(rows)