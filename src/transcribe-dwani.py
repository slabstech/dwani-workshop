import gradio as gr
import requests
import os

# List of supported languages
LANGUAGES = ["malayalam", "tamil", "telugu", "hindi", "kannada"]

# Function to extract language name
def get_lang_name(lang_string):
    return lang_string.split("(")[0].strip().lower()

def transcribe_api(audio_file, language):
    # Get the base URL from environment variable
    base_url = os.getenv("DWANI_AI_API_BASE_URL")

    if not base_url:
        return {"error": "DWANI_AI_API_BASE_URL environment variable is not set"}

    # Define the endpoint path
    endpoint = "v1/transcribe/?language"

    # Construct the full API URL
    url = f"{base_url.rstrip('/')}/{endpoint}={get_lang_name(language)}"
    
    headers = {
        "accept": "application/json",
    }
    
    try:
        # Open the file in binary mode
        with open(audio_file, 'rb') as f:
            files = {
                "file": (os.path.basename(audio_file), f, "audio/x-wav")
            }
            response = requests.post(url, headers=headers, files=files)
            response.raise_for_status()
            return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Create Gradio interface
with gr.Blocks(title="Speech to Text API Interface") as demo:
    gr.Markdown("# Speech to Text API Interface")
    
    with gr.Row():
        with gr.Column():
            # Input components
            audio_input = gr.Audio(
                label="Audio File",
                type="filepath",
                sources=["upload"]
            )
            language_input = gr.Dropdown(
                label="Language",
                choices=LANGUAGES,
                value="kannada"
            )
            
            submit_btn = gr.Button("Transcribe")
        
        with gr.Column():
            # Output component
            output = gr.JSON(label="Transcription Response")
    
    # Connect the button click to the API function
    submit_btn.click(
        fn=transcribe_api,
        inputs=[audio_input, language_input],
        outputs=output
    )

# Launch the interface
demo.launch()