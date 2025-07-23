FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install PyMuPDF
RUN pip install PyMuPDF

# Copy the Python script
COPY process_pdfs.py .

# Run the script
CMD ["python", "process_pdfs.py"]
