FROM python:3.11
WORKDIR /app
# Added openenv-core here
RUN pip install fastapi uvicorn openenv-core>=0.2.0
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
