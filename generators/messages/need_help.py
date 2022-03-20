from utils import (
    message,
    action_link,
    action_input,
    button,
)

from messages.utils import location_select


messages = {
    **location_select('need_help_i_am_now_in', 'i_need_help'),
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
        'i_need_shelter_info_message',
        buttons=[
            button('main_menu_button', action_link('main_menu')),
        ],
    ),
    'i_need_medical_support': message(
        'i_need_medical_support_message',
        buttons=[
            button('main_menu_button', action_link('main_menu')),
        ],
    ),
    'i_need_material_support': message(
        'i_need_material_support_message',
        buttons=[
            button('main_menu_button', action_link('main_menu')),
        ],
    ),
    'i_need_jewish_organization': message(
        'i_need_jewish_info_message',
        buttons=[
            button('main_menu_button', action_link('main_menu')),
        ],
    ),
    'i_need_psychological': message(
        'i_need_psychological_info_message',
        buttons=[
            button('main_menu_button', action_link('main_menu')),
        ],
    ),
    'i_need_lawyers': message(
        'i_need_lawyers_info_message',
        buttons=[
            button('main_menu_button', action_link('main_menu')),
        ],
    ),
}
