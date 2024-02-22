from vosk import Model, KaldiRecognizer
import pyaudio
import json


# Initialize Vosk model for speech recognition
model = Model(r"C:/Users/creat/Downloads/py_drona/drone_all-main/drone_all-main/vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, 16000)

# Initialize PyAudio for microphone input
mic = pyaudio.PyAudio()  # Make sure your microphone is enabled and working
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)  # Increased buffer size
stream.start_stream()



# Continuously listen for speech input and recognize it
while True:
    data = stream.read(4096)
    
    # Process the received audio data for speech recognition
    if recognizer.AcceptWaveform(data):
        
        print(recognizer.Result())
        
        
        
   