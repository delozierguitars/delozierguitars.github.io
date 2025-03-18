import os
import shutil
import markdown
import subprocess
from jinja2 import Environment, FileSystemLoader

# Paths
SOURCE_DIR = ".source"
PAGES_DIR = os.path.join(SOURCE_DIR, "pages")
MEDIA_DIR = os.path.join(SOURCE_DIR, "media")
TEMPLATES_DIR = os.path.join(SOURCE_DIR, "templates")
OUTPUT_DIR = "."  # Root directory

# Set up Jinja environment
env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
template = env.get_template("page.html")  # Main template for pages

def convert_markdown_to_html(md_file):
    """Reads a Markdown file and converts it to HTML."""
    with open(md_file, "r", encoding="utf-8") as f:
        md_content = f.read()
    return markdown.markdown(md_content, extensions=["extra"])

def process_markdown_files():
    """Convert Markdown files to HTML and save in root directory."""
    for md_file in os.listdir(PAGES_DIR):
        if md_file.endswith(".md"):
            md_path = os.path.join(PAGES_DIR, md_file)
            html_content = convert_markdown_to_html(md_path)
            title = os.path.splitext(md_file)[0].capitalize()  # Use filename as title
            if title == "Index":
                title = "Home"

            navbar_position = "left" if title == "Home" else "top"

            # Render with Jinja template
            output_html = template.render(title=title, content=html_content, navbar=navbar_position)

            # Save as HTML in the root directory
            output_filename = os.path.splitext(md_file)[0] + ".html"
            output_path = os.path.join(OUTPUT_DIR, output_filename)

            with open(output_path, "w", encoding="utf-8") as f:
                f.write(output_html)

            print(f"Generated: {output_path}")


def copy_media():
    """Copy media from __source__/media/ to media/ in the root directory."""
    if not os.path.exists("media"):
        os.makedirs("media")

    for root, dirs, files in os.walk(MEDIA_DIR):  # Recursively go through media folder
        for media_file in files:
            if media_file.endswith(".mp4"):
                media_src = os.path.join(root, media_file)
                media_dest = os.path.join("media", os.path.relpath(media_src, MEDIA_DIR))
                shutil.copy(media_src, media_dest)
                print(f"Copied: {media_dest}")
            if media_file.endswith(".jpg"):
                media_src = os.path.join(root, media_file)
                media_dest = os.path.join("media", os.path.relpath(media_src, MEDIA_DIR))
                shutil.copy(media_src, media_dest)
                print(f"Copied: {media_dest}")
            if media_file.endswith(".png"):
                media_src = os.path.join(root, media_file)
                media_dest = os.path.join("media", os.path.relpath(media_src, MEDIA_DIR))
                shutil.copy(media_src, media_dest)
                print(f"Copied: {media_dest}")

def main():
    process_markdown_files()
    copy_media()
    print("Site generation complete.")

if __name__ == "__main__":
    main()