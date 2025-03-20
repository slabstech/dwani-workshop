import gradio as gr
import requests
from urllib.parse import quote

# List of supported languages
LANGUAGES = [
    "Assamese (asm_Beng)", "Kashmiri (Arabic) (kas_Arab)", "Punjabi (pan_Guru)",
    "Bengali (ben_Beng)", "Kashmiri (Devanagari) (kas_Deva)", "Sanskrit (san_Deva)",
    "Bodo (brx_Deva)", "Maithili (mai_Deva)", "Santali (sat_Olck)",
    "Dogri (doi_Deva)", "Malayalam (mal_Mlym)", "Sindhi (Arabic) (snd_Arab)",
    "English (eng_Latn)", "Marathi (mar_Deva)", "Sindhi (Devanagari) (snd_Deva)",
    "Konkani (gom_Deva)", "Manipuri (Bengali) (mni_Beng)", "Tamil (tam_Taml)",
    "Gujarati (guj_Gujr)", "Manipuri (Meitei) (mni_Mtei)", "Telugu (tel_Telu)",
    "Hindi (hin_Deva)", "Nepali (npi_Deva)", "Urdu (urd_Arab)",
    "Kannada (kan_Knda)", "Odia (ory_Orya)"
]

def text_to_speech(text, language, voice, model, token):
    # URL encode the input text
    encoded_text = quote(text)
    
    # Construct URL with query parameters (speed fixed at 1)
    url = (f"https://slabstech-dhwani-server.hf.space/v1/audio/speech?"
           f"input={encoded_text}&"
           f"voice={quote(voice)}&"
           f"model={quote(model)}&"
           f"response_format=mp3&"
           f"speed=1")
    
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {token}",
    }
    
    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        
        # Save the audio content to a temporary file
        temp_file = "temp_output.mp3"
        with open(temp_file, "wb") as f:
            f.write(response.content)
        
        return temp_file
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

# Create Gradio interface
with gr.Blocks(title="Text to Speech API Interface") as demo:
    gr.Markdown("# Text to Speech API Interface")
    
    with gr.Row():
        with gr.Column():
            # Input components
            text_input = gr.Textbox(
                label="Text",
                placeholder="Enter text to convert to speech",
                value="ನಿಮ್ಮ ಇನ್‌ಪುಟ್ ಪಠ್ಯವನ್ನು ಇಲ್ಲಿ ಸೇರಿಸಿ"  # Your example text
            )
            language_input = gr.Dropdown(
                label="Language",
                choices=LANGUAGES,
                value="Kannada (kan_Knda)"
            )
            voice_input = gr.Textbox(
                label="Voice",
                value="Anu speaks with a high pitch at a normal pace in a clear"
            )
            model_input = gr.Textbox(
                label="Model",
                value="ai4bharat/indic-parler-tts"
            )
            token_input = gr.Textbox(
                label="Bearer Token",
                placeholder="Enter your authorization token",
                type="password",
                value=""
            )
            
            submit_btn = gr.Button("Generate Speech")
        
        with gr.Column():
            # Output component
            audio_output = gr.Audio(
                label="Generated Speech",
                type="filepath",
                interactive=False
            )
    
    # Connect the button click to the API function
    submit_btn.click(
        fn=text_to_speech,
        inputs=[text_input, language_input, voice_input, model_input, token_input],
        outputs=audio_output
    )

# Launch the interface
demo.launch()