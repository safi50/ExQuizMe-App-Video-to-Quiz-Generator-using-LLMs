# ExQuizMe? App : Video to Text Conversion and Quiz Generation using LLMs
<img width="1672" alt="Screenshot 2024-07-22 at 9 13 22 PM" src="https://github.com/user-attachments/assets/634f3908-d040-43e5-8953-e990e9d7b53c">

## Project Demo
https://github.com/user-attachments/assets/afdf9528-f043-46d1-9d33-3d5d250b75db




## Project Overview
This project provides a Flask API for processing video files to generate text transcriptions using the Whisper model and subsequently creating quizzes with the transcriptions using Mistral-7n LLM.

In today's digital era, the abundance of educational video content presents both opportunities and challenges for learners. This AI Video Summarization and Quiz Generation Tool addresses the need for efficient educational tools by leveraging state-of-the-art Large Language Models (LLMs) to extract key concepts from educational videos, generate concise summaries, and create quizzes to reinforce learning.

The project aims to enhance the learning experience by providing a comprehensive platform that combines video summarization with interactive quiz generation, making it easier for learners to grasp and retain essential information from educational videos.


## Features

- Video content extraction and processing
- Speech-to-text conversion using **OpenAI's whisper-large-v3**
- Key concept extraction and summarization
- Quiz generation based on video content using **Mistral-7B-Instruct-v0.1** LLM
- User-friendly interface for video upload and interaction
- Cloud-based deployment on AWS EC2, Microsoft Azure

## Technologies Used

- **Speech-to-Text Model**: OpenAI Whisper ("openai/whisper-large-v3")
- **Quiz Generation Model**: Mistral AI ("mistralai/Mistral-7B-Instruct-v0.2")
- **Cloud Infrastructure**: AWS EC2, Azure Virtual Machine
- **Programming Language**: Python
- **Web Framework**: Flask (for backend API)
- **Frontend**: HTML, CSS, JavaScript

## Getting Started with ExQuizMe?

### Installing

1. **Clone the repository:**

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
Change ```domain = 'enter-your-hostname' in templates/index.html```
Use Ec2 instance public address or local host.

```
python run.py
```
This command launches the server, typically accessible at `http://127.0.0.1:5000/`.

### Notes
- Make sure `ffmpeg` is installed on your system as it's required for the audio extraction functionality.
- Adjust paths and configurations as necessary according to your setup.

### Hugging Face Login

You can use CLI as showcased in the videos or you can enter your token in the following codes in mixtral_wrapper.py.
from huggingface_hub import login
```login(token="enter-your-token")```

## Note: Virtual Machine Compute Required for Efficient Working
- VCPU's : >16
- RAM : >32Gb
- GPU Required: **Yes!!!**
- Storage Requirement: >=100Gb
