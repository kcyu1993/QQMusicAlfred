"""
    Reference: NeteaseMusicControls
"""
import sys
import alfred

items = [['toggle', 'play/pause current song'],
        ['prev', 'play previous song'],
        ['next', 'play next song'],
        ['up', 'turn volume up'],
        ['down', 'turn volumn down'],
        ['like', 'like/dislike current song'],
        ['togglelyrics', 'display/hide the lyrics']]

query = sys.argv[1].lower()

feedback = alfred.Feedback()

chosenItem = []
for item in items:
    if item[0].startswith(query):
        chosenItem.append(item)

if len(chosenItem) == 0:
    feedback.addItem(title='Oops!', subtitle='undefined action...')
else:
    for item in chosenItem:
        feedback.addItem(title=item[0], subtitle=item[1], autocomplete=item[0], arg=item[0])
feedback.output()

