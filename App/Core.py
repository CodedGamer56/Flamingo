# All core features are implemented here

import mysql.connector as mysql
import colorful as cf

def run():
    cf.use_true_colors()
    
    database = mysql.connect(host='localhost', user='root', database='Flamingo', password='mysql56')
    
    if database.is_connected():
        print('Connected to database')
    else:
        print('Problem in connecting to database')
    
    db_cursor = database.cursor()
    db_cursor.execute('SELECT * FROM journey ORDER BY subject')
    
    subjects = db_cursor.fetchall()
    
    for i in subjects:
        db_cursor.execute('SELECT name FROM quest WHERE parent_id = {id}'.format(id = i[0]))
        data = db_cursor.fetchall()
        print(cf.bold_cyan(i[1] + ':'))
    
        for j in data:
            print(cf.grey('\t' + j[0]))
    
    database.close()