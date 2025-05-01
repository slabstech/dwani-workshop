# dwani.ai - Your Kannada Speaking Voice Buddy

## Overview

dwani.ai is a self-hosted GenAI platform designed to provide voice mode interaction for Kannada and other Indian languages. 


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


nohup python src/server/main.py --port 7860 > server.log 2>&1 &


### dwani.ai - Voice assistant
```bash
python src/dwani-voice-assistant.py
```

[dwani.ai - voice assistant](https://huggingface.co/spaces/slabstech/text-to-speech-synthesis)



### Chat / Text Answer
```bash
python src/chat-dhwani.py
```
[Chat UX ](https://huggingface.co/spaces/slabstech/dwani-ai-chat)

### Image Query
```bash
python src/image-query.py
```
[Image Query UX ](https://huggingface.co/spaces/slabstech/dwani-ai-image-query)


### PDF Chat
```bash
python src/pdf-chat-dhwani.py
```
[PDF Chat UX ](https://huggingface.co/spaces/slabstech/dwani-ai-pdf-chat)


### Text to Speech
```bash
python src/text-to-speech-dhwani.py
```

[Text to Speech UX](https://huggingface.co/spaces/slabstech/text-to-speech-synthesis)


### Translate
```bash
python src/translate-dhwani.py
```

[Translate UX](https://huggingface.co/spaces/slabstech/dwani-ai-translate)

### Speech to Text / ASR
```bash
python src/transcribe-dhwani.py
```

[ASR/ Speech to Text UX](https://huggingface.co/spaces/slabstech/asr-transcription)

### Text to Speech
```bash
python src/text-to-speech-dhwani.py
```

[Text to Speech UX](https://huggingface.co/spaces/slabstech/text-to-speech-synthesis)



## Video Tutorials


- Dhwani - How to use - Dhwani AI - Workshop:  20th March, 2025
[![Watch the video](https://img.youtube.com/vi/RLIhG1bt8gw/hqdefault.jpg)](https://youtu.be/f5JkJLQJFGA)


- Dhwani - Intoduction to Project
[![Watch the video](https://img.youtube.com/vi/kqZZZjbeNVk/hqdefault.jpg)](https://youtu.be/kqZZZjbeNVk)


## Models and Tools

The project utilizes the following open-source tools:

| Open-Source Tool                       | Source Repository                                          | 
|---------------------------------------|-------------------------------------------------------------|
| Automatic Speech Recognition : ASR   | [ASR Indic Server](https://github.com/slabstech/asr-indic-server) | 
| Text to Speech : TTS                  | [TTS Indic Server](https://github.com/slabstech/tts-indic-server)  | 
| Translation                           | [Indic Translate Server](https://github.com/slabstech/indic-translate-server) | 
| Document Parser                       | [Indic Document Server](https://github.com/slabstech/docs-indic-server) |
| Dhwani Server | [Dhwani Server](https://github.com/slabstech/dhwani-server) | 
| Dhwani Android | [Android](https://github.com/slabstech/dhwani-android) |
| Large Language Model                  | [LLM Indic Server](https://github.com/slabstech/llm-indic-server_cpu) | 


## Architecture

| Answer Engine| Answer Engine with Translation                                 | Voice Translation                          |
|----------|-----------------------------------------------|---------------------------------------------|
| ![Answer Engine](docs/kannada-answer-engine.drawio.png "Engine") | ![Answer Engine Translation](docs/kannada-answer-engine-translate.png "Engine") | ![Voice Translation](docs/voice-translation.drawio.png "Voice Translation") |

