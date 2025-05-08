Text Chat

- English to English

curl -X 'POST' \
  'https://dwani-dwani-server-workshop.hf.space/v1/chat' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "prompt": "hi",
  "src_lang": "eng_Latn",
  "tgt_lang": "eng_Latn"
}'

{
  "response": "Hello! How can I help you with questions about India, specifically Karnataka?"
}


- Kannada to Kannada

curl -X 'POST' \
  'https://dwani-dwani-server-workshop.hf.space/v1/chat' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "prompt": "ಕರ್ನಾಟಕದ ರಾಜಧಾನಿ ಯಾವುದು",
  "src_lang": "kan_Knda",
  "tgt_lang": "kan_Knda"
}'

{
  "response": "ಕರ್ನಾಟಕದ ರಾಜಧಾನಿ ಬೆಂಗಳೂರು. "
}

Kannada to English

curl -X 'POST' \
  'https://dwani-dwani-server-workshop.hf.space/v1/chat' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "prompt": "ಕರ್ನಾಟಕದ ರಾಜಧಾನಿ ಯಾವುದು",
  "src_lang": "kan_Knda",
  "tgt_lang": "eng_Latn"
}'

{
  "response": "The capital of Karnataka is Bengaluru."
}


English to Kannada

curl -X 'POST' \
  'https://dwani-dwani-server-workshop.hf.space/v1/chat' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "prompt": "what is the capital of Karnataka ?",
  "src_lang": "eng_Latn",
  "tgt_lang": "kan_Knda"
}'


{
  "response": "ಕರ್ನಾಟಕದ ರಾಜಧಾನಿ ಬೆಂಗಳೂರು. "
}



-- Transcribe  / Automatic Speech Recognition
curl -X 'POST' \
  'https://dwani-dwani-server-workshop.hf.space/v1/transcribe/?language=kannada' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@kannada_sample_1.wav;type=audio/x-wav'

  {
  "text": "ಕರ್ನಾಟಕ ದ ರಾಜಧಾನಿ ಯಾವುದು"
}



- Speech to Speech

curl -X 'POST' \
  'https://dwani-dwani-server-workshop.hf.space/v1/speech_to_speech?language=kannada' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@kannada_sample_1.wav;type=audio/x-wav' -o speech_speech_output.wav



- Speech Synthesis


curl -X 'POST' \
  'https://dwani-dwani-server-workshop.hf.space/v1/audio/speech' \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "ಕರ್ನಾಟಕದ ರಾಜಧಾನಿ ಬೆಂಗಳೂರು. "
}'


Visual Query

curl -X 'POST' \
  'https://dwani-dwani-server-workshop.hf.space/v1/visual_query?src_lang=eng_Latn&tgt_lang=kan_Knda' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'query=describe the image' \
  -F 'file=@Screenshot from 2025-04-26 21-41-12.png;type=image/png'


{
  "answer": "ಚಿತ್ರದ ವಿವರಣೆ ಹೀಗಿದೆಃ ಈ ಚಿತ್ರವು ಕಂದುಬಣ್ಣದ ಮತ್ತು ಬಿಳಿ ಕೋಟ್ ಹೊಂದಿರುವ ಸಂತೋಷದ, ಮಧ್ಯಮ ಗಾತ್ರದ ನಾಯಿಯ ಡಿಜಿಟಲ್ ವರ್ಣಚಿತ್ರವಾಗಿದೆ, ಕಾಲರ್ ಧರಿಸಿ, ಮೋಡ ಕವಿದ ಆಕಾಶದ ಕೆಳಗೆ ಹುಲ್ಲುಗಾವಲು ಮೈದಾನದಲ್ಲಿ ನಿಂತಿದೆ. "
}



--  PDF Query

curl -X 'POST' \
  'http://209.20.158.215:7861/extract-text-eng/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@ITA-software-travel-complexity.pdf;type=application/pdf' \
  -F 'page_number=1' \
  -F 'src_lang=eng_Latn' \
  -F 'tgt_lang=eng_Latn' \
  -F 'prompt=describe the image'


  {
  "page_content": "Here's a description of the image:\n\nThe image is a slide titled \"Computational Complexity of Air Travel Planning\" presented by Carl de Marcken from ITA Software. The slide explains that the document is a set of annotated slides aimed at providing an undergraduate computer science background on the complexity of air travel planning and is powered by ITA Software, which creates search and optimization software for the travel industry."
}