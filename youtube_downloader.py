import os
import yt_dlp

# ------  USER SE URL INPUT LENA >>>>>

url = input("Enter your url: ")

# -------DOWNLAOD LOCATION PATH SET KARNA >>>>>

path = input("Enter download path (leave blank for current directory)").strip()

if not path:
    path = "."

# ------- DOWNLOAD OPTIONS SET KARNA >>>>>

print("\nSelect download Quality/Type:")
print("1. Best Quality(videeo+audio)")
print("2. 1080p Video Only")
print("3. 720p Video Only")
print("4. 480p Video Only")
print("5. only audio (mp3)")

choice = input("Enter your choice (1-5): ").strip()

# ------- format aur quality ke hisaab se options set karna >>>>>

if choice == "2":
    format_option = "bestvideo[height<=1080]+bestaudio/best[height<=1080]"
elif choice == "3":
    format_option = "bestvideo[height<=720]+bestaudio/best[height<=720]"
elif choice == "4":
    format_option = "bestvideo[height<=480]+bestaudio/best[height<=480]"
elif choice == "5":
    format_option = "bestaudio/best"
else:
    format_option = "bv*+ba/b"

#------- yt_dlp options set karna DICTIONARY BANANA >>>>>
ydl_opts = {
    'format': format_option,
    'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
}

# ------ AGAR USER NE SIRF AUDIO DOWNLOAD KARNA CHAHTA HAI TO MP3 ME CONVERT KARNE KE LIYE OPTIONS ADD KARNA >>>>>

if choice == "5":
    ydl_opts['postprocessors'] = [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]

# ----- DOWNLOAD START KARNA >>>>>

print("\nDownloading starting...")
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("\nDownload completed successfully!")