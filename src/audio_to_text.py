import speech_recognition as sr


# Convert audio to text
def audio_to_text(filename):
    # Initialize recognizer
    r = sr.Recognizer()
    # Open the file
    with sr.AudioFile(filename) as source:
        # Listen for the data (load audio to memory)
        audio_data = r.record(source)
        # Recognize (convert from speech to text)
        text = r.recognize_google(audio_data, language='zh-CN')
        return text
