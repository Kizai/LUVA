import sounddevice as sd
import soundfile as sf
import numpy as np

# Set the duration of the recording in seconds
duration = 10


# Record audio
def record_audio():
    # Get the sample rate
    sample_rate = 44100
    # Record audio
    audio = sd.rec(int(sample_rate * duration), samplerate=sample_rate, channels=2, dtype='int16')
    sd.wait()
    # Save the audio file
    sf.write('output.wav', audio, sample_rate, 'PCM_16')
