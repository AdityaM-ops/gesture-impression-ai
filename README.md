
# Gesture Impression AI

AI-powered hand gesture interpretation using MediaPipe, OpenCV, and LLaMA3 via Ollama.

## Features

- Real-time hand gesture detection using webcam
- Basic gesture recognition (e.g., thumbs up, victory)
- Natural language interpretation using local LLMs (LLaMA3 + Ollama)
- Streamlit interface for interactive use

## Setup Instructions (For ZIP Download Users)

1. **Download the ZIP**

   Click the green `Code` button on GitHub and choose **Download ZIP**.

2. **Extract the ZIP**

   Extract the contents to any folder on your computer.

3. **Open in VS Code**

   Open the extracted folder using Visual Studio Code.

4. **Create a Virtual Environment**

   Open a terminal in VS Code and run:

   ```bash
   python -m venv venv

5. **Open a terminal in VS Code and activate the virtual environment**:

   .\venv\Scripts\activate

6. **Install all required dependencies by running:**

   pip install -r requirements.txt

7. **Start Ollama in a separate terminal:**

   ollama serve

   Then pull the required LLM model:

   ollama pull llama3

8. **Run the app using Streamlit:**

   streamlit run app.py

