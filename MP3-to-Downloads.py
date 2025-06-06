import yt_dlp
import os

def download_youtube_mp3(video_url):
    try:
        # Target folder: your Downloads folder
        download_folder = r"C:\Users\Matta\Downloads"

        # yt_dlp options to extract audio in mp3
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'quiet': True,
            'noplaylist': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            title = info.get('title', 'audio')
            mp3_path = os.path.join(download_folder, f"{title}.mp3")

        if os.path.exists(mp3_path):
            print(f"✅ MP3 saved at: {mp3_path}")
            return mp3_path
        else:
            raise Exception("❌ MP3 file not found after processing.")

    except Exception as e:
        print(f"Error downloading MP3: {e}")
        return None


# 🔽 Example usage
if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=yqFfmwVufMo"  # Replace with your video
    download_youtube_mp3(url)
