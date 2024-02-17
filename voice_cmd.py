# Import necessary libraries
from vosk import Model, KaldiRecognizer
import pyaudio
import pyttsx3
import json
from Pluto import pluto  # Assuming Pluto is a module or class to control a drone

# Initialize Vosk model for speech recognition
model = Model(r"C:/Users/creat/Downloads/py_drona/drone_pyprograms/vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, 16000)

# Initialize PyAudio for microphone input
mic = pyaudio.PyAudio()  # Make sure your microphone is enabled and working
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

# Initialize Pluto object for controlling the drone
my_pluto = pluto()

# Initialize pyttsx3 for text-to-speech conversion
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)

# Continuously listen for speech input and control the drone accordingly
while True:
    data = stream.read(4096)
    
    # Process the received audio data for speech recognition
    if recognizer.AcceptWaveform(data):
        text = recognizer.Result()
        data = json.loads(text)
        text = data["text"]
        print(text)  # Print the recognized text
        
        # If no speech was recognized, prompt the user to speak again
        if text == "":
            engine.say("Could not understand, please speak again!")
            engine.runAndWait()            
        else:
            # Depending on the recognized command, control the drone
            if text == "hello":
                my_pluto.arm()
            elif text == "take off":
                my_pluto.take_off()
            elif text == "land":
                my_pluto.land()
            elif text == "calmdown":
                my_pluto.disarm()
                
            # Speak out the recognized text
            engine.say("You said " + text)
            engine.runAndWait()  # Wait for the speech to finish
