# Use an official lightweight Python image
FROM python:3.11-slim

# Set workdir
WORKDIR /app

# Copy project files
COPY requirements.txt .
COPY app1.py .
COPY modell.pkl .
# If you have other required files or folders, copy them as well.
# COPY data.csv . 
# COPY other_files/ ./other_files/

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Streamlit runs on PORT, default to 8501. App Runner supplies PORT as an env var.
ENV PORT=${PORT:-8080}
ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_SERVER_ENABLE_CORS=false
ENV STREAMLIT_SERVER_PORT=$PORT
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0

# Expose port (optional, for local)
EXPOSE $PORT

# Run the streamlit app
CMD ["sh", "-c", "streamlit run app1.py --server.port $PORT --server.address 0.0.0.0"]
