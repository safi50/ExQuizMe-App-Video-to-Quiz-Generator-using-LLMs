import subprocess
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import torch

class WhisperWrapper:
    def __init__(self, model_id="openai/whisper-large-v3", gpu_index=1, use_cuda=True):
        """
        Initializes the model pipeline for further usage.
        """
        self.device = torch.device("cuda" if torch.cuda.is_available() and use_cuda else "cpu")
        self.model_id = model_id

        model = AutoModelForSpeechSeq2Seq.from_pretrained(
            model_id,
            low_cpu_mem_usage=True,
            use_safetensors=True
        ).to(self.device)

        self.processor = AutoProcessor.from_pretrained(model_id)

        self.pipe = pipeline(
            "automatic-speech-recognition",
            model=model,
            tokenizer=self.processor.tokenizer,
            feature_extractor=self.processor.feature_extractor,
            device=self.device.index if torch.cuda.is_available() and use_cuda else -1
        )

    def transcribe(self, audio_path):
        # The pipeline should handle the necessary input preprocessing
        result = self.pipe(audio_path)
        return result["text"]

    def extract_audio_from_video(self, video_path, audio_output_path="temp_audio.wav"):
        """
        Extracts audio from video using ffmpeg and saves it to audio_output_path.
        Returns the path to the extracted audio file.
        """
        command = f"ffmpeg -i {video_path} -ab 160k -ac 2 -ar 44100 -vn {audio_output_path}"
        subprocess.run(command, shell=True, check=True)
        return audio_output_path
