import mysql.connector as mysql
from .Render import render_debug, render_error

db_object = None
cursor = None

def init_db():
    global db_object, cursor
    try:
        db_object = mysql.connect(host='localhost', user='root', database='Flamingo', password='mysql56')
        cursor = db_object.cursor()
        render_debug('Connection established with database')
    except Exception as db_error:
        render_error('Failed to connect to database - {}'.format(db_error))

def get_subjects(col = '*', ext = 'ORDER BY subject'):
    query = 'SELECT {0} FROM journey {1}'.format(col, ext)
    cursor.execute(query)
    feedback = cursor.fetchall()

    if col != '*' and (',' not in col):
        feedback = [i[0] for i in feedback]

    return feedback

def get_quests(col = '*', ext = ''):
    query = 'SELECT {0} FROM quest {1}'.format(col, ext)
    cursor.execute(query)
    feedback = cursor.fetchall()
    
    if col != '*' and (',' not in col):
        feedback = [i[0] for i in feedback]

    return feedback

def get_cards(col = '*', ext=''):
    query = 'SELECT {0} FROM card {1}'.format(col, ext)
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

def exists_card(_card, checkFor = 'id'):
    cards = get_cards(checkFor)
    exists = False
    
    if checkFor == 'id' and (_card in cards):
        exists = True
    elif _card.lower() in cards:
        exists = True
    
    return exists

def create_journey(_subject):
    query = 'INSERT INTO journey(subject) VALUE ("{}")'.format(_subject.title())
    cursor.execute(query)
    feedback = cursor.fetchall()
    return feedback

def create_quest(_quest, _pid):
    query = 'INSERT INTO quest(parent_id, name) VALUE ({0}, "{1}")'.format( _pid, _quest.title())
    cursor.execute(query)
    feedback = cursor.fetchall()
    return feedback

def create_card(_front, _back, _qid):
    query = 'INSERT INTO card(front, back, quest_id) VALUE ("{0}", "{1}", {2})'.format(_front.lower(), _back.lower(), _qid)
    cursor.execute(query)
    feedback = cursor.fetchall()
    return feedback

def edit_card(newVal, condition, col = 'review'):
    query = 'UPDATE card SET {0} = {1} WHERE {2}'.format(col, newVal, condition)
    cursor.execute(query)
    feedback = cursor.fetchall()
    return feedback

def del_journey(value, condition = 'subject = {}'):
    query = 'DELETE FROM journey WHERE ' + condition.format(value)
    cursor.execute(query)
    feedback = cursor.fetchall()
    return feedback

def del_quest(value, condition = 'parent_id = '):
    query = 'DELETE FROM quest WHERE ' + condition.format(*value)
    cursor.execute(query)
    feedback = cursor.fetchall()
    return feedback

def del_card(value, condition = 'id = {}'):
    query = 'DELETE FROM card WHERE ' + condition.format(value)
    cursor.execute(query)
    feedback = cursor.fetchall()
    return feedback

def end():
    db_object.commit()
    db_object.close()