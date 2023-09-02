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
    exists = db.get_subjects('subject', 'WHERE subject = "{label}"'.format(label = label))

    if label == '':
        cmd.error('Cannot accept empty label')
    elif exists != []:
        cmd.error('Journey already exists')
    else:
        cmd.debug(db.create_journey(label))

def end():
    db.end()
    cmd.msg('Bye!')
