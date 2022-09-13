import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

# set the api from the .env file to authenticate
authenticator = IAMAuthenticator(apikey)

# declare the language translator object
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)
# set the service url from the url in the .env file
language_translator.set_service_url(url)


def english_to_french(englishText):
    """
    This translates English to French.
    """
    translation = language_translator.translate(
        text=englishText,
        model_id='en-fr').get_result()
    frenchText = translation['translations'][0]['translation']
    return frenchText


def french_to_english(frenchText):
    """
    This translates French to English
    """
    translation = language_translator.translate(
        text=frenchText,
        model_id='fr-en').get_result()
    englishText = translation['translations'][0]['translation']
    return englishText
