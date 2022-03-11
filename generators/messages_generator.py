import json

from utils import message, action_link, action_input, button, links_to_check


messages = {
    'root': message(
        'What do you need?',
        buttons=[
            button('Help', action_link('need_help_from_location')),
            button('Donate', action_link('donate')),
            button('Main Info', action_link('main_info')),
            button('About Us', action_link('about_us')),
        ],
    ),
    'donate': message('Thank you for helping. Here are charities collecting donations for people in need:'),
    'main_info': message('We have collected different groups and resources for people helping those in need:'),
    'about_us': message('Grow Ukraine is a group of volunteers working to solve the complex logistics of humanitarian aid delivery'),
    'number_of_people_looking_for_shelter': message(
        'How many people are looking for shelter?',
        action=action_input('number', 'how_many_days_need_shelter'),
    ),
}


# validate that all links exist in messages
do_exit = False
for link in links_to_check:
    if link not in messages:
        print(f'Referenced link "{link}" is not in messages')
        do_exit = True

if do_exit:
    print('\n------- ( ! ) ------- \nYou have links to messages which don\'t exist (see above). Please resolve this and try again. No output file generated.\n------- ( ! ) -------')
    exit()


with open('output.json', 'w') as f:
    f.write(json.dumps(messages, indent=2))
