import pycountry


from utils import (
    message,
    action_link,
    button,
    get_country_importance,
    fix_country_name,
    country_name_to_key,
)


UKRANIAN_CITIES = ['Kyiv', 'Dnipro', 'Kharkiv', 'Melitopol', 'Other']
IMPORTANT_COUNTRIES = ['Poland', 'Romania', 'Moldova', 'France', 'Germany', 'Italy', 'Austria', 'Spain', 'Sweden', 'Switzerland', 'Belgium', 'Czech Republic']


def location_select(entry_message, exit_to):
    return {
        entry_message: message(
            'i_am_now_in_message',
            buttons=[
                button('country_ukraine', action_link('select_ukrainian_city'), context={'Country': 'Ukraine'}),
                button('other_country_button', action_link('select_important_country')),
            ],
        ),
        'select_ukrainian_city': message(
            'select_which_city_message',
            buttons=[
                button(
                    country_name_to_key(city_name),
                    action_link(exit_to),
                    context={'City': city_name},
                )
                for city_name in UKRANIAN_CITIES
            ]
        ),
        'select_important_country': message(
            'select_a_country_message',
            buttons=[
                # TODO: use correct country keys
                button(
                    country_name_to_key(fix_country_name(c)),
                    action_link(exit_to),
                    context={'Country': fix_country_name(c)},
                )
                for c in IMPORTANT_COUNTRIES
            ] + [button('other_button', action=action_link('select_all_countries'))],
        ),
        'select_all_countries': message(
            'select_a_country_message',
            buttons=[
                # TODO: use correct country keys
                button(
                    country_name_to_key(fix_country_name(c.name)),
                    action_link(exit_to),
                    context={'Country': fix_country_name(c.name)},
                )
                for c in sorted(list(pycountry.countries), key=lambda c: get_country_importance(c))
            ],
        ),
    }
