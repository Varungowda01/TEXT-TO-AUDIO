import pyttsx3


from indic_tts.tts import TTS

def text_to_speech_english(text):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set properties (optional)
    rate = engine.getProperty('rate')   # Get current speech rate
    engine.setProperty('rate', rate-50) # Decrease the rate (slower speech)
    volume = engine.getProperty('volume') # Get current volume level (0.0 to 1.0)
    engine.setProperty('volume', volume+0.25) # Increase the volume

    # Set the voice (optional)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id) # Change the voice (0 for male, 1 for female)

    # Convert text to speech
    engine.say(text)
    engine.runAndWait()

def text_to_speech_sanskrit(text):
    # Initialize the TTS engine for Sanskrit
    tts = TTS('sanskrit')

    # Generate the speech
    wav_data = tts.text_to_speech(text)

    # Play the audio
    play_obj = sa.play_buffer(wav_data, 1, 2, 16000)
    play_obj.wait_done()

if __name__ == "__main__":
    english_text = "Hello, this is a test of the English text-to-speech functionality."
    sanskrit_text = "नमः, एषः संस्कृतभाषायाः पाठवाचनकार्यस्य परीक्षणम् अस्ति।"

    print("Playing English text...")
    text_to_speech_english(english_text)

    print("Playing Sanskrit text...")
    text_to_speech_sanskrit(sanskrit_text)
