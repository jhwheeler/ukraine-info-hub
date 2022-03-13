import json
import pycountry


from utils import (
    message,
    action_link,
    action_input,
    button,
    links_to_check,
    get_country_importance,
    fix_country_name,
)


messages = {
    'root': message(
        'What do you need?',
        buttons=[
            button('Help', action_link('i_am_now_in')),
            button('Donate', action_link('donate')),
            button('Main Info', action_link('main_info')),
            button('About Us', action_link('about_us')),
        ],
    ),
    'donate': message('Thank you for helping. Here are charities collecting donations for people in need:'),
    'main_info': message('We have collected different groups and resources for people helping those in need:'),
    'about_us': message('Grow Ukraine is a group of volunteers working to solve the complex logistics of humanitarian aid delivery'),
    'i_am_now_in': message(
        'I am now in...',
        buttons=[
            button('Country Ukraine', action_link('i_need'), context={'Country': 'Ukraine'}),
            button('Other country', action_link('select_counry_currently_in')),
        ],
    ),
    'select_counry_currently_in': message(
        'Select a country',
        buttons=[
            button(fix_country_name(c.name), action_link('i_need'), context={'Country': fix_country_name(c.name)})
            for c in sorted(pycountry.countries, key=lambda c: get_country_importance(c))
        ],
    ),
    'i_need': message(
        'I need',
        buttons=[
            button('Help', action_link('i_need_help'), context={'Need': 'Help'}),
            button('Job', action_link('i_need_job'), context={'Need': 'Job'}),
        ],
    ),
    'i_need_help': message(
        'I need help with',
        buttons=[
            button('Shelter', action_link('i_need_shelter'), context={'NeedType': 'Shelter'}),
            button('Medical support', action_link('i_need_medical_support'), context={'Need': 'MedicalSupport'}),
            button('Material support', action_link('i_need_material_support'), context={'Need': 'Material'}),
            button('Jewish organizations', action_link('i_need_jewish_organization'), context={'Need': 'Jews'}),
            button('Psychological support', action_link('i_need_psychological'), context={'Need': 'Psychological'}),
            button('Lawyers', action_link('i_need_lawyers'), context={'Need': 'Lawyer'}),
        ],
    ),
    'i_need_shelter': message(
        'How many people are looking for shelter?',
        action=action_input('number', 'how_many_people_need_shelter'),
    ),
    'how_many_people_need_shelter': message(
        'How many people are looking for shelter?',
        action=action_input('number', 'data_processing_agreement'),
    ),
    'i_need_medical_support': message(
        'What kind of medical support do you need?',
        action=action_input('text', 'data_processing_agreement'),
    ),
    'i_need_material_support': message(
        'What kind of material support do you need?',
        action=action_input('text', 'data_processing_agreement'),
    ),
    'i_need_jewish_organization': message(
        '___JEWISH INFO___',
        action=action_input('text', 'data_processing_agreement'),
    ),
    'i_need_psychological': message(
        'Check out the following information: ___PSYCHOLOGICAL INFO___',
        action=action_input('text', 'root'),
    ),
    'i_need_lawyers': message(
        'Check out the following information: ___LAWYER INFO___',
        action=action_input('text', 'root'),
    ),
    'data_processing_agreement': message(
        'Let\'s proceed.\nDo you give your consent tot the processing of your personal data (___agreement url___)?',
        buttons=[
            button('No', action_link('______i_do_not_consent')),
            button('Share your telegram contact', action_link('______')),
        ],
    ),
    'i_need_job': message(
        '___ JOB INFO ___',
        buttons=[
            button('Back to main menu', action_link('root')),
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


with open('messages.json', 'w') as f:
    f.write(json.dumps(messages, indent=2))
