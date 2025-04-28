import gradio as gr
import requests
from PIL import Image
import io

def visual_query(image, src_lang, tgt_lang, prompt):
    # API endpoint

    import os

    # Get the base URL (IP or domain) from environment variable
    base_url = os.getenv("DWANI_AI_API_BASE_URL")

    if not base_url:
        raise ValueError("DWANI_AI_API_BASE_URL environment variable is not set")

    # Define the endpoint path
    endpoint = "/v1/visual_query"

    # Construct the full API URL
    url = f"{base_url.rstrip('/')}{endpoint}"

    # Prepare the query parameters
    params = {
        "src_lang": src_lang,
        "tgt_lang": tgt_lang
    }

    # Convert the image to bytes
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    # Prepare the files and data for the POST request
    files = {
        'file': ('image.png', img_byte_arr, 'image/png')
    }
    data = {
        'query': prompt
    }

    # Set headers
    headers = {
        'accept': 'application/json'
    }

    try:
        # Send the POST request
        response = requests.post(url, params=params, headers=headers, files=files, data=data)
        
        # Check if the request was successful
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Exception occurred: {str(e)}"

# Create Gradio interface
iface = gr.Interface(
    fn=visual_query,
    inputs=[
        gr.Image(type="pil", label="Upload Image"),
        gr.Textbox(label="Source Language (e.g., kan_Knda)", placeholder="kan_Knda"),
        gr.Textbox(label="Target Language (e.g., kan_Knda)", placeholder="kan_Knda"),
        gr.Textbox(label="Prompt", placeholder="e.g., describe the image")
    ],
    outputs=gr.JSON(label="API Response"),
    title="Visual Query API Interface",
    description="Upload an image, specify source and target languages, and provide a prompt to query the visual API."
)

# Launch the interface
iface.launch()