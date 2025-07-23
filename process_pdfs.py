import os
import re
import json
import fitz  # PyMuPDF

INPUT_DIR = "/app/input/pdfs"
OUTPUT_DIR = "/app/output"

def extract_title(doc):
    """Extracts the visually largest text from the first page."""
    page = doc[0]
    blocks = page.get_text("dict")["blocks"]
    title_candidate = ""
    max_font_size = 0

    for block in blocks:
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                text = span.get("text", "").strip()
                if len(text) > 10 and span["size"] > max_font_size:
                    max_font_size = span["size"]
                    title_candidate = text

    return title_candidate

def extract_outline_from_toc(doc):
    """Extract structured outline only from the Table of Contents page."""
    outlines = []
    toc_page = None

    # Step 1: Locate the TOC page
    for i in range(min(6, len(doc))):
        text = doc[i].get_text()
        if "Table of Contents" in text:
            toc_page = doc[i]
            break

    if toc_page is None:
        return outlines  # TOC not found

    # Step 2: Use block extraction to get clean lines
    lines = []
    blocks = toc_page.get_text("blocks")
    for b in blocks:
        line = b[4].strip()
        if len(line) > 0:
            lines.append(line)

    # Step 3: Parse lines that match section headings
    for line in lines:
        # Match numbered headings like "2.1 Something ... 6"
        match = re.match(r"(?:(\d+(?:\.\d+)*))\s+(.+?)\s+(\d{1,3})$", line)
        if match:
            section = match.group(1)
            heading = match.group(2).strip()
            page = int(match.group(3))
            level = "H2" if "." in section else "H1"
            outlines.append({
                "level": level,
                "text": f"{section} {heading}",
                "page": page
            })
            continue

        # Match unnumbered headings like "Acknowledgements 4"
        fallback = re.match(r"(.+?)\s+(\d{1,3})$", line)
        if fallback:
            heading = fallback.group(1).strip()
            page = int(fallback.group(2))
            outlines.append({
                "level": "H1",
                "text": heading,
                "page": page
            })

    return outlines

def process_pdf(pdf_path):
    with fitz.open(pdf_path) as doc:
        title = extract_title(doc)
        outline = extract_outline_from_toc(doc)
        return {
            "title": title,
            "outline": outline
        }

def main():
    for filename in os.listdir(INPUT_DIR):
        if not filename.lower().endswith(".pdf"):
            continue
        pdf_path = os.path.join(INPUT_DIR, filename)
        result = process_pdf(pdf_path)

        json_filename = os.path.splitext(filename)[0] + ".json"
        output_path = os.path.join(OUTPUT_DIR, json_filename)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    main()
