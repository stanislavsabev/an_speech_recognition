
import re
import speech_recognition as sr
from google_trans_new import google_translator

import pyttsx3

from siri import speak, take_command 


LANGUAGES = {
    'afrikaans' : 'af',
    'albanian' : 'sq',
    'amharic' : 'am',
    'arabic' : 'ar',
    'armenian' : 'hy',
    'azerbaijani' : 'az',
    'basque' : 'eu',
    'belarusian' : 'be',
    'bengali' : 'bn',
    'bosnian' : 'bs',
    'bulgarian' : 'bg',
    'catalan' : 'ca',
    'cebuano' : 'ceb',
    'chichewa' : 'ny',
    'chinese (simplified)' : 'zh-c',
    'chinese (traditional)' : 'zh-t',
    'corsican' : 'co',
    'croatian' : 'hr',
    'czech' : 'cs',
    'danish' : 'da',
    'dutch' : 'nl',
    'english' : 'en',
    'esperanto' : 'eo',
    'estonian' : 'et',
    'filipino' : 'tl',
    'finnish' : 'fi',
    'french' : 'fr',
    'frisian' : 'fy',
    'galician' : 'gl',
    'georgian' : 'ka',
    'german' : 'de',
    'greek' : 'el',
    'gujarati' : 'gu',
    'haitian creole' : 'ht',
    'hausa' : 'ha',
    'hawaiian' : 'haw',
    'hebrew' : 'iw',
    'hebrew' : 'he',
    'hindi' : 'hi',
    'hmong' : 'hmn',
    'hungarian' : 'hu',
    'icelandic' : 'is',
    'igbo' : 'ig',
    'indonesian' : 'id',
    'irish' : 'ga',
    'italian' : 'it',
    'japanese' : 'ja',
    'javanese' : 'jw',
    'kannada' : 'kn',
    'kazakh' : 'kk',
    'khmer' : 'km',
    'korean' : 'ko',
    'kurdish (kurmanji)' : 'ku',
    'kyrgyz' : 'ky',
    'lao' : 'lo',
    'latin' : 'la',
    'latvian' : 'lv',
    'lithuanian' : 'lt',
    'luxembourgish' : 'lb',
    'macedonian' : 'mk',
    'malagasy' : 'mg',
    'malay' : 'ms',
    'malayalam' : 'ml',
    'maltese' : 'mt',
    'maori' : 'mi',
    'marathi' : 'mr',
    'mongolian' : 'mn',
    'myanmar (burmese)' : 'my',
    'nepali' : 'ne',
    'norwegian' : 'no',
    'odia' : 'or',
    'pashto' : 'ps',
    'persian' : 'fa',
    'polish' : 'pl',
    'portuguese' : 'pt',
    'punjabi' : 'pa',
    'romanian' : 'ro',
    'russian' : 'ru',
    'samoan' : 'sm',
    'scots gaelic' : 'gd',
    'serbian' : 'sr',
    'sesotho' : 'st',
    'shona' : 'sn',
    'sindhi' : 'sd',
    'sinhala' : 'si',
    'slovak' : 'sk',
    'slovenian' : 'sl',
    'somali' : 'so',
    'spanish' : 'es',
    'sundanese' : 'su',
    'swahili' : 'sw',
    'swedish' : 'sv',
    'tajik' : 'tg',
    'tamil' : 'ta',
    'telugu' : 'te',
    'thai' : 'th',
    'turkish' : 'tr',
    'turkmen' : 'tk',
    'ukrainian' : 'uk',
    'urdu' : 'ur',
    'uyghur' : 'ug',
    'uzbek' : 'uz',
    'vietnamese' : 'vi',
    'welsh' : 'cy',
    'xhosa' : 'xh',
    'yiddish' : 'yi',
    'yoruba' : 'yo',
    'zulu' : 'zu',
}

#Translation function
def trans(result):
    # print('What language you want to translate to?')
    speak('What language you want to translate to? :')
    i = 0
    while i < 2:
        langinput = take_command()
        language = LANGUAGES.get(str(langinput.lower()))
        if language is None:
            speak('Unknown language, try again!')
            i += 1
            continue
    if language is None:
        return ''

    translator=google_translator()
    translate_text=translator.translate(result ,lang_tgt=language, lang_src='en')
    return translate_text