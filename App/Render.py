from rich.console import Console
from rich.theme import Theme
from rich.table import Table
from rich.panel import Panel

app_theme = Theme(
        {
            'error': '#fc3030',
            'debug': '#ffc933',
            'msg': '#27e644'
        }
    )

screen = Console(theme = app_theme)

def render_menu(subjects, quests):
    # Topbar: Study, New, Edit, Remove, View, Settings
    for i in range(len(subjects)):
        screen.print(subjects[i][1] + ':', style='bold #ffffff')

        for j in quests[i]:
            screen.print('\t', j, style = '#00b8c2')

def render_cards(cards, questName):
    table = Table(title = questName.title())

    table.add_column('ID', justify='left', style='bold cyan')
    table.add_column('Front', justify='center', style='#03fc7f')
    table.add_column('Level', justify='center', style='#0390fc')

    for i in cards:
        table.add_row(str(i[0]), i[1], i[2])
        
    screen.print(table)

def render_flashcard(front):
    screen.print(Panel(front, style='cyan', border_style ='white'))

def render_debug(content):
    screen.print('!', content, style='debug')

def render_error(content):
    screen.print('#', content, style='error')

def render_msg(content, _style='msg'):
    screen.print('~', content, style=_style)
'''
Design Ideas
    - Spotify (Artist - Journey, Album - Quest, Song - Card)
    - Github Commit Stats
    - Recently Viewed
'''