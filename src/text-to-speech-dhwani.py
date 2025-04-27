import gradio as gr
import requests

def text_to_speech(text):
    # Construct URL with plain text as query parameter
    url = (f"https://slabstech-dhwani-server-workshop.hf.space/v1/audio/speech?"
           f"input={text}&response_format=mp3")
    
    headers = {
        "accept": "application/json"
    }
    
    try:
        response = requests.post(url, headers=headers, data='')
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
                value="ಕರ್ನಾಟಕದ ರಾಜಧಾನಿ ಬೆಂಗಳೂರು."  # Example from curl
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
demo.launch()