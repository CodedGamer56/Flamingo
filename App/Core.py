import random
import arrow
from rich.prompt import Prompt

from . import Database as db
from . import Render as UI

from . import Handler as check


def run():
    # Initialization work is done here
    db.init_db()

    subjects = db.get_subjects()
    quests = []

    for i in subjects:
        data = db.get_quests('name', 'WHERE parent_id = {id}'.format(id = i[0]))
        quests.append(data)

    UI.render_menu(subjects, quests)

def study():
    # The main algorithm of the program
    journey = input('Journey Name: ')
    quest = input('Quest Name: ')

    try:
        check.journey(journey)
        check.quest(quest)
        qid = db.get_quests('id', 'WHERE name = "{0}"'.format(quest.title()))

        deck = []

        rookieDeckExt = 'level = "Rookie" AND quest_id = {} LIMIT 10'.format(qid[0]) # New cards
        rookie_deck = db.get_cards(col = 'front, back, level', ext = 'WHERE ' + rookieDeckExt)

        everydayDeckExt = 'level = "Ranger" and quest_id = {}'.format(qid[0]) # Everyday cards
        everyday_deck = db.get_cards(col = 'front, back, level', ext = 'WHERE ' + everydayDeckExt) 

        today = arrow.now()
        ftoday = today.date()
        currentDeckExt = 'review = "{0}" and quest_id = {1}'.format(ftoday, qid[0]) # Today's cards
        current_deck = db.get_cards(col = 'front, back, level', ext = 'WHERE ' + currentDeckExt)
        
        deck = rookie_deck + everyday_deck + current_deck
        deck = show_cards(deck[:])
        study_deck = deck
        
        while study_deck != []:
            for i in study_deck:
                if i[2] == 'Veteran':
                    study_deck.remove(i)

            study_deck = show_cards(study_deck)
            
    except Exception as error:
        UI.render_error(error)

def show_cards(deck):
    random.shuffle(deck)

    for i in range(len(deck)):
        flashcard = deck[i]
        UI.render_flashcard(flashcard[0])
        recallLvl = Prompt.ask('Recall level: ', choices = ['Hard', 'Moderate', 'Easy', 'Again'])
        
        flashcard = assign_card_level(flashcard, recallLvl)
        deck[i] = flashcard

    return deck

def assign_card_level(card, recallLvl):
    newLvl = ''
    _card = list(card)

    if recallLvl == 'Hard':
        newLvl = 'Ranger'
    elif recallLvl == 'Moderate':
        newLvl = 'Recruit'
    elif recallLvl == 'Easy':
        newLvl = 'Veteran'

    _card[2] = newLvl
    return tuple(_card)

def new_journey():
    label = input('Journey Name: ')

    try:
        check.journey(label, False)
        UI.render_debug(db.create_journey(label))
    except Exception as err:
        UI.render_error(err)

def new_quest():
    journey = input('Journey Name: ')
    label = input('Quest Name: ')

    try:
        check.journey(journey)
        check.quest(label, False)

        pid = db.get_subjects(col = 'id', ext = 'WHERE subject = "{}"'.format(journey))
        db.create_quest(label, pid[0])
    except Exception as err:
        UI.render_error(err)

def new_card():
    journey = input('Journey Name: ')
    quest = input('Quest Name: ')

    front = input('Card (Front): ')
    back = input('Card (back): ')

    try:
        check.journey(journey)
        check.quest(quest)
        check.card(front, 'front', False)

        qid = db.get_quests('id', 'WHERE name = "{0}"'.format(quest.title()))
        db.create_card(front, back, qid[0])
    except Exception as err:
        UI.render_error(err)

def remove_journey():
    journey = input('Journey Name: ')
    
    try:
        check.journey(journey)

        pid = db.get_subjects(col = 'id', ext = 'WHERE subject = "{}"'.format(journey))
        db.del_quest(pid[0])
        db.del_journey(journey)    
    except Exception as err:
        UI.render_error(err)

def remove_quest():
    journey = input('Journey Name: ')
    quest = input('Quest Name: ')

    try:
        check.journey(journey)
        check.quest(quest)
        
        pid = db.get_subjects(col = 'id', ext = 'WHERE subject = "{}"'.format(journey))
        db.del_quest((pid[0], quest), 'parent_id = {0} and name = "{1}"')
    except Exception as err:
        UI.render_error(err)

def remove_card():
    journey = input('Journey Name: ')
    quest = input('Quest Name: ')

    try:
        check.journey(journey)
        check.quest(quest)

        qid = db.get_quests('id', 'WHERE name = "{0}"'.format(quest.title()))
        
        cards = db.get_cards(col = 'id, front, level', ext = 'WHERE quest_id = {}'.format(qid[0]))
        UI.render_cards(cards, quest)
        
        card_id = input('ID of card to delete: ')

        check.card(card_id)
        db.del_card(card_id)
    except Exception as error:
        UI.render_error(error)

def end():
    db.end()
    UI.render_msg('Bye!')