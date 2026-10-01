import os
import yt_dlp

download_folder = os.path.expanduser("~/storage/shared/Download")

def download_video(url):
    options = {
        "format": "bestvideo+bestaudio/best",
        "outtmpl": os.path.join(download_folder, "%(title)s.%(ext)s"),
        "merge_output_format": "mp4",
    }

    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])

        print("\n✅ Download complete!")
        print(f"📁 Saved to: {download_folder}")

    except Exception as e:
        print(f"\n❌ Error: {e}")


def main():
    print("=" * 40)
    print("      YouTube Video Downloader")
    print("=" * 40)

    url = input("\n🔗 Paste YouTube URL: ").strip()

    if not url:
        print("❌ No URL entered.")
        return

    download_video(url)


if __name__ == "__main__":
    main()
