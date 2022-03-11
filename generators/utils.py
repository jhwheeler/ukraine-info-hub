links_to_check = []


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


def button(message, action):
    return {
        'message': message,
        'action': action,
    }


def message(message, buttons=None, action=None):
    return {
        'message': message,
        **({'buttons': validate_buttons(buttons)} if buttons else {}),
        **({'action': validate_action(action)} if action else {}),
    }
