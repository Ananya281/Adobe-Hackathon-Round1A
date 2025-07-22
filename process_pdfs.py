import os
import fitz  # PyMuPDF
import json
from pathlib import Path

def extract_headings(pdf_path):
    doc = fitz.open(pdf_path)
    headings = []
    font_sizes = []

    for page_num, page in enumerate(doc):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                for span in line["spans"]:
                    text = span["text"].strip()
                    size = span["size"]

                    if len(text) < 3 or not text[0].isalpha():
                        continue

                    font_sizes.append(size)
                    headings.append({
                        "text": text,
                        "size": size,
                        "page": page_num
                    })

    sizes_ranked = sorted(list(set(font_sizes)), reverse=True)
    title_size = sizes_ranked[0]
    h1_size = sizes_ranked[1] if len(sizes_ranked) > 1 else title_size
    h2_size = sizes_ranked[2] if len(sizes_ranked) > 2 else h1_size
    h3_size = sizes_ranked[3] if len(sizes_ranked) > 3 else h2_size

    outline = []
    title = None
    used_titles = set()

    for item in headings:
        level = None
        if item["size"] == title_size and not title:
            title = item["text"]
            continue
        elif item["size"] == h1_size:
            level = "H1"
        elif item["size"] == h2_size:
            level = "H2"
        elif item["size"] == h3_size:
            level = "H3"

        if level:
            outline.append({
                "level": level,
                "text": item["text"],
                "page": item["page"]
            })

    return {
        "title": title if title else "Untitled Document",
        "outline": outline
    }

def process_all():
    input_dir = Path("/app/input")
    output_dir = Path("/app/output")

    for file in input_dir.glob("*.pdf"):
        result = extract_headings(file)
        output_file = output_dir / f"{file.stem}.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2)
        print(f"✅ Processed: {file.name}")


if __name__ == "__main__":
    process_all()
