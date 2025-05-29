# 🎙️ Accent Detector – Setup Instructions (Complete)

A Flask API that:
- 🔊 Accepts a video URL (YouTube, MP4, etc.)
- 📝 Transcribes audio using Faster-Whisper
- 🧠 Analyzes the English accent using Google Gemini API

---

## 1. 📦 Clone the Repository

```bash
git clone https://github.com/your-username/accent-detector.git
cd accent-detector
docker-compose up --build
Then go to:
👉 http://localhost:5000
add your env data
```

---

## 2. 🐍 Create a Virtual Environment

```bash
python -m venv venv
```

---

## 3. ▶️ Activate the Environment

### For Windows CMD:
```cmd
venv\Scripts\activate
```

### For Windows PowerShell:
```powershell
.\venv\Scripts\Activate.ps1
```

### For macOS/Linux:
```bash
source venv/bin/activate
```

---

## 4. 📥 Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. 🔐 Add Your API Keys

Create a `.env` file inside the `utils/` folder with the following content:

```ini
# 🔑 Gemini API (Required)
GOOGLE_API_KEY=your_google_gemini_api_key_here

# 🧠 LangChain (Optional if used with Gemini/OpenAI)
LANGCHAIN_API_KEY=your_langchain_api_key_here
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=accent-detector

# 🤖 OpenAI (Optional fallback if you're using OpenAI models)
OPENAI_API_KEY=your_openai_api_key_here

```

---

## 6. 🎧 Install and Configure FFmpeg

### 📦 Download:
[https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)

### 🗂️ Extract and set path to `bin/` (e.g. `C:\ffmpeg\bin`)

---

### 🪟 On Windows:
1. Open **System Environment Variables**
2. Edit `Path`
3. Add: `C:\ffmpeg\bin`

---

### 🍎 On macOS/Linux:
Add to your shell profile (`~/.bashrc`, `~/.zshrc`):

```bash
export PATH="$PATH:/path/to/ffmpeg/bin"
```

### ✅ Test:
```bash
ffmpeg -version
```
If you see version output, FFmpeg is installed correctly.

---

## 7. 🚀 Run the Flask App

```bash
python app.py
```

By default, the server will be live at:  
👉 `http://127.0.0.1:5000`

---

## 8. 🧪 Test the API (Postman / curl)

**Endpoint:**
```
POST http://127.0.0.1:5000/analyze
```

### ✅ Request Body:
```json
{
  "video_url": "https://somevideo.com/video.mp4"
}
```

---

## 🧪 Example using Postman

- **URL:** `http://127.0.0.1:5000/analyze`
- **Method:** `POST`
- **Headers:**
  ```http
  Content-Type: application/json
  ```
- **Body (raw JSON):**
  ```json
  {
    "video_url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"
  }
  ```

---

## 📤 Expected Response

```json
{
  "accent": "American",
  "confidence": 75,
  "summary": "The accent resembles American English based on pronunciation patterns in the transcript."
}
```

---

## 🗂️ Logs

- Transcripts & Gemini output: `logs/accent_results.txt`
- Raw Gemini responses: `logs/gemini_responses.txt`

---

## 📝 Notes

- ✅ Supports any video URL `yt-dlp` can handle
- 🔐 Ensure your Gemini API key is valid and active
- ⚙️ Optional: Use a GPU machine for better performance

---

## 🌐 Supported Video URL Types

```
╭────────────────────────────────────────────╮
│ ✅ YouTube Standard videos                │
│ ✅ YouTube Shorts                         │
│ ✅ Streamable (https://streamable.com/abc)│
│ ✅ Vimeo (https://vimeo.com/12345678)     │
│ ✅ Direct MP4/WEBM/MKV URLs               │
│ ✅ Facebook (Public video links)          │
│ ✅ Twitter (Video tweet URLs)             │
│ ✅ Dailymotion                             │
│ ✅ TikTok (Region-dependent)              │
│ ✅ Twitch (Clips & Full videos)           │
│ ✅ SoundCloud (Audio files)               │
│ ✅ Instagram (Stories/Videos)             │
│ ✅ Bilibili, Rumble, PeerTube, etc.       │
╰────────────────────────────────────────────╯
```

---


## ✅ Test the Accent Detector API via Postman
**You can test the API using Postman through the following public ngrok URL: **

🔗 POST https://444c-185-84-106-206.ngrok-free.app/analyze

**🔸 Headers:**
           Content-Type: application/json

🔸 Body (raw JSON):

{
  "video_url": "https://streamable.com/kzb6ki"
}
🔸 Example Response:
{
  "accent": "American",
  "confidence": 85,
  "summary": "The speaker uses common American English pronunciations and colloquialisms, suggesting an American accent with a high degree of likelihood."
}

**🔔 Note: This link only works when I have ngrok running, so feel free to notify me before testing.
Alternatively, you can run the project locally by following the setup steps in the README.

Let me know if you'd like help running it on your machine 🚀**

