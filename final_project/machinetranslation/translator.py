import logging
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
from ibm_watson import ApiException


load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

# language_translator.set_disable_ssl_verification(True)


def englishToFrench(english_text):
    '''Translate english text to french'''
    try:
        text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    except ApiException as ex:
        #logging.warning("Method failed with status code " + str(ex.code)\
        # + ": " + ex.message)
        return None

    french_text = text['translations'][0]['translation'].strip()
    return french_text

def frenchToEnglish(french_text):
    '''Translate french text to english'''
    try:
        text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    except ApiException as ex:
        #logging.warning("Method failed with status code " + str(ex.code)\
        # + ": " + ex.message)
        return None

    english_text = text['translations'][0]['translation'].strip()
    return english_text


if __name__ == '__main__':
    print(englishToFrench('Hello'))
    print(englishToFrench(''))
    print(frenchToEnglish('Bonjour'))
    print(frenchToEnglish(''))
