"""
     _____         _     _____      _                  _             
    |_   _|____  _| |_  | ____|_  _| |_ _ __ __ _  ___| |_ ___  _ __ 
      | |/ _ \ \/ / __| |  _| \ \/ / __| '__/ _` |/ __| __/ _ \| '__|
      | |  __/>  <| |_  | |___ >  <| |_| | | (_| | (__| || (_) | |   
      |_|\___/_/\_\\__| |_____/_/\_\\__|_|  \__,_|\___|\__\___/|_|   


    This script extracts the text from an audio file. It is assumed that
    the spoken language in the audio is either (ar)abic or (en)glish and
    the duration of the audio is not too long(depending on your internet
    connection speed an error might accur)
    
    This tool accepts .wav format (see README.md for more details about
    supported formats)
    
    Requirments:
    speech_recognition: contains the tool that recognize Text
    bidi.algorithm: formats the text correctly (not necessary for 'en')
    NOTE: languages like 'ar' requires using it 2 times

    This tool produces (.txt) file containing the extracted text.

    see README.md for more details on how to use the tool and for how to
    install the requirments
"""

from speech_recognition import Recognizer, AudioFile, UnknownValueError, RequestError
from sys import argv, exit
from bidi.algorithm import get_display


# check if the user provided all the necessary arguments
if len(argv) != 3:
    print("Usage: python3 __init__.py audio_file lang_code")
    exit(1)

# make an instance of the Recognizer class
r = Recognizer()

# load audio into the memory
with AudioFile(argv[1]) as source:
    audio = r.record(source)

# extract the text if couldn't finish the program with understandable message
try:
    # FIXME: use another recognizer (Recommended: offline one)
    # This limits audio duration depending on your internet connection speed
    text = get_display(get_display(r.recognize_google(audio, language=argv[2])))

except UnknownValueError:
    print("Could not understand audio!!")
    exit(1)

except RequestError:
    print("Could not fulfill your request. Please check your internet connection")
    exit(1)

# write the extracted text to .txt file
file = open(argv[2] + '-Text.txt', 'w')
file.write(text)
file.close()