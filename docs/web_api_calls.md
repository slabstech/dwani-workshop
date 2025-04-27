Text Chat

- English to English

curl -X 'POST' \
  'https://slabstech-dhwani-server-workshop.hf.space/v1/chat' \
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
  'https://slabstech-dhwani-server-workshop.hf.space/v1/chat' \
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
  'https://slabstech-dhwani-server-workshop.hf.space/v1/chat' \
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
  'https://slabstech-dhwani-server-workshop.hf.space/v1/chat' \
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
  'https://slabstech-dhwani-server-workshop.hf.space/v1/transcribe/?language=kannada' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@kannada_sample_1.wav;type=audio/x-wav'

  {
  "text": "ಕರ್ನಾಟಕ ದ ರಾಜಧಾನಿ ಯಾವುದು"
}



- Speech to Speech

curl -X 'POST' \
  'https://slabstech-dhwani-server-workshop.hf.space/v1/speech_to_speech?language=kannada' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@kannada_sample_1.wav;type=audio/x-wav' -o speech_speech_output.wav



- Speech Synthesis

curl -X 'POST' \
  'http://209.20.158.215:7862/v1/audio/speech' \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "ಕರ್ನಾಟಕದ ರಾಜಧಾನಿ ಬೆಂಗಳೂರು. "
}'

