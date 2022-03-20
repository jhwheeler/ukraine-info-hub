from utils import (
    message,
    action_link,
    action_input,
    button,
    main_menu_button,
)

from messages.utils import location_select


messages = {
    'i_can_help_i_represent': message(
        'i_represent_message',
        buttons=[
            button(
                'government_button',
                action_link('can_help_i_am_now_in'),
                context={'Represent': 'Government'},
            ),
            button(
                'non_government_org_button',
                action_link('can_help_i_am_now_in'),
                context={'Represent': 'Non-government organization'},
            ),
            button(
                'company_button',
                action_link('can_help_i_am_now_in'),
                context={'Represent': 'Company'},
            ),
            button(
                'individual_button',
                action_link('can_help_i_am_now_in'),
                context={'Represent': 'Individual'},
            ),
        ],
    ),
    **location_select('can_help_i_am_now_in', 'i_can_help'),
    'i_can_help': message(
        'i_can_help_message',
        buttons=[
            button('i_can_help_to_mothers_button', action_link('i_can_help_to_mothers')),
            button('i_can_help_law_button', action_link('i_can_help_law')),
            button('i_can_help_psychology_button', action_link('i_can_help_psychology')),
            button('i_can_volunteer_button', action_link('i_can_volunteer')),
            button('i_can_provide_material_support_button', action_link('i_can_provide_material_support')),
            button('i_can_provide_financial_support_button', action_link('i_can_provide_financial_support')),
            button('i_can_provide_employment_button', action_link('i_can_provide_employment')),
            button('i_can_provide_shelter_button', action_link('i_can_provide_shelter')),
            button('i_can_provide_food_button', action_link('i_can_provide_food')),
            button('i_can_provide_transport_button', action_link('i_can_provide_transport')),
            button('i_can_provide_transport_people_button', action_link('i_can_provide_transport_people')),
            button('i_can_provide_assistance_in_ukraine_button', action_link('i_can_provide_assistance_in_ukraine')),
            button('i_can_provide_other_button', action_link('i_can_provide_other')),
        ],
    ),
    'i_can_help_to_mothers': message('i_can_help_mothers_message', **main_menu_button),
    'i_can_help_law': message('i_can_help_law_message', **main_menu_button),
    'i_can_help_psychology': message('i_can_help_psychology_message', **main_menu_button),
    'i_can_volunteer': message('i_can_volunteer_message', **main_menu_button),
    'i_can_provide_material_support': message('i_can_provide_material_support_message', **main_menu_button),
    'i_can_provide_financial_support': message('i_can_provide_financial_support_message', **main_menu_button),
    'i_can_provide_employment': message('i_can_provide_employment_message', **main_menu_button),
    'i_can_provide_shelter': message('i_can_provide_shelter_message', **main_menu_button),
    'i_can_provide_food': message('i_can_provide_food_message', **main_menu_button),
    'i_can_provide_transport': message('i_can_provide_transport_message', **main_menu_button),
    'i_can_provide_transport_people': message('i_can_provide_transport_people_message', **main_menu_button),
    'i_can_provide_assistance_in_ukraine': message('i_can_provide_assistance_in_ukraine_message', **main_menu_button),
    'i_can_provide_other': message('i_can_provide_other_message', **main_menu_button),
}
