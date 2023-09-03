import colorful as cf

from . import Database as db
from . import Handler as check
from . import Render as UI
from . import Log as cmd

running = True

def init():
    # Initialization work is done here
    db.init()
    UI.render_menu()

def new_journey():
    label = input('Journey Name: ')

    try:
        check.journey(label, False)
        cmd.debug(db.create_journey(label))
    except Exception as err:
        cmd.error(err)

def new_quest():
    journey = input('Journey Name: ')
    label = input('Quest Name: ')

    try:
        check.journey(label)
        check.quest(label, False)

        pid = db.get_subjects(col = 'id', ext = 'WHERE subject = "{}"'.format(journey))
        db.create_quest(label, pid[0])
    except Exception as err:
        cmd.error(err)

def remove_journey():
    journey = input('Journey Name: ')
    
    try:
        check.journey(journey)

        pid = db.get_subjects(col = 'id', ext = 'WHERE subject = "{}"'.format(journey))
        db.del_quest(pid[0])
        db.del_journey(journey)    
    except Exception as err:
        cmd.error(err)

def remove_quest():
    journey = input('Journey Name: ')
    quest = input('Quest Name: ')

    try:
        check.journey(journey)
        check.quest(quest)
        
        pid = db.get_subjects(col = 'id', ext = 'WHERE subject = "{}"'.format(journey))
        db.del_quest((pid[0], quest), 'parent_id = {0} and name = "{1}"')
    except Exception as err:
        cmd.error(err)

def end():
    db.end()
    cmd.msg('Bye!')

# Extension Object
#   Conditional statement - 