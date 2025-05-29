🎙️ Accent Detector – Setup Instructions (Complete)
1. 📦 Clone the Repository
bash


git clone https://github.com/your-username/accent-detector.git
cd accent-detector
2. 🐍 Create a Virtual Environment
bash


python -m venv venv
3. ▶️ Activate the Environment
For Windows CMD:

cmd


venv\Scripts\activate
For Windows PowerShell:

powershell


.\venv\Scripts\Activate.ps1
For macOS/Linux:

bash


source venv/bin/activate
4. 📥 Install Python Dependencies
bash


pip install -r requirements.txt
5. 🔐 Add Your Gemini API Key
Create a .env file inside the utils/ folder:

ini


GOOGLE_API_KEY=your_google_gemini_api_key_here
6. 🎧 Install and Configure FFmpeg
Download from:
https://www.gyan.dev/ffmpeg/builds/

Extract the zip, and  the path to the bin/ folder (e.g., C:\ffmpeg\bin).

Add FFmpeg to your system PATH:

On Windows:

Search for “Environment Variables”

 the Path variable

Add: C:\ffmpeg\bin

On macOS/Linux:

Add this to ~/.bashrc or ~/.zshrc:

bash


export PATH="$PATH:/path/to/ffmpeg/bin"
Test in terminal:

bash


ffmpeg -version
✅ If you see version output, FFmpeg is correctly installed.

7. 🚀 Run the Flask App
bash


python app.py
The app will start at:
http://127.0.0.1:5000

8. 🧪 Test the API (e.g. in Postman or curl)
POST to:

arduino


http://127.0.0.1:5000/analyze
Request Body:

json


{
  "video_url": "https://somevideo.com/video.mp4"
}

Setup Instructions
Clone the repository:

.\venv\Scripts\Activate.ps1
python app.py 

git clone https://github.com/your-username/accent-detector.git
cd accent-detector
Create and activate a Python virtual environment:

On Linux/macOS:



python3 -m venv venv
source venv/bin/activate
On Windows (PowerShell):

powershell

python -m venv venv
.\venv\Scripts\Activate.ps1
Install required Python packages:



pip install -r requirements.txt
Set up your environment variables:

Create a .env file in the utils folder with your Google API key:

ini

GOOGLE_API_KEY=your_google_gemini_api_key_here
Make sure ffmpeg is installed and available in your system PATH.

You can download ffmpeg from https://www.gyan.dev/ffmpeg/builds/

Test by running ffmpeg -version in your terminal.

Running the API
Start the Flask server:



python app.py
By default, it runs on http://127.0.0.1:5000

How to Use
Send a POST request to /analyze with JSON body containing the key "video_url" and a valid video URL as value.

Example using Postman
URL: http://127.0.0.1:5000/analyze

Method: POST

Headers:
Content-Type: application/json

Body (raw JSON):

json

{
  "video_url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"
}
Expected Response
A JSON object with:

accent: Detected English accent (e.g., "American", "British", etc.)

confidence: Confidence score (0-100)

summary: One sentence explanation of the classification

Example:

json

{
  "accent": "American",
  "confidence": 75,
  "summary": "The accent resembles American English based on pronunciation patterns in the transcript."
}
Logs
Transcripts and Gemini responses are saved to logs/accent_results.txt

Raw Gemini responses are saved to logs/gemini_responses.txt

Notes
The API supports any video URL that yt-dlp can download (YouTube, Streamable, direct MP4 links, etc.).

Ensure your Google Gemini API key is valid and has proper access.

For best performance, you may want to run on a machine with a GPU.



Supported Video URL Types
YouTube Standard videos (https://www.youtube.com/watch?v=...)
Streamable
Short video hosting platform links (https://streamable.com/abc123)
imeo
Vimeo video URLs (https://vimeo.com/12345678)
Direct MP4 or other video file links
Any direct HTTP(S) link to a video file on a server (e.g., .mp4, .webm, .mkv)
Examples: https://example.com/videos/sample-video.mp4
Facebook Videos
Public Facebook video URLs
6. Twitter Videos
Twitter video tweets URLs
7. Dailymotion
URLs from Dailymotion platform
8. TikTok
TikTok video URLs (subject to region and platform changes)
9. Twitch Clips and Videos
10. Other supported platforms (partial list)
SoundCloud (for audio)
Instagram (videos/stories)
Bilibili
Rumble
PeerTube
And many more 