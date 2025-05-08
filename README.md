# dwani.ai - Your Kannada Speaking Voice Buddy

## Overview

dwani.ai is a self-hosted GenAI platform designed to provide voice mode interaction for Kannada and other Indian languages. 

[dwani.ai - Workshop Slides](https://tinyurl.com/dwani-ai-workshop)

## Workshop steps

### For Development 
- **Prerequisites**: Python 3.10
- **Steps**:
  1. **Create a virtual environment**:
  ```bash
  python -m venv venv
  ```
  2. **Activate the virtual environment**:
  ```bash
  source venv/bin/activate
  ```
  On Windows, use:
  ```bash
  venv\Scripts\activate
  ```
  3. **Install dependencies**:
  - ```bash
    pip install -r requirements.txt
    ```

- To Run the program
  - DWANI_AI_API_BASE_URL environement variable has to be set
    - export DWANI_AI_API_BASE_URL=http://example.com:example-port
  - Please email us to get the IP for dwani.ai - workshop inference server


# dwani.ai Features and Commands

| Feature                  | Command                                      | Web UX Link                                                                 | Server  |
|--------------------------|----------------------------------------------|----------------------------------------------|-----------------------------------------------------------------------------|
| Voice Assistant          | `python src/dwani-voice-assistant.py`        | [Voice Assistant](https://huggingface.co/spaces/slabstech/dwani-voice-assistant) | [https://github.com/slabstech/dwani-server](https://github.com/slabstech/dwani-server)|
| Chat / Text Answer       | `python src/chat-dwani.py`                  | [Chat UX](https://huggingface.co/spaces/slabstech/dwani-ai-chat)            |[https://github.com/slabstech/llm-indic-server](https://github.com/slabstech/llm-indic-server)|
| Image Query              | `python src/image-query.py`                  | [Image Query UX](https://huggingface.co/spaces/slabstech/dwani-ai-image-query) | [https://github.com/slabstech/llm-indic-server](https://github.com/slabstech/llm-indic-server)|
| PDF Chat                 | `python src/pdf-chat-dwani.py`              | [PDF Chat UX](https://huggingface.co/spaces/slabstech/dwani-ai-pdf-chat)    |[https://github.com/slabstech/docs-indic-server](https://github.com/slabstech/docs-indic-server)|
| Kannada -  PDF Extraction,Translation and Creation | `python src/vllm/kannada-pdf.py`              | [kannada PDF ](https://huggingface.co/spaces/slabstech/kannada-pdf-prompt)    |[https://github.com/slabstech/docs-indic-server](https://github.com/slabstech/docs-indic-server)|
| Text to Speech           | `python src/text-to-speech-dwani.py`        | [Text to Speech UX](https://huggingface.co/spaces/slabstech/text-to-speech-synthesis) | [https://github.com/slabstech/tts-indic-server](https://github.com/slabstech/tts-indic-server)|
| Translate                | `python src/translate-dwani.py`             | [Translate UX](https://huggingface.co/spaces/slabstech/dwani-ai-translate)  |[https://github.com/slabstech/indic-translate-server](https://github.com/slabstech/indic-translate-server)|
| Speech to Text / ASR     | `python src/transcribe-dwani.py`            | [ASR/ Speech to Text UX](https://huggingface.co/spaces/slabstech/asr-transcription) |[https://github.com/slabstech/asr-indic-server](https://github.com/slabstech/asr-indic-server)|



## Video Tutorials


- dwani - How to use - dwani AI - Workshop:  20th March, 2025
[![Watch the video](https://img.youtube.com/vi/RLIhG1bt8gw/hqdefault.jpg)](https://youtu.be/f5JkJLQJFGA)


- dwani - Intoduction to Project
[![Watch the video](https://img.youtube.com/vi/kqZZZjbeNVk/hqdefault.jpg)](https://youtu.be/kqZZZjbeNVk)


## Models and Tools

The project utilizes the following open-source tools:

| Open-Source Tool                       | Source Repository                                          | 
|---------------------------------------|-------------------------------------------------------------|
| Automatic Speech Recognition : ASR   | [ASR Indic Server](https://github.com/slabstech/asr-indic-server) | 
| Text to Speech : TTS                  | [TTS Indic Server](https://github.com/slabstech/tts-indic-server)  | 
| Translation                           | [Indic Translate Server](https://github.com/slabstech/indic-translate-server) | 
| Document Parser                       | [Indic Document Server](https://github.com/slabstech/docs-indic-server) |
| dwani Server | [dwani Server](https://github.com/slabstech/dwani-server) | 
| dwani Android | [Android](https://github.com/slabstech/dwani-android) |
| Large Language Model                  | [LLM Indic Server](https://github.com/slabstech/llm-indic-server_cpu) | 


## Architecture

| Answer Engine| Answer Engine with Translation                                 | Voice Translation                          |
|----------|-----------------------------------------------|---------------------------------------------|
| ![Answer Engine](docs/kannada-answer-engine.drawio.png "Engine") | ![Answer Engine Translation](docs/kannada-answer-engine-translate.png "Engine") | ![Voice Translation](docs/voice-translation.drawio.png "Voice Translation") |

<!-- 

nohup python src/server/main.py --port 7860 > server.log 2>&1 &

-->