# Offline-Video-Downloader
offline-video-downloader

# Media Downloader (Python Script)

## 📌 What This Script Does

This Python script allows you to download videos or extract audio (MP3) from multiple URLs in one go.
You simply provide links in a `links.txt` file, choose a quality, and the script downloads everything automatically.

---

## ⚙️ Setup Instructions

1. **Install Python (if not already installed)**
   Make sure Python 3 is installed on your system.

2. **Install yt-dlp**
   This script depends on `yt-dlp` for downloading media:

   ```
   pip install yt-dlp
   ```

3. **Prepare Files**

   * Place the Python script (e.g., `media_downloader.py`)
   * Create a file named `links.txt`
   * Ensure both are in the **same folder** 

---

## 🧾 How to Use

1. Open `links.txt`

2. Paste your media URLs (one per line), for example:

   ```
   https://example.com/video1
   https://example.com/video2
   ```

3. Save the file

4. Run the script:

   ```
   python media_downloader.py
   ```

5. Choose a download option:

   * Select a video quality (e.g., 480p, 720p, etc.)
   * Or choose **Best Audio (MP3)**

6. The script will:

   * Download all links in the list
   * Save them in the same folder

---

## 📂 Output

* Videos are saved as `.mp4`
* Audio is saved as `.mp3`
* Files are stored in the same directory as the script

---

## ⚠️ Important Notes

* `links.txt` must exist, or the script will fail
* Only resolutions **480p and above** are shown
* Internet connection is required
* Some websites may restrict downloads
* Make sure you comply with content usage rights

---

## ✅ Summary

* Add links → Run script → Pick quality → Downloads start automatically

---

Enjoy fast and simple batch downloading 🚀
