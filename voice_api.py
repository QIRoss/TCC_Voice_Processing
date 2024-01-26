from flask import Flask, request, jsonify
from sr_google_api import audio_to_text
# from sr_pocketsphinx import audio_to_text
# from torch_librosa_example import audio_to_text

voice_api = Flask(__name__)

@voice_api.route('/transcribe', methods=['POST'])
def transcribe_wav():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and file.filename.endswith('.wav'):
        try:
            text = audio_to_text(file)
            return jsonify({'text': text}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Invalid file format, must be .wav'}), 400

if __name__ == '__main__':
    voice_api.run(debug=True)