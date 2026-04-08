FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install fastapi uvicorn openenv-core>=0.2.0
RUN pip install -e .
EXPOSE 8080
CMD ["server"]
