# Flask API for Video-to-Text Translation and Quiz Generation

This project provides a Flask API for processing video files to generate text transcriptions using the Whisper model and subsequently creating quizzes with the transcriptions.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6 or higher
- ffmpeg (for audio extraction from video)

### Installing

1. **Clone the repository:**

```
git clone <repository-url>
```

Replace `<repository-url>` with the actual URL of the GitHub repository.

2. **Create and activate a virtual environment:**

- Navigate to the project directory:
  ```
  cd path/to/project
  ```
- Create a virtual environment:
  ```
  python -m venv venv
  ```
- Activate the virtual environment:
  - On Windows:
    ```
    .\venv\Scripts\activate
    ```
  - On macOS/Linux:
    ```
    source venv/bin/activate
    ```

3. **Install dependencies:**

With the virtual environment activated, install the requirements using:

```
pip install -r requirements.txt
```

### Running the Project

To start the Flask server, run:

Change '''domain = 'enter-your-hostname' in templates/index.html'''

Use Ec2 instance public address or local host.

```
python run.py
```

This command launches the server, typically accessible at `http://127.0.0.1:5000/`.

### Testing the API

To test the API's functionality, you can use tools like `curl`, Postman, or any HTTP client.

#### Testing Video-to-Text Translation

- **Using `curl`:**

```
curl -X POST -F "video=@path/to/your/video.mp4" http://127.0.0.1:5000/transcribe_video
```

Replace `path/to/your/video.mp4` with the actual path to a video file.

- **Using Postman:**
- Method: `POST`
- URL: `http://127.0.0.1:5000/transcribe_video`
- Body type: `form-data`
- Key: `video` (type: File), select the video file to upload
- Hit `Send` and check the response.


#### Testing Quiz Generation

- **Using `curl`:**
```
curl -X POST -H "Content-Type: application/json" \
    -d '{"content":"Lorem Ipsum", "complexity": "advanced", "q_type": "quiz"}' \
    http://127.0.0.1:5000/generate_quiz
```
Replace "Lorem Ipsum" with actual transcription of a video.

### Notes

- Make sure `ffmpeg` is installed on your system as it's required for the audio extraction functionality.
- Adjust paths and configurations as necessary according to your setup.


### Hugging Face Login

You can use CLI as showcased in the videos or you can enter your token in the following codes in mixtral_wrapper.py.

from huggingface_hub import login
login(token="enter-your-token")