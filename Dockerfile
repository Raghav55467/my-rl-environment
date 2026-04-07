FROM python:3.11

WORKDIR /app

# This covers every possible name for the library
RUN pip install openenv openenv-core fastapi uvicorn

# If the above fails, this is the 'Force' backup (No spaces in these lines)
RUN pip install git+https://github.com/openenv/openenv.git || true

COPY . .

CMD ["python", "main.py"]
