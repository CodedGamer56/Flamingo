from .Database import exists_journey, exists_quest, exists_card

def journey(label, exist = True):
    emsg = ''
    flag = exists_journey(label)

    if flag == False and exist == True:
        emsg = 'No such journey exists'
    elif flag == True and exist == False:
        emsg = 'Journey already exists'
    elif label == '':
        emsg = 'Cannot accept empty label'
        
    if emsg:
        raise Exception(emsg)

def quest(label, exist = True):
    emsg = ''
    flag = exists_quest(label)

    if flag == False and exist == True:
        emsg = 'No such quest exists'
    elif flag == True and exist == False:
        emsg = 'Quest already exists'
    elif label == '':
        emsg = 'Cannot accept empty label'
    
    if emsg:
        raise Exception(emsg)

def card(label, checkFor = 'id', exist = True):
    emsg = ''
    flag = exists_card(label, checkFor)

    if flag == False and exist == True:
        emsg = 'No such card exists'
    elif flag == True and exist == False:
        emsg = 'Card already exists'
    elif label == '':
        emsg = 'Card front cannot be empty'
    
    if emsg:
        raise Exception(emsg)
    