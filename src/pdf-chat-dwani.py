import gradio as gr
import requests

# Function to send the POST request to the API
def extract_text_from_pdf(pdf_file, page_number):
    # API endpoint
    url = "http://209.20.158.215:7861/extract-text-eng/"

    # Prepare the payload
    files = {
        "file": (pdf_file.name, pdf_file, "application/pdf")
    }
    data = {
        "page_number": str(page_number),
        "src_lang": "eng_Latn",
        "tgt_lang": "eng_Latn",
        "prompt": "describe the image"
    }

    # Headers
    headers = {
        "accept": "application/json"
    }

    try:
        # Send the POST request
        response = requests.post(url, files=files, data=data, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            return response.json().get("result", "No result returned from API")
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Error: Failed to connect to the API - {str(e)}"

# Gradio interface
with gr.Blocks(title="PDF Text Extraction") as demo:
    gr.Markdown("# Extract Text from PDF and Describe Content")
    
    # Input components
    pdf_input = gr.File(label="Upload PDF File", file_types=[".pdf"])
    page_number_input = gr.Number(label="Page Number", value=1, precision=0, minimum=1)
    
    # Submit button
    submit_button = gr.Button("Extract and Describe")
    
    # Output component
    output_text = gr.Textbox(label="API Response", lines=10)
    
    # Connect the button to the function
    submit_button.click(
        fn=extract_text_from_pdf,
        inputs=[pdf_input, page_number_input],
        outputs=output_text
    )

# Launch the Gradio app
demo.launch()