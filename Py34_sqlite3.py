from datetime import date
import sqlite3

def from_sq(name):
    name = name + '.db'
    con = sqlite3.connect(name)
    cur = con.cursor()
    for value in cur.execute('''SELECT * FROM tasks'''):
        for ind in value:
            if ind == date:
                print(date.fromtimestamp(ind))
            else:
                print(ind, type(ind))


def to_sq(name, name1, lists):
    name1 = name1 + '.db'
    con = sqlite3.connect(name1)
    cur = con.cursor()
    cur.executemany('''INSERT INTO {} VALUES (?,?)'''.format(name, lists))
    con.commit()


if __name__ == '__main__':
    con = sqlite3.connect('persons.db')
    cur = con.cursor()
    cur.executescript("""CREATE TABLE IF NOT EXISTS persons(ind BIGINT, name TEXT, birth TEXT);  
                   CREATE TABLE IF NOT EXISTS employees(id, position, salary);
                   CREATE TABLE IF NOT EXISTS contacts(id, type, value)""")

    # cur.execute("""CREATE TABLE IF NOT EXISTS persons (ind BIGINT, name TEXT, birth TEXT) """)
    # cur2.execute("""CREATE TABLE IF NOT EXISTS employees (id, position, salary) """) #ONE-TO-ONE relation to person
    # cur3.execute("""CREATE TABLE IF NOT EXISTS contacts (id, type, value)""") #MANY-TO-ONE relation to employees

    for index in range(10):
        to_sq(persons, persons, [index, name, birth])
        to_sq(employees, persons, [index, position, salary])
        to_sq(contacts, persons, [index, type, value])

    cur.execute('''SELECT * FROM persons JOIN employees ON persons.ind = employees.id''')
    cur.execute('''SELECT * FROM contacts JOIN employees ON contacts.id = employees.id''')
    con.commit()