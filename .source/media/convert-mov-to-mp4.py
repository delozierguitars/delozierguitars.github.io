import os
import subprocess

# Define the folder where the .mov files are located
MEDIA_DIR = "."

def convert_mov_to_mp4(source_file, dest_file):
    """Converts a .mov file to .mp4 using FFmpeg with optimized settings."""
    
    # Skip conversion if the MP4 file already exists
    if os.path.exists(dest_file):
        print(f"Skipping {source_file} (already converted).")
        return

    print(f"Converting {source_file} to {dest_file}...")

    # FFmpeg command with compatible settings for QuickTime & browsers
    command = [
        "ffmpeg", "-i", source_file,  # Input file
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "slow", "-crf", "23",  # Video settings
        "-c:a", "aac", "-b:a", "128k",  # Audio settings
        "-movflags", "+faststart",  # Optimize for web streaming
        dest_file
    ]

    try:
        subprocess.run(command, check=True)
        print(f"✅ Successfully converted: {dest_file}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error converting {source_file}: {e}")

def main():
    """Find and convert all .mov files in the current directory."""
    for file in os.listdir(MEDIA_DIR):
        if file.lower().endswith(".mov"):
            source_path = os.path.join(MEDIA_DIR, file)
            dest_path = os.path.join(MEDIA_DIR, file.replace(".mov", ".mp4"))
            convert_mov_to_mp4(source_path, dest_path)

    print("🎸 Conversion complete!")

if __name__ == "__main__":
    main()
    