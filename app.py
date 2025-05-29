from flask import Flask, request, jsonify
from faster_whisper import WhisperModel
import tempfile
import subprocess
import requests
import os
from datetime import datetime
from utils.gemini_prompt import analyze_accent
import yt_dlp
import tempfile
import os
app = Flask(__name__)

# Load Faster-Whisper model (CPU or GPU)
model = WhisperModel("base", device="cpu")

# Log file path
LOG_FILE = "logs/accent_results.txt"



def download_video(url):
    try:
        # Use system temp folder for downloads
        download_folder = tempfile.gettempdir()
        
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': os.path.join(download_folder, 'downloaded_video.%(ext)s'),
            'quiet': True,
            'no_warnings': True,
            # Uncomment below to enable debug logs if needed
            # 'verbose': True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            video_path = ydl.prepare_filename(info)
        
        if not os.path.exists(video_path):
            raise Exception("Video download failed: file not found after download.")
        
        return video_path
    
    except Exception as e:
        raise Exception(f"Failed to download video: {e}")
# def download_video(url):
#     try:
#         response = requests.get(url, stream=True)
#         if response.status_code != 200:
#             raise Exception(f"Download failed: {response.status_code}")

#         tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
#         for chunk in response.iter_content(chunk_size=8192):
#             tmp_file.write(chunk)
#         tmp_file.close()
#         return tmp_file.name
#     except Exception as e:
#         raise Exception(f"Failed to download video: {e}")

# def extract_audio(video_path):
#     audio_path = video_path.replace(".mp4", ".wav")
#     command = [
#         "ffmpeg", "-y", "-i", video_path,
#         "-ar", "16000", "-ac", "1", "-f", "wav", audio_path
#     ]
#     subprocess.run(command, check=True)
#     return audio_path
def extract_audio(video_path):
    base, _ = os.path.splitext(video_path)
    audio_path = base + ".wav"

    command = [
        "ffmpeg", "-y", "-i", video_path,
        "-ar", "16000", "-ac", "1", "-f", "wav", audio_path
    ]

    subprocess.run(command, check=True)
    return audio_path

def transcribe_audio(audio_path):
    segments, _ = model.transcribe(audio_path)
    transcript = " ".join([segment.text for segment in segments])
    return transcript

def log_result(video_url, transcript, result):
    # Make sure the logs folder exists
    os.makedirs("logs", exist_ok=True)

    # Create a unique filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = f"logs/accent_result_{timestamp}.txt"

    # Write data into the new file
    with open(log_file, "w", encoding="utf-8") as f:
        f.write(f"--- Analysis @ {datetime.now()} ---\n")
        f.write(f"Video URL: {video_url}\n")
        f.write(f"Accent: {result['accent']} (Confidence: {result['confidence']}%)\n")
        f.write(f"Summary: {result['summary']}\n")
        f.write("Transcript:\n")
        f.write(transcript + "\n")
        f.write("Gemini Response:\n")
        f.write(str(result) + "\n")
        f.write("--- End of Entry ---\n")

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json()
        video_url = data.get("video_url")

        if not video_url:
            return jsonify({"error": "Missing video_url"}), 400

        # Step 1: Download
        video_path = download_video(video_url)

        # Step 2: Extract audio
        audio_path = extract_audio(video_path)

        # Step 3: Transcribe
        transcript = transcribe_audio(audio_path)

        # Step 4: Analyze accent with Gemini
        result = analyze_accent(transcript)

        # Step 5: Log transcript and AI response
        log_result(video_url, transcript, result)

        # Clean up
        os.remove(video_path)
        os.remove(audio_path)

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
