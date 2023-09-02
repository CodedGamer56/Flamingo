import colorful as cf

from . import Database as db

def render_menu():
    # Topbar: Study, New, Edit, Remove, View, Settings
    subjects = db.get_subjects()
    
    for i in subjects:
        print(cf.bold_cyan(i[1]) + ':')
        data = db.get_quests('name', 'WHERE parent_id = {id}'.format(id = i[0]))

        for j in data:
            print('\t', cf.grey(j))
            
'''
Design Ideas
    - Spotify (Artist - Journey, Album - Quest, Song - Card)
    - Github Commit Stats
    - Recently Viewed
'''