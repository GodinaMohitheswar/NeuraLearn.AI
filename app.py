import openai
import streamlit as st
from gtts import gTTS
import speech_recognition as sr
import os

# Set your OpenAI API key
openai.api_key = "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"

# Function to get AI response using the old API (Completion)
def get_ai_response(prompt):
    try:
        # Correct API call using the old method for completions
        response = openai.Completion.create(
            model="text-davinci-003",  # You can use other models like "gpt-3.5-turbo"
            prompt=prompt,
            max_tokens=150
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
