import json
import gettext

import pycountry


from utils import (
    message,
    action_link,
    action_input,
    button,
    get_country_importance,
    fix_country_name,
)

from messages.can_help import messages as can_help_messages
from messages.need_help import messages as need_help_messages

from utils import (
    links_to_check,
    all_translation_keys,
)


messages = {
    'root': message(
        'select_language_message',
        buttons=[
            button(
                'language_english_button',
                action=action_link('main_menu'),
                context={'Language': 'English'},
            ),
            button(
                'language_ukranian_button',
                action=action_link('main_menu'),
                context={'Language': 'Ukranian'},
            ),
            button(
                'language_russian_button',
                action=action_link('main_menu'),
                context={'Language': 'Russian'},
            ),
        ],
    ),
    'main_menu': message(
        'what_do_you_need_message',
        buttons=[
            button('help_button', action_link('need_help_i_am_now_in')),
            button('donate_button', action_link('donate')),
            button('main_info_button', action_link('main_info')),
            button('about_us_button', action_link('about_us')),
            button('i_can_help_button', action_link('i_can_help')),
        ],
    ),
    'donate': message('donate_links_message'),
    'main_info': message('main_info_message'),
    'about_us': message('about_us_message'),
    **need_help_messages,
    **can_help_messages,
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

# Print all translation messages
# print('\n'.join(sorted([key for key in all_translation_keys if not key.endswith('_country')])))

with open('static/messages.json', 'w') as f:
    f.write(json.dumps(messages, indent=2))
