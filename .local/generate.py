import os
import shutil
import markdown
from jinja2 import Environment, FileSystemLoader

# Paths
SOURCE_DIR = ".source"
PAGES_DIR = os.path.join(SOURCE_DIR, "pages")
IMAGES_DIR = os.path.join(SOURCE_DIR, "images")
TEMPLATES_DIR = os.path.join(SOURCE_DIR, "templates")
OUTPUT_DIR = "."  # Root directory

# Set up Jinja environment
env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
template = env.get_template("page.html")  # Main template for pages

def convert_markdown_to_html(md_file):
    """Reads a Markdown file and converts it to HTML."""
    with open(md_file, "r", encoding="utf-8") as f:
        md_content = f.read()
    return markdown.markdown(md_content)

def process_markdown_files():
    """Convert Markdown files to HTML and save in root directory."""
    for md_file in os.listdir(PAGES_DIR):
        if md_file.endswith(".md"):
            md_path = os.path.join(PAGES_DIR, md_file)
            html_content = convert_markdown_to_html(md_path)
            title = os.path.splitext(md_file)[0].capitalize()  # Use filename as title
            if title == "Index":
                title = "Home"

            # Render with Jinja template
            output_html = template.render(title=title, content=html_content)

            # Save as HTML in the root directory
            output_filename = os.path.splitext(md_file)[0] + ".html"
            output_path = os.path.join(OUTPUT_DIR, output_filename)

            with open(output_path, "w", encoding="utf-8") as f:
                f.write(output_html)

            print(f"Generated: {output_path}")

def copy_images():
    """Copy images from __source__/images/ to images/ in the root directory."""
    if not os.path.exists("images"):
        os.makedirs("images")

    for img_file in os.listdir(IMAGES_DIR):
        img_src = os.path.join(IMAGES_DIR, img_file)
        img_dest = os.path.join("images", img_file)
        shutil.copy(img_src, img_dest)
        print(f"Copied: {img_dest}")

def main():
    process_markdown_files()
    copy_images()
    print("Site generation complete.")

if __name__ == "__main__":
    main()
