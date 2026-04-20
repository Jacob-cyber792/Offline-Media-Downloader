import subprocess
import json
import sys

def get_first_url():
    try:
        with open("links.txt", "r") as f:
            for line in f:
                if line.strip():
                    return line.strip()
    except FileNotFoundError:
        print("links.txt file not found.")
        sys.exit(1)

def get_formats(url):
    result = subprocess.run(
        ["yt-dlp", "-J", url],
        capture_output=True,
        text=True
    )
    data = json.loads(result.stdout)
    return data.get("formats", [])

def get_resolutions(formats):
    resolutions = set()
    for f in formats:
        if f.get("height") and f["height"] >= 480:
            resolutions.add(f["height"])
    return sorted(resolutions)

def display_options(resolutions):
    print("\nAvailable Qualities (Video + Audio merged):\n")
    for idx, height in enumerate(resolutions, 1):
        print(f"{idx}. {height}p")
    print(f"{len(resolutions)+1}. Best Audio (MP3)")

def download_all(selected_height=None, audio_only=False):
    with open("links.txt", "r") as f:
        links = [line.strip() for line in f if line.strip()]

    for idx, url in enumerate(links, 1):
        print(f"\nDownloading {idx}/{len(links)}...\n")

        if audio_only:
            subprocess.run([
                "yt-dlp",
                "-f", "bestaudio",
                "--extract-audio",
                "--audio-format", "mp3",
                "--audio-quality", "0",
                url
            ])
        else:
            format_string = f"bestvideo[height={selected_height}]+bestaudio/best"
            subprocess.run([
                "yt-dlp",
                "-f", format_string,
                "--merge-output-format", "mp4",
                url
            ])

def main():
    print("=" * 50)
    print("   YouTube Batch Downloader (Merged A/V)")
    print("=" * 50)

    first_url = get_first_url()
    formats = get_formats(first_url)
    resolutions = get_resolutions(formats)

    if not resolutions:
        print("No resolutions >= 480p found.")
        sys.exit()

    display_options(resolutions)

    choice = int(input("\nChoose quality: "))

    if 1 <= choice <= len(resolutions):
        selected_height = resolutions[choice - 1]
        download_all(selected_height=selected_height)

    elif choice == len(resolutions) + 1:
        download_all(audio_only=True)

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
