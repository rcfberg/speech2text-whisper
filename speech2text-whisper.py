import whisper
import os

def transcribe_audio(audio_path, model_type='base', output_path='transcription.txt'):
    # Load the Whisper model
    model = whisper.load_model(model_type)

    # Transcribe the audio
    result = model.transcribe(audio_path)

    # Save the transcription
    with open(output_path, 'w') as file:
        file.write(result['text'])

    print(f"Transcription saved to {output_path}")

if __name__ == "__main__":
    # Prompt the user to upload an audio file
    audio_file_path = input("Please enter the path of your audio file: ")

    # Validate the audio file path
    if not os.path.exists(audio_file_path):
        print("The specified audio file does not exist.")
    else:
        # Transcribe the audio
        transcribe_audio(audio_file_path)
