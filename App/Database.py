import mysql.connector as mysql

from . import Log as cmd

db_object = None
cursor = None

def init():
    global db_object, cursor
    try:
        db_object = mysql.connect(host='localhost', user='root', database='Flamingo', password='mysql56')
        cursor = db_object.cursor()
        cmd.debug('Connection established with database')
    except Exception as db_error:
        cmd.error('Failed to connect to database - {error}'.format(error = db_error))

def get_subjects(col = '*', ext = 'ORDER BY subject'):
    query = 'SELECT {column} FROM journey {extension}'.format(column = col, extension = ext)
    cursor.execute(query)
    feedback = cursor.fetchall()

    if col != '*' and (',' not in col):
        feedback = [i[0] for i in feedback]

    return feedback

def get_quests(col = '*', ext = ''):
    query = 'SELECT {column} FROM quest {extension}'.format(column = col, extension = ext)
    cursor.execute(query)
    feedback = cursor.fetchall()
    
    if col != '*' and (',' not in col):
        feedback = [i[0] for i in feedback]

    return feedback

def exists_journey(_subject):
    subjects = get_subjects(col = 'subject')
    exists = False

    if  _subject.title() in subjects:
        exists = True

    return exists

def exists_quest(_quest):
    quests = get_quests(col = 'name')
    exists = False

    if _quest.title() in quests:
        exists = True

    return exists

def create_journey(_subject):
    query = 'INSERT INTO journey(subject) VALUE ("{subjectLabel}")'.format(subjectLabel = _subject.title())
    cursor.execute(query)
    feedback = cursor.fetchall()
    return feedback

def create_quest(_quest, _pid):
    query = 'INSERT INTO quest(parent_id, name) VALUE ({pid}, "{questLabel}")'.format(pid = _pid, questLabel = _quest.title())
    cursor.execute(query)
    feedback = cursor.fetchall()
    return feedback

def end():
    db_object.commit()
    db_object.close()