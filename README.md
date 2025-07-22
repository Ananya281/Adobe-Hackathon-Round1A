# 📄 Adobe Hackathon Round1A – PDF Heading Extractor

A lightweight Python-Docker utility that extracts **headings/outline structure** from PDF files using `PyMuPDF` (`fitz`). Built and containerized for submission in **Adobe Hackathon Round 1A**.

---

## 🚀 Features

- 📂 Batch processes all PDFs in a folder
- 🧠 Extracts structural headings (outline) from each PDF
- 🐳 Dockerized for clean, reproducible execution
- 🛡️ Runs fully offline with no network dependency

---

## 🛠️ Tech Stack

| Component     | Technology       |
|---------------|------------------|
| Language      | Python 3.10       |
| PDF Parser    | `PyMuPDF` (`fitz`) |
| Container     | Docker (Linux/amd64 compatible) |
| OS Support    | macOS, Windows, Linux |

---

## 📁 Folder Structure

├── Dockerfile
├── process_pdfs.py
├── sample_dataset/
│ └── pdfs/
│ ├── file01.pdf
│ ├── file02.pdf
│ └── ...
├── output/
│ └── file01.json
│ └── file02.json
└── README.md


---

## 🧪 How It Works

For each `.pdf` file inside the `sample_dataset/pdfs/` folder, the app:
1. Reads the PDF using `fitz`.
2. Extracts outline (heading) structure.
3. Dumps the result as a `.json` file inside the `output/` directory.

---

## 🐳 Run with Docker

### ✅ Step 1: Build the Docker Image

```bash
docker build --platform linux/amd64 -t adobe-hackathon-round1a:v1 .
```

```bash
docker run --rm -it \
  --platform linux/amd64 \
  -v "$(pwd)/sample_dataset/pdfs:/app/input/pdfs:ro" \
  -v "$(pwd)/output:/app/output" \
  --network none \
  adobe-hackathon-round1a:v1
```

  
