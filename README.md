# Youtube-download
This is a simple desktop application built with PySide6 and yt-dlp (a youtube-dl fork) that allows you to download audio and video from YouTube.

Features

    Download YouTube videos as MP4, MKV, or AVI.
    Download YouTube audio as MP3, WAV, or FLAC.
    Support for single video and playlist downloads.
    User-friendly graphical interface.

Prerequisites

Before running this application, you need to have the following installed:

    Python 3.x: Download from python.org.
    yt-dlp: This is the core utility for downloading.
        You can download the yt-dlp.exe executable from the official GitHub repository: yt-dlp releases.
        Place yt-dlp.exe in a directory where you'll select it within the application.
    FFmpeg: This is required by yt-dlp for audio and video processing (e.g., converting formats, merging audio/video streams).
        Download ffmpeg.exe from the official FFmpeg website: ffmpeg.org/download.html.
        Extract the contents and ensure ffmpeg.exe (and ffprobe.exe) are in the same directory as yt-dlp.exe.
    Python Libraries:
        PySide6: For the graphical user interface.
        easygui: For simple file/directory dialogs.

You can install the Python libraries using pip:


pip install PySide6 easygui

How to Use

    Download the Source Code:
    Clone this repository or download the main.py and blueprint.py files to your local machine.

    Place Executables:
    Ensure that yt-dlp.exe and ffmpeg.exe (along with ffprobe.exe) are in the same directory on your computer. This directory will be selected in the application.

    Run the Application:
    Open a terminal or command prompt, navigate to the directory where you saved main.py, and run:
    python main.py

    Select yt-dlp.exe Directory:
    Upon launching the application, click the "Browse" button next to "Location of ytdlp.exe". Navigate to and select the directory where you placed yt-dlp.exe (and ffmpeg.exe).

    Enter YouTube URL:
    Paste the URL of the YouTube video or playlist you want to download into the "URL" text field.

    Choose Download Type (Audio/Video) and Format:
        Audio: Select the "Audio" tab. Choose your desired format (MP3, WAV, or FLAC). Check "Playlist" if you're downloading a playlist.
        Video: Select the "Video" tab. Choose your desired format (MP4, MKV, or AVI). Check "Playlist" if you're downloading a playlist.

    Start Download:
    Click the "Go!" button under the respective Audio or Video tab to start the download. The "Result" label will show the download progress.

    Open Destination Folder:
    Once the download is complete, you can click the "Destination" button to open the folder where your downloaded files are saved. By default, audio files will be saved in a subfolder named Audio and video files in a subfolder named Video within the yt-dlp.exe directory. If you downloaded a playlist, an additional subfolder named after the playlist will be created inside Audio or Video.

Troubleshooting

    "Did you forget to browse for location of ytdlp and ffmpeg executables?": This message appears if you click "Destination" before selecting the working directory using the "Browse" button.
    Download Errors: If you encounter errors during download, ensure:
        Your yt-dlp.exe and ffmpeg.exe are up to date.
        The URL is valid.
        You have an active internet connection.
        The selected directory has write permissions.


