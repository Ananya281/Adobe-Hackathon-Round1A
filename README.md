# 📄 Adobe Hackathon Round1A – PDF Heading Extractor

A lightweight, Dockerized Python solution for extracting structured **title and headings (outline)** from PDFs. Built to meet all constraints and evaluation criteria for **Adobe Hackathon Round 1A**.

---

## 🚀 Features

- 📂 Automatically processes all PDFs
- 🧠 Extracts document **title** and **outline structure** (H1, H2, H3...) from PDF content
- 💾 Generates JSON outputs in `/app/output`, matching the required schema
- 🐳 Fully containerized with Docker (`linux/amd64` compatible)
- 🛡️ Works **offline**, **no internet** or GPU required

---

## 🛠️ Tech Stack

| Component     | Technology         |
|---------------|--------------------|
| Language      | Python 3.10         |
| PDF Parsing   | `pdfminer.six`      |
| Clustering    | `scikit-learn` (KMeans) |
| Array Ops     | `numpy`             |
| Container     | Docker              |
| Architecture  | `linux/amd64` (x86_64) |

---

## 📁 Folder Structure

Challenge_1a/
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
│ └── output_schema.json  #JSON output schema


## Run the Solution with Docker

Step 1: Build the Docker Image

`docker build --platform linux/amd64 -t adobe-hackathon-round1a:latest .`

 Step 2: Run the Container

 ```
 docker run --rm \
   -v $(pwd)/sample_dataset/pdfs:/app/input:ro \
   -v $(pwd)/sample_dataset/outputs:/app/output \
   --network none \
   adobe-hackathon-round1a:latest
 ```
