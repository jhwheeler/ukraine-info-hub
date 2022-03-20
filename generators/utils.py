
from unidecode import unidecode

import pycountry_convert


links_to_check = []
all_translation_keys = set()


def fix_country_name(country_name):
    # Taiwan is an independent state!
    if ',' in country_name:
        country_name = country_name.split(',')[0]
    
    return country_name


def country_name_to_key(country_name):
    return unidecode(
        country_name
        .replace(' ', '_')
        .replace('(', '')
        .replace(')', '')
        .replace('\'', '')
        .lower()
         + '_country'
    )


def add_translation_key(message):
    global all_translation_keys
    all_translation_keys.add(message)


def validate_action(action):
    action_type = action['type']

    if action_type == 'link' and 'destination' not in action:
        raise ValueError('Action with link has no destination')

    if action_type == 'number' and 'input_type' not in action:
        raise ValueError(f'Action with input has no input type: {action}')
    
    return action


def validate_button(button):
    if not button.get('message'):
        raise ValueError('Button has no message')

    if not button.get('action'):
        raise ValueError('Button has no action')

    button['action'] = validate_action(button['action'])

    return button


def validate_buttons(buttons):
    return [validate_button(button) for button in buttons]


def validate_context(context):
    return context


def action_link(destination):
    global links_to_check
    links_to_check.append(destination)

    return {
        'type': 'link',
        'destination': destination,
    }


def action_input(input_type, destination):
    global links_to_check
    links_to_check.append(destination)

    return {
        'type': 'input',
        'input_type': input_type,
        'post_action_destination': destination,
    }


def button(message, action, context=None):
    add_translation_key(message)

    return {
        'message': message,
        'action': action,
        **({'context': validate_context(context)} if context else {}),
    }


def message(message, buttons=None, action=None):
    add_translation_key(message)

    return {
        'message': message,
        **({'buttons': validate_buttons(buttons)} if buttons else {}),
        **({'action': validate_action(action)} if action else {}),
    }


def get_country_importance(country):
    if country.alpha_2 == 'PL':
        return 1

    if country.alpha_2 == 'HU':
        return 2

    if country.alpha_2 in ['PL', 'SK', 'RO', 'MD', 'GE']:
        return 3

    if country.alpha_2 in ['EE', 'LT', 'LV', 'DE', 'CZ', 'SL', 'CR', 'RS', 'MC', 'BG']:
        return 4

    try:
        continent = pycountry_convert.country_alpha2_to_continent_code(country.alpha_2)
    except Exception:
        return 9

    if continent == 'EU':
        return 5

    return 9


main_menu_button = {'buttons': [button('main_menu_button', action_link('main_menu'))]}
