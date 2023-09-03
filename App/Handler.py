from . import Database as db

def journey(label, exist = True):
    emsg = ''
    if db.exists_journey(label) == False:
        emsg = 'No such journey exists'
    if exist == False:
        emsg = 'Journey already exists'
    elif label == '':
        emsg = 'Cannot accept empty label'
    
    if emsg:
        raise Exception(emsg)

def quest(label, exist = True):
    emsg = ''
    if db.exists_quest(label) == False:
        emsg = 'No such quest exists'
    if exist == False:
        emsg = 'Quest already exists'
    elif label == '':
        emsg = 'Cannot accept empty label'
    
    if emsg:
        raise Exception(emsg)
