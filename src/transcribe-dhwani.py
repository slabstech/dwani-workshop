import gradio as gr
import requests

# List of supported languages
LANGUAGES = [
    "malayalam",
    "tamil",
    "telugu",
    "hindi", 
    "kannada"
]

# Function to extract language name
def get_lang_name(lang_string):
    return lang_string.split("(")[0].strip().lower()

def transcribe_api(audio_file, language):
    url = f"https://slabstech-dhwani-server-workshop.hf.space/v1/transcribe/?language={get_lang_name(language)}"
    
    headers = {
        "accept": "application/json",
    }
    
    # Open the file in binary mode
    with open(audio_file, 'rb') as f:
        files = {
            "file": (audio_file, f, "audio/x-wav")
        }
        try:
            response = requests.post(url, headers=headers, files=files)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return f"Error: {str(e)}"

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