import streamlit as st
import openai
from gtts import gTTS
import speech_recognition as sr
import os

# Set your OpenAI API key
openai.api_key = "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"

# Function to get AI response from GPT-3 (or GPT-4) using the updated API method
def get_ai_response(prompt):
    try:
        # Use Completion.create for the latest OpenAI API
        response = openai.Completion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if you have access
            prompt=prompt,
            max_tokens=150  # Adjust this based on your need
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {e}"

# Function to convert text to speech
def text_to_speech(text, filename="explanation.mp3"):
    tts = gTTS(text, lang='en')
    tts.save(filename)
    return filename

# Function for voice input (file upload)
def record_voice(uploaded_audio):
    recognizer = sr.Recognizer()

    # Open the uploaded audio file and recognize speech
    with sr.AudioFile(uploaded_audio) as source:
        audio = recognizer.record(source)

    try:
        # Recognize speech using Google Speech Recognition
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I could not understand the audio."
    except sr.RequestError:
        return "Could not request results from Google Speech Recognition service."

# Streamlit app structure
def run_app():
    st.title("NeuraLearn.AI: AI-Powered Smart Learning")
    st.header("Topic-Based AI Video Explanation")
    
    # Text input or voice input
    input_choice = st.radio("Choose input method", ('Text', 'Voice'))
    
    if input_choice == 'Text':
        user_input = st.text_input("Enter your topic:")
    else:
        uploaded_audio = st.file_uploader("Upload an audio file", type=["wav", "mp3"])
        if uploaded_audio:
            user_input = record_voice(uploaded_audio)  # Function to handle voice input
        else:
            user_input = None
    
    if user_input:
        st.subheader("AI Generated Text Answer:")
        
        # Get AI response from OpenAI API
        ai_response = get_ai_response(user_input)
        
        st.write(ai_response)
        
        # Convert to speech
        if st.button("Generate Voice Explanation"):
            audio_file = text_to_speech(ai_response)
            st.audio(audio_file, format="audio/mp3")
        
        # Generate video explanation (mocked - would require real video generation tech)
        if st.button("Generate Video Explanation"):
            st.write("Video explanation generation is coming soon!")

# Run the app
if __name__ == "__main__":
    run_app()
