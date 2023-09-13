import json


def get_translation(locale, key):
    try:
        with open(f'locales/{locale}.json') as f:
            translations = json.load(f)
            return translations.get(key, key)
    except FileNotFoundError:
        return key
