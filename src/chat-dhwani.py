import gradio as gr
import requests

def chat_api(prompt, language, tgt_language):
    url = "https://slabstech-dhwani-server-workshop.hf.space/v1/chat"
    
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    
    payload = {
        "prompt": prompt,
        "src_lang": language,
        "tgt_lang": tgt_language
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

# Create Gradio interface
with gr.Blocks(title="Chat API Interface") as demo:
    gr.Markdown("# Chat API Interface")
    
    with gr.Row():
        with gr.Column():
            # Input components
            prompt_input = gr.Textbox(
                label="Prompt",
                placeholder="Enter your prompt here (e.g., 'hi')"
            )
            language_input = gr.Textbox(
                label="Source Language",
                placeholder="Enter source language code (e.g., 'eng_Latn')",
                value="eng_Latn"
            )
            tgt_language_input = gr.Textbox(
                label="Target Language",
                placeholder="Enter target language code (e.g., 'eng_Latn')",
                value="eng_Latn"
            )
            
            submit_btn = gr.Button("Submit")
        
        with gr.Column():
            # Output component
            output = gr.JSON(label="Response")
    
    # Connect the button click to the API function
    submit_btn.click(
        fn=chat_api,
        inputs=[prompt_input, language_input, tgt_language_input],
        outputs=output
    )

# Launch the interface
demo.launch()