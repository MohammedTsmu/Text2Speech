from gtts import gTTS
import pygame
import os

def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    audio_file = "output.mp3"
    tts.save(audio_file)
    
    # Initialize pygame mixer and play the saved file
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    
    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    return audio_file

if __name__ == "__main__":
    text = input("Enter the text to convert to speech: ")
    lang = input("Enter the language code (default is 'en'): ") or 'en'
    audio_file = text_to_speech(text, lang)
    print(f"Audio saved to {audio_file}")
