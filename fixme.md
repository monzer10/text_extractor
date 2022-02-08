## fixes:

1. `recognize_google()`:
    It limits the duration. meaning that, if your audio is too long compared to your 
    internet connection speed it will produce a RequestError.
    
    Recommended fix: find an offline `recognizer`