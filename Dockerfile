FROM python:3.11-slim

# prepare system to get needed dependencies
RUN apt-get update && apt-get install -y \
    curl unzip chromium-driver chromium \
    && rm -rf /var/lib/apt/lists/*

# chrome env for selenium
ENV CHROME_BIN=/usr/bin/chromium
ENV PATH=$PATH:/usr/lib/chromium

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "main.py"]
