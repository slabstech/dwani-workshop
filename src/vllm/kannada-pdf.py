import gradio as gr
import PyPDF2
from pdf2image import convert_from_path
import os
import tempfile

def preview_pdf(pdf_file):
    try:
        # pdf_file is a file path (string) from Gradio's File component
        if not pdf_file:
            return "Error: No file uploaded", None

        # Use the file path directly
        pdf_path = pdf_file

        # Extract basic info from the PDF
        with open(pdf_path, "rb") as file:
            pdf = PyPDF2.PdfReader(file)
            num_pages = len(pdf.pages)
            info = f"PDF Info:\n- Number of pages: {num_pages}"

        # Convert the first page to an image
        images = convert_from_path(pdf_path, first_page=1, last_page=1)
        image_path = os.path.join(tempfile.gettempdir(), "preview.png")
        images[0].save(image_path, "PNG")

        return info, image_path
    except Exception as e:
        return f"Error: {str(e)}", None

# Define the Gradio interface
interface = gr.Interface(
    fn=preview_pdf,
    inputs=gr.File(label="Upload PDF", file_types=[".pdf"]),
    outputs=[
        gr.Textbox(label="PDF Information"),
        gr.Image(label="Preview of First Page")
    ],
    title="PDF Previewer",
    description="Upload a PDF file to see its basic information and a preview of the first page."
)

# Launch the interface
interface.launch()