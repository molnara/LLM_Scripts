FROM ollama/ollama

# Install system libraries
RUN apt-get update

# Install Python
RUN apt-get install -y python3 && \
    apt-get install -y pip

# Install the application dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
