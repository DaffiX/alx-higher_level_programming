#!/usr/bin/python3
"""lists all states from the database"""
if __name__ == '__main__':
    
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()

    #use cursor to execute queries
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC;")

    # fetch all data - grab row
    rows = cursor.fetchall()
    for row in rows:
        print(row)
