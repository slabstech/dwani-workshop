import gradio as gr
import requests

def chat_api(prompt, language, token):
    url = "https://slabstech-dhwani-server.hf.space/v1/chat"
    
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "prompt": prompt,
        "src_lang": language
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
                placeholder="Enter your prompt here (e.g., 'hello')"
            )
            language_input = gr.Textbox(
                label="Source Language",
                placeholder="Enter language code (e.g., 'kan_Knda')",
                value="kan_Knda"
            )
            token_input = gr.Textbox(
                label="Bearer Token",
                placeholder="Enter your authorization token",
                type="password",
                #value="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaHdhbmktd29ya3Nob3BAZXhhbXBsZS5jb20iLCJleHAiOjE3NDI0NTkwNzEuMzk4NjF9.zk3WWuoTjYGbAzDSIOXhkOiiG6p-UkqxKapq8T4JlKs"
                value=""

            )
            
            submit_btn = gr.Button("Submit")
        
        with gr.Column():
            # Output component
            output = gr.JSON(label="Response")
    
    # Connect the button click to the API function
    submit_btn.click(
        fn=chat_api,
        inputs=[prompt_input, language_input, token_input],
        outputs=output
    )

# Launch the interface
demo.launch()