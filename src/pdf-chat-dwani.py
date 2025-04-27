import gradio as gr
import requests
from PyPDF2 import PdfReader
import io
import os

# Function to validate PDF file
def is_valid_pdf(file_path):
    try:
        # If file_path is a string (Gradio provides a temporary file path)
        if isinstance(file_path, str) and os.path.exists(file_path):
            with open(file_path, "rb") as f:
                pdf = PdfReader(f)
                if len(pdf.pages) > 0:
                    return True, f"Valid PDF with {len(pdf.pages)} pages"
                return False, "Invalid PDF: No pages found"
        else:
            return False, "Invalid PDF: File path is not valid"
    except Exception as e:
        return False, f"Invalid PDF: {str(e)}"

# Function to send the POST request to the API
def extract_text_from_pdf(pdf_file, page_number):
    if not pdf_file:
        return "Error: No file uploaded. Please upload a PDF file."

    # Validate the PDF using the file path
    valid, message = is_valid_pdf(pdf_file)
    if not valid:
        return f"Error: {message}. Please upload a valid PDF file or repair the current one."

    # API endpoint
    url = "http://209.20.158.215:7861/extract-text-eng/"

    # Prepare the payload
    with open(pdf_file, "rb") as f:
        files = {
            "file": ("uploaded.pdf", f, "application/pdf")
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
                result = response.json()
                page_content = result.get("page_content", "No description returned from API")
                return page_content
            else:
                return f"Error: {response.status_code} - {response.text}"
        except Exception as e:
            return f"Error: Failed to connect to the API - {str(e)}"

# Gradio interface
with gr.Blocks(title="PDF Content Description") as demo:
    gr.Markdown("# PDF Content Description Extractor")
    gr.Markdown(
        """
        Upload a PDF file (e.g., Dhwani-AI-Pitch-Europe.pdf) and specify a page number to extract a description of its content.
        The API will analyze the page and return a textual description, such as details about images, text, or layout.
        """
    )
    
    # Input components
    pdf_input = gr.File(label="Upload PDF File", file_types=[".pdf"], type="filepath")
    page_number_input = gr.Number(label="Page Number", value=1, precision=0, minimum=1)
    
    # Submit button
    submit_button = gr.Button("Extract Description")
    
    # Output component
    output_text = gr.Textbox(
        label="Content Description",
        lines=10,
        placeholder="The API response will appear here, describing the content of the specified PDF page."
    )
    
    # Connect the button to the function
    submit_button.click(
        fn=extract_text_from_pdf,
        inputs=[pdf_input, page_number_input],
        outputs=output_text
    )

# Launch the Gradio app
demo.launch()