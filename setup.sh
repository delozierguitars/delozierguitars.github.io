#!/bin/bash

# Define directories
SOURCE_DIR="__source__"
PAGES_DIR="$SOURCE_DIR/pages"
IMAGES_DIR="$SOURCE_DIR/images"
TEMPLATES_DIR="templates"

# Create necessary directories
echo "Creating directory structure..."
mkdir -p "$PAGES_DIR" "$IMAGES_DIR" "$TEMPLATES_DIR"

# Create sample Markdown files
echo "Creating sample Markdown files..."
cat > "$PAGES_DIR/index.md" <<EOL
# Welcome to My Static Site

This is a simple static site generated with Markdown and Jinja2.
EOL

cat > "$PAGES_DIR/about.md" <<EOL
# About This Site

This site is built using Python, Jinja2, and Markdown.
EOL

cat > "$PAGES_DIR/contact.md" <<EOL
# Contact Us

Email us at [info@example.com](mailto:info@example.com).
EOL

# Create sample image placeholder
echo "Adding a placeholder image..."
touch "$IMAGES_DIR/logo.png"

# Create Jinja base template
echo "Creating Jinja templates..."
cat > "$TEMPLATES_DIR/page.html" <<EOL
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="/">My Site</a>
            <div class="navbar-nav">
                <a class="nav-link" href="/">Home</a>
                <a class="nav-link" href="/about.html">About</a>
                <a class="nav-link" href="/contact.html">Contact</a>
            </div>
        </div>
    </nav>

    <div class="container mt-4">
        <h1>{{ title }}</h1>
        <div>{{ content | safe }}</div>
    </div>

    <footer class="text-center py-3 mt-5 bg-light">
        <p>© 2024 My Static Site</p>
    </footer>
</body>
</html>
EOL

# Create Python script for static site generation
echo "Creating site generator script..."
cat > "generate.py" <<EOL
import os
import shutil
import markdown
from jinja2 import Environment, FileSystemLoader

# Paths
SOURCE_DIR = "__source__"
PAGES_DIR = os.path.join(SOURCE_DIR, "pages")
IMAGES_DIR = os.path.join(SOURCE_DIR, "images")
TEMPLATES_DIR = "templates"
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
EOL

# Create requirements.txt
echo "Creating requirements.txt..."
cat > "requirements.txt" <<EOL
Jinja2
Markdown
EOL

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

echo "Setup complete. Run 'python generate.py' to build your static site."