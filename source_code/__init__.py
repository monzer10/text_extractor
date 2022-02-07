from speech_recognition import Recognizer, AudioFile, UnknownValueError, RequestError
from sys import argv, exit
from bidi.algorithm import get_display


if len(argv) != 3:
    print("Usage: python3 __init__.py audio_file lang_code")
    exit(1)

r = Recognizer()

with AudioFile(argv[1]) as source:
    audio = r.record(source)

try:
    # TODO: use another recognizer (offline if any)
    # This limits duration depending on your internet connection
    text = get_display(r.recognize_google(audio, language=argv[2]))

except UnknownValueError:
    print("Could not understand audio!!")
    exit(1)

except RequestError as e:
    print("Could not fulfill your request. Please check your internet connection")
    exit(1)

file = open(argv[2] + '-Text.txt', 'w')
file.write(get_display(text))
file.close()