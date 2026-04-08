FROM python:3.11
WORKDIR /app

# Install dependencies
RUN pip install fastapi uvicorn openenv-core>=0.2.0

# Copy files
COPY . .

# Install the current directory as a package
RUN pip install -e .

# Expose port
EXPOSE 8080

# The grader looks for this port specifically
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
