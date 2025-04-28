import gradio as gr
import requests
import urllib.parse
import tempfile
import os

def text_to_speech(text):
    # Validate input
    if not text or not isinstance(text, str):
        raise ValueError("Input text must be a non-empty string")

    # Get the base URL from environment variable
    base_url = os.getenv("DWANI_AI_API_BASE_URL")
    if not base_url:
        raise ValueError("DWANI_AI_API_BASE_URL environment variable is not set")

    # Define the endpoint path
    endpoint = "/v1/audio/speech"
    
    # Construct query parameters
    query_params = urllib.parse.urlencode({"input": text, "response_format": "mp3"})
    url = f"{base_url.rstrip('/')}{endpoint}?{query_params}"

    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(url, headers=headers, json={})
        response.raise_for_status()
        
        # Save the audio content to a temporary file
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_file:
            temp_file.write(response.content)
            temp_file_path = temp_file.name
        
        return temp_file_path
    except requests.exceptions.RequestException as e:
        raise ValueError(f"API request failed: {str(e)}")
    except IOError as e:
        raise ValueError(f"Failed to save audio file: {str(e)}")

# Create Gradio interface
with gr.Blocks(title="Text to Speech API Interface") as demo:
    gr.Markdown("# Text to Speech API Interface")
    
    with gr.Row():
        with gr.Column():
            # Input components
            text_input = gr.Textbox(
                label="Text",
                placeholder="Enter text to convert to speech",
                value="ಕರ್ನಾಟಕದ ರಾಜಧಾನಿ ಬೆಂಗಳೂರು."
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
        inputs=[text_input],
        outputs=audio_output
    )

# Launch the interface
try:
    demo.launch(server_name="0.0.0.0", server_port=7860)
except Exception as e:
    print(f"Failed to launch Gradio interface: {str(e)}")