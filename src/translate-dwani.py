import gradio as gr
import requests
import json

# List of supported languages
LANGUAGES = [
    "Assamese (asm_Beng)", "Kashmiri (Arabic) (kas_Arab)", "Punjabi (pan_Guru)",
    "Bengali (ben_Beng)", "Kashmiri (Devanagari) (kas_Deva)", "Sanskrit (san_Deva)",
    "Bodo (brx_Deva)", "Maithili (mai_Deva)", "Santali (sat_Olck)",
    "Dogri (doi_Deva)", "Malayalam (mal_Mlym)", "Sindhi (Arabic) (snd_Arab)",
    "English (eng_Latn)", "Marathi (mar_Deva)", "Sindhi (Devanagari) (snd_Deva)",
    "Konkani (gom_Deva)", "Manipuri (Bengali) (mni_Beng)", "Tamil (tam_Taml)",
    "Gujarati (guj_Gujr)", "Manipuri (Meitei) (mni_Mtei)", "Telugu (tel_Telu)",
    "Hindi (hin_Deva)", "Nepali (npi_Deva)", "Urdu (urd_Arab)",
    "Kannada (kan_Knda)", "Odia (ory_Orya)"
]

# Function to extract language code from selection
def get_lang_code(lang_string):
    return lang_string.split("(")[-1].rstrip(")")

def translate_api(sentences, src_lang, tgt_lang):

    import os

    # Get the base URL (IP or domain) from environment variable
    base_url = os.getenv("DWANI_AI_API_BASE_URL")

    if not base_url:
        raise ValueError("DWANI_AI_API_BASE_URL environment variable is not set")

    # Define the endpoint path
    endpoint = "/v1/translate"

        # Construct the full API URL
    url = f"{base_url.rstrip('/')}{endpoint}"


    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    
    # Convert sentences string to list if it's a string
    if isinstance(sentences, str):
        try:
            sentences_list = json.loads(sentences)
        except json.JSONDecodeError:
            sentences_list = [sentences]
    else:
        sentences_list = sentences
    
    payload = {
        "sentences": sentences_list,
        "src_lang": get_lang_code(src_lang),
        "tgt_lang": get_lang_code(tgt_lang)
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP Error: {str(e)}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request Error: {str(e)}"}

# Create Gradio interface
with gr.Blocks(title="Translation API Interface") as demo:
    gr.Markdown("# Translation API Interface")
    gr.Markdown("Enter sentences and select languages to translate.")
    
    with gr.Row():
        with gr.Column():
            # Input components
            sentences_input = gr.Textbox(
                label="Sentences",
                placeholder='Enter sentences as JSON array or single sentence (e.g., ["Hello", "Good morning"] or "Hello")',
                lines=3,
                value='["Hi"]'
            )
            src_lang_input = gr.Dropdown(
                label="Source Language",
                choices=LANGUAGES,
                value="English (eng_Latn)"
            )
            tgt_lang_input = gr.Dropdown(
                label="Target Language",
                choices=LANGUAGES,
                value="Kannada (kan_Knda)"
            )
            
            submit_btn = gr.Button("Translate")
        
        with gr.Column():
            # Output component
            output = gr.JSON(label="Translation Response")
    
    # Connect the button click to the API function
    submit_btn.click(
        fn=translate_api,
        inputs=[sentences_input, src_lang_input, tgt_lang_input],
        outputs=output
    )

# Launch the interface
if __name__ == "__main__":
    demo.launch()