# Speech-To-Text-Conversion

Speech-to-Text Conversion (Using Python and SpeechRecognition)
## Overview
This Python script listens to your microphone input and converts your speech into text using Google Speech Recognition. It continuously listens and transcribes speech until the phrase "stop listening" is spoken.

## Features
Continuously listens for speech.

Converts speech to text using Google’s Speech-to-Text API.

Stops when the phrase "stop listening" is spoken.

Handles errors gracefully (e.g., unknown speech or request issues).

## Prerequisites
To use this script, you'll need Python 3.x and the following libraries:

SpeechRecognition: Library for speech recognition.

PyAudio: Library required for microphone input support.

## Installation
Install Python 3.x (if not already installed).

Install required libraries:
You can install the necessary Python packages via pip. Open your terminal or command prompt and run the following:

pip install SpeechRecognition
pip install pyaudio  # If you don't have PyAudio installed yet
Check microphone permissions:
Ensure your microphone is set up correctly on your system and that your application has permission to use it.

## Usage
Save the code in a Python file, e.g., speech_to_text.py.

Run the script in your terminal:

python speech_to_text.py
Start speaking! The program will transcribe your speech into text in real-time.

To stop the program, say "stop listening" or manually interrupt it with Ctrl+C.

## Example Output
 Speech-to-Text is running... Say 'stop listening' to exit.

 Speak Now...
 You said: Hello, how are you?

 Speak Now...
 You said: I am fine, thank you!

 Speak Now...
You said: stop listening
Exiting speech recognition loop.
Error Handling
If the program cannot understand your speech, it will display the following message:


 Could not understand your speech.
If there is an issue with the API request, the following message will be displayed:


 Could not request results from the speech service.


## Acknowledgments
SpeechRecognition Library: This script uses the SpeechRecognition library, which makes speech recognition accessible and simple.

