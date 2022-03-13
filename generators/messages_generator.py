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

from utils import (
    links_to_check,
    all_translation_keys,
)


messages = {
    'root': message(
        'what_do_you_need_message',
        buttons=[
            button('help_button', action_link('i_am_now_in')),
            button('donate_button', action_link('donate')),
            button('main_info_button', action_link('main_info')),
            button('about_us_button', action_link('about_us')),
        ],
    ),
    'donate': message('donate_links_message'),
    'main_info': message('main_info_message'),
    'about_us': message('about_us_message'),
    'i_am_now_in': message(
        'i_am_now_in_message',
        buttons=[
            # button('country_ukraine', action_link('i_need'), context={'Country': 'Ukraine'}),
            button('other_country_button', action_link('select_counry_currently_in')),
        ],
    ),
    'select_counry_currently_in': message(
        'select_a_country_message',
        buttons=[
            # button(fix_country_name(c.name), action_link('i_need'), context={'Country': fix_country_name(c.name)})
            # for c in sorted(pycountry.countries, key=lambda c: get_country_importance(c))
        ],
    ),
    'i_need': message(
        'i_need_message',
        buttons=[
            button('i_need_help_button', action_link('i_need_help'), context={'Need': 'Help'}),
            button('i_need_job_button', action_link('i_need_job'), context={'Need': 'Job'}),
        ],
    ),
    'i_need_help': message(
        'i_need_help_with_message',
        buttons=[
            button('shelter_button', action_link('i_need_shelter'), context={'NeedType': 'Shelter'}),
            button('medical_support_button', action_link('i_need_medical_support'), context={'Need': 'MedicalSupport'}),
            button('material_support_button', action_link('i_need_material_support'), context={'Need': 'Material'}),
            button('jewish_organization_button', action_link('i_need_jewish_organization'), context={'Need': 'Jews'}),
            button('psychological_support_button', action_link('i_need_psychological'), context={'Need': 'Psychological'}),
            button('lawyers_button', action_link('i_need_lawyers'), context={'Need': 'Lawyer'}),
        ],
    ),
    'i_need_shelter': message(
        'how_many_people_looking_shelter_message',
        action=action_input('number', 'how_long_need_shelter'),
    ),
    'how_long_need_shelter': message(
        'how_long_need_shelter_message',
        action=action_input('number', 'data_processing_agreement'),
    ),
    'i_need_medical_support': message(
        'i_need_medical_support_message',
        action=action_input('text', 'data_processing_agreement'),
    ),
    'i_need_material_support': message(
        'what_kind_material_support_message',
        action=action_input('text', 'data_processing_agreement'),
    ),
    'i_need_jewish_organization': message(
        'jewish_info_message',
        action=action_input('text', 'data_processing_agreement'),
    ),
    'i_need_psychological': message(
        'psychological_info_message',
        action=action_input('text', 'root'),
    ),
    'i_need_lawyers': message(
        'lawyers_info_message',
        action=action_input('text', 'root'),
    ),
    'data_processing_agreement': message(
        'data_processing_agreement_consent_message',
        buttons=[
            button('no_button', action_link('______i_do_not_consent')),
            button('share_your_telegram_contact_message', action_link('______')),
        ],
    ),
    'i_need_job': message(
        'job_info_message',
        buttons=[
            button('back_to_main_menu_button', action_link('root')),
        ],
    ),
}


# validate that all links exist in messages
do_exit = False
for link in links_to_check:
    if link not in messages:
        print(f'Referenced link "{link}" is not in messages')
        do_exit = True


# TODO: uncomment
# if do_exit:
#     print('\n------- ( ! ) ------- \nYou have links to messages which don\'t exist (see above). Please resolve this and try again. No output file generated.\n------- ( ! ) -------')
#     exit()

print('\n'.join(all_translation_keys))


with open('messages.json', 'w') as f:
    f.write(json.dumps(messages, indent=2))
