import csv
import gettext
from utils import fix_country_name, country_name_to_key

import pycountry


with open('static/country_translations.csv', 'w') as f:
    # create the csv writer
    writer = csv.writer(f)

    languages = ['uk-UA', 'ru-UA']

    writer.writerow(['Key', 'en-US'] + languages + ['Description'])

    for country in pycountry.countries:
        english_name = fix_country_name(country.name)
        translation_key = country_name_to_key(english_name)

        row = [translation_key, english_name]

        for language_code in languages:
            lang = gettext.translation('iso3166', pycountry.LOCALES_DIR, languages=[language_code[:2]])
            lang.install()

            row.append(fix_country_name(_(country.name)))

        row.append(f'Country name for {country.name}')

        writer.writerow(row)

print('done')
