import colorful as cf

from . import Database as db
from . import Render as UI
from . import Log as cmd

running = True

def init():
    # Initialization work is done here
    db.init()
    UI.render_menu()

def new_journey():
    label = input('Journey Name: ')
    exists = db.exists_journey(label)

    if label == '':
        cmd.error('Cannot accept empty label')
    elif exists == False:
        cmd.error('Journey already exists')
    else:
        cmd.debug(db.create_journey(label))

def new_quest():
    journey = input('Journey Name: ')
    label = input('Quest Name: ')

    if db.exists_journey(journey) == False:
        cmd.error('No such journey exists')
    elif label == '':
        cmd.error('Cannot accept empty label')
    else:
        pid = db.get_subjects(col = 'id', ext = 'WHERE subject = "{_journey}"'.format(_journey = journey))
        db.create_quest(label, pid[0])
    
def end():
    db.end()
    cmd.msg('Bye!')
