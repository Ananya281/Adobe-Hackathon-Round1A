# 📄 Adobe Hackathon Round 1A – PDF Heading Extractor

A lightweight, containerized Python solution to extract **document titles** and **structured headings** (H1, H2, H3...) from PDF files. Designed to fulfill all constraints and evaluation metrics for **Adobe Hackathon Round 1A**.

---

## ✨ Features

- 📁 **Batch Processing**: Automatically processes all PDFs from the input folder
- 🧠 **Smart Extraction**: Uses layout analysis & clustering to extract titles and heading structures
- 💡 **Outline Detection**: Generates hierarchical headings (H1, H2, H3...) in clean JSON format
- 💾 **Output Ready**: Saves structured JSONs in the specified output directory
- 🐳 **Dockerized**: Easy to build and run with Docker (`linux/amd64` compatible)
- 🛡️ **Offline Execution**: No internet or GPU required

---

## 🛠️ Tech Stack

| 🔧 Component     | 🚀 Technology         |
|------------------|------------------------|
| Language         | Python 3.10            |
| PDF Parsing      | `pdfminer.six`         |
| Clustering       | `scikit-learn (KMeans)`|
| Numerical Ops    | `NumPy`                |
| Containerization | Docker                 |
| Architecture     | `linux/amd64 (x86_64)` |

---

## 📁 Project Structure


```
Adobe-Hackathon-Round1A/
├── Dockerfile            #Docker configuration
├── process_pdfs.py       #Main processing script
├── requirements.txt      #Python dependencies
├── README.md             #Project documentation
├── sample_dataset/
│ ├── pdfs/               #Input PDFs
│ │ └── sample.pdf
│ ├── outputs/            #Output JSONs
│ │ └── sample.json
│ └── schema/
│   └── output_schema.json  #JSON output schema
```

---

## 🚀 How to Run with Docker

`
Make sure Docker is installed and running.
`

#### ▶️ Step 1: Build the Docker Image

```
docker build --platform linux/amd64 -t adobe-hackathon-round1a:latest .
```

#### ▶️ Step 2: Run the Container

```bash
docker run --rm \
  -v "$(pwd)/sample_dataset/pdfs:/app/input:ro" \
  -v "$(pwd)/sample_dataset/outputs:/app/output" \
  --network none \
  adobe-hackathon-round1a:latest
```
Note: for Windows users (Git Bash):
If you're running the Docker command on Windows using Git Bash or MSYS2, please add `winpty` before `docker run` to avoid TTY-related issues.

## 📦 Output Format

The output is a structured JSON following this format:

```
{
  "title": "Document Title",
  "headings": [
    {
      "text": "Section Heading",
      "level": 1,
      "page": 1
    },
    ...
  ]
}
```

Schema reference: `sample_dataset/schema/output_schema.json`

## ✅ Compatibility

- ✅ Platform: `linux/amd64`
- ✅ Offline Mode: Yes
- ❌ No GPU or internet required
