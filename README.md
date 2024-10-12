# markdown-crawl

## Setup

```bash
git clone https://github.com/mendableai/firecrawl
cd firecrawl
cp apps/api/.env.example .env
sed -i 's/USE_DB_AUTHENTICATION=true/USE_DB_AUTHENTICATION=false/' .env
docker compose build
docker compose up -d
```

## Usage

```bash
./firecrawl.sh <url> <max_pages> <destination_folder>
```

## Status

- Open `http://localhost:3002/admin/@/queues/` to see the status of the crawler.
