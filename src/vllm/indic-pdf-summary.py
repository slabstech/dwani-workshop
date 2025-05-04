import gradio as gr
import requests
import os

# Get the base URL (IP or domain) from environment variable
base_url = os.getenv("DWANI_AI_API_BASE_URL")

# Translation API endpoint
translation_api_url = "https://slabstech-dhwani-server-workshop.hf.space/v1/translate"

def summarize_pdf(pdf_file, page_number, src_lang, tgt_lang):
    """Summarize a PDF page and translate the summary."""
    if not pdf_file:
        return "Please upload a PDF file."
    if not page_number or page_number < 1:
        return "Please enter a valid page number."

    endpoint = "/summarize-pdf"

    # Construct the full API URL
    url = f"{base_url.rstrip('/')}{endpoint}"

    headers = {
        "accept": "application/json"
    }

    try:
        # Prepare the multipart form data
        files = {
            "file": (pdf_file.name, open(pdf_file.name, "rb"), "application/pdf")
        }
        data = {
            "page_number": str(page_number)
        }

        # Send POST request to summarize PDF
        response = requests.post(url, headers=headers, files=files, data=data)

        # Check if request was successful
        if response.status_code == 200:
            result = response.json()
            summary_response = {
                "Original Text": result.get("original_text", "N/A"),
                "Summary": result.get("summary", "N/A"),
                "Processed Page": result.get("processed_page", "N/A")
            }

            # Translate the summary
            translation_payload = {
                "sentences": [summary_response["Summary"]],
                "src_lang": src_lang,
                "tgt_lang": tgt_lang
            }
            translation_response = requests.post(
                translation_api_url,
                json=translation_payload,
                headers={"accept": "application/json", "Content-Type": "application/json"}
            )
            translation_response.raise_for_status()
            translation_result = translation_response.json()
            translated_summary = translation_result["translations"][0]

            # Add translated summary to the response
            summary_response["Translated Summary"] = translated_summary

            return summary_response
        else:
            return f"Error: {response.status_code} - {response.text}"

    except requests.exceptions.RequestException as e:
        return f"Error querying summarize API or translation API: {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        # Ensure the file is closed if it was opened
        if 'files' in locals() and files['file'][1]:
            files['file'][1].close()

# Define language options (based on the provided example and common use cases)
language_options = [
    "kan_Knda",  # Kannada
    "eng_Latn",  # English
    "hin_Deva",  # Hindi
    "tam_Taml",  # Tamil
    "tel_Telu",  # Telugu
]

# Define Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# PDF Summarizer with Translation")
    gr.Markdown("Upload a PDF, specify a page number, and select source and target languages to summarize and translate the content.")

    with gr.Row():
        with gr.Column():
            pdf_input = gr.File(label="Upload PDF", file_types=[".pdf"])
            page_number = gr.Number(label="Page Number", value=1, minimum=1, precision=0)
            src_lang_input = gr.Dropdown(
                choices=language_options,
                label="Source Language",
                value="eng_Latn"  # Default to English
            )
            tgt_lang_input = gr.Dropdown(
                choices=language_options,
                label="Target Language",
                value="kan_Knda"  # Default to Kannada
            )
            submit_btn = gr.Button("Summarize and Translate")

    output = gr.JSON(label="Response")

    submit_btn.click(
        fn=summarize_pdf,
        inputs=[pdf_input, page_number, src_lang_input, tgt_lang_input],
        outputs=output
    )

# Launch the interface
demo.launch()