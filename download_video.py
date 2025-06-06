import yt_dlp
import os
import tempfile

def download_video(url):
    try:
        # Set download folder
        download_folder = tempfile.gettempdir()

        # yt_dlp options
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': os.path.join(download_folder, 'downloaded_video.%(ext)s'),
            'quiet': False,
            'noplaylist': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            video_path = ydl.prepare_filename(info)

        if not os.path.exists(video_path):
            raise Exception("Download failed: File not found.")

        print(f"✅ Download complete: {video_path}")
        return video_path

    except Exception as e:
        print(f"❌ Error: {e}")

# ----------------------
# 👉 Set your video URL here
video_url = "https://www.youtube.com/watch?v=yqFfmwVufMo"  # replace this with your real URL

# Download video
download_video(video_url)
