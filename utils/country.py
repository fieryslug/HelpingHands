import pycountry
import unidecode
from constants import countries


special = {
    'laopdr': 'LAO',
    'swaziland': 'SWZ',
    'unitedstates': 'USA',
    'czechrepublic': 'CZE',
    'antigua&deps': 'ATG',
    'capeverde': 'CPV',
    'eattimor': 'TLS',
    'bosniaherzegovina': 'BIH'
}

def get_code(name):

    name = preprocess(name)

    if name in countries.country_code:
        return countries.country_code[name]

    if name in special.keys():
        return special[name]

    for country in pycountry.countries:
        n = preprocess(country.name)
        if n.find(name) != -1:
            return country.alpha_3



    return 'unknown'


def preprocess(name):
    name = name.lower()
    name = name.replace(' ', '')
    name = unidecode.unidecode(name)
    name = name.replace('st.', 'saint')
    return name
