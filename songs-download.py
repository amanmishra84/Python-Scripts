import os
import shutil
import yt_dlp

# Define the destination directory (USB Drive Path)
USB_DRIVE = r"E:\my music"  # Ensure this path is correct for your system

# Ensure directory exists
if not os.path.exists(USB_DRIVE):
    os.makedirs(USB_DRIVE)

# Bollywood hit songs (1960-1990) - Replace these with actual working URLs
song_urls = [
    "https://www.youtube.com/watch?v=58xP3i4N2Ec",
    "https://www.youtube.com/watch?v=A7WWnTR5arQ",
    "https://www.youtube.com/watch?v=7ah9PjFqzgk",
    "https://www.youtube.com/watch?v=o4ZZ1rntVUI",
    "https://www.youtube.com/watch?v=H6RymEGHGjE",
    "https://www.youtube.com/watch?v=2iUuiHhskOE"

]

# yt-dlp options for audio download
options = {
    "format": "bestaudio/best",
    "outtmpl": os.path.join(USB_DRIVE, "%(title)s.%(ext)s"),
    "ffmpeg_location": r"D:\ffmpeg\bin",  # Specify the correct FFmpeg path
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "128",
        }
    ],
}

# Function to check available storage
def get_available_space(path):
    """Returns available space (in bytes) for the given path."""
    total, used, free = shutil.disk_usage(path)
    return free  # Free space in bytes

# Approximate file size assumption per song (in bytes)
AVG_SONG_SIZE_MB = 5  # Assume each song is ~5MB
AVG_SONG_SIZE_BYTES = AVG_SONG_SIZE_MB * 1024 * 1024  # Convert MB to bytes

# Initialize downloader
ydl = yt_dlp.YoutubeDL(options)

# Download songs one by one with storage check
for song_url in song_urls:
    available_space = get_available_space(USB_DRIVE)

    # Check if there's enough space for the next song
    if available_space < AVG_SONG_SIZE_BYTES:
        print(f"⚠️ Not enough storage space for {song_url}. Download stopped.")
        break  # Stop downloading further songs

    print(f"⬇️ Downloading: {song_url}")
    ydl.download([song_url])  # Download only this song

print("✅ Download process completed.")
