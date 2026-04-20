# 🎬 Offline Media Downloader (Python + yt-dlp)

## 📌 Overview

This project is a simple yet powerful offline media downloader built using Python. It allows you to download videos or extract audio (MP3) from multiple URLs in one go using a single script.

You provide links in a `links.txt` file, select your preferred quality, and the script handles everything — downloading, merging video/audio, and saving files locally.

---

## ⚡ Core Features

* 📥 **Batch Downloading**
  Download multiple videos at once from a list of URLs

* 🎥 **Video + Audio Merging**
  Automatically merges best video and audio into `.mp4`

* 🎧 **Audio Extraction (MP3)**
  Convert videos into high-quality MP3 files

* 📊 **Quality Selection**
  Choose from available resolutions (480p and above)

* ⚡ **Automated Workflow**
  One command runs everything

---

## 🧩 Tools & Technologies

* **Python 3** – Core script logic
* **yt-dlp** – Media downloading engine
* **subprocess** – Executes yt-dlp commands
* **json** – Parses video format data
* **sys** – Handles program exits and errors

All logic is implemented in the main script .

---

# 🚀 FULL STEP-BY-STEP SETUP GUIDE

---

## 🪟 Windows Installation Guide

### ✅ Step 1: Install Python

1. Download Python from the official website
2. Run installer
3. ✔️ Check **"Add Python to PATH"**
4. Verify:

```bash id="win-python-check"
python --version
```

---

### ✅ Step 2: Install yt-dlp

```bash id="win-ytdlp-install"
pip install yt-dlp
```

---

### ✅ Step 3: (Optional but Recommended) Install FFmpeg

FFmpeg is required for:

* Merging video + audio
* Converting to MP3

1. Download FFmpeg
2. Extract it
3. Add `bin` folder to PATH

Verify:

```bash id="win-ffmpeg-check"
ffmpeg -version
```

---

### ✅ Step 4: Prepare Project Files

Make sure both files are in the **same folder**:

```text id="win-folder-structure"
media_downloader.py
links.txt
```

---

### ✅ Step 5: Add Download Links

Open `links.txt` and paste URLs:

```text id="win-links-example"
https://example.com/video1
https://example.com/video2
```

---

### ✅ Step 6: Run the Script

```bash id="win-run"
python media_downloader.py
```

---

## 🐧 Linux Installation Guide

### ✅ Step 1: Install Python & Pip

```bash id="linux-python-install"
sudo apt update
sudo apt install python3 python3-pip
```

Verify:

```bash id="linux-python-check"
python3 --version
```

---

### ✅ Step 2: Install yt-dlp

```bash id="linux-ytdlp-install"
pip3 install yt-dlp
```

---

### ✅ Step 3: Install FFmpeg

```bash id="linux-ffmpeg-install"
sudo apt install ffmpeg
```

---

### ✅ Step 4: Prepare Files

```text id="linux-folder-structure"
media_downloader.py
links.txt
```

---

### ✅ Step 5: Add Links

```text id="linux-links-example"
https://example.com/video1
https://example.com/video2
```

---

### ✅ Step 6: Run the Script

```bash id="linux-run"
python3 media_downloader.py
```

---

# ▶️ HOW TO USE

### 🧪 Step-by-Step Flow

```text id="usage-flow"
1. Add links to links.txt
2. Run the script
3. Select quality option
4. Wait for downloads
5. Files saved automatically
```

---

### 📊 Example Output

```bash id="example-output"
Available Qualities:

1. 480p
2. 720p
3. 1080p
4. Best Audio (MP3)

Choose quality:
```

---

### 🎯 What Happens Next

* Script downloads all links
* Merges video + audio (if video selected)
* Converts to MP3 (if audio selected)
* Saves files in same folder

---

# 🔄 SYSTEM WORKFLOW

```text id="workflow"
Read links.txt
   ↓
Fetch available formats (yt-dlp)
   ↓
Display quality options
   ↓
User selects option
   ↓
Download all media
   ↓
Save files locally
```

---

# ⚠️ IMPORTANT NOTES

* `links.txt` must exist in the same folder
* Only resolutions **≥ 480p** are shown
* Internet is required for downloading media
* Some websites may restrict downloads
* Respect copyright and usage rights

---

# 📂 OUTPUT

* 🎥 Videos → `.mp4`
* 🎧 Audio → `.mp3`
* 📁 Saved in current directory

---

# ✅ FINAL SUMMARY

A simple and efficient media downloader that:

* Handles multiple downloads at once
* Lets you choose quality
* Supports both video and audio
* Works on Linux and Windows

---

🔥 Perfect for offline media collection and automation tasks.

---
