# Use minimal Python base image, AMD64 compatible
FROM --platform=linux/amd64 python:3.10

# Set working directory
WORKDIR /app

# Copy code
COPY process_pdfs.py .
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create input/output folders (if they’re not mounted at runtime)
RUN mkdir -p /app/input /app/output

# Run the processing script when container starts
CMD ["python", "process_pdfs.py"]