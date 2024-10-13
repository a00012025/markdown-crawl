import sys
import os
from firecrawl import FirecrawlApp

# Check if all required arguments are provided
if len(sys.argv) != 3:
    print("Usage: python3 scrape.py <url> <destination_folder>")
    sys.exit(1)

# Get arguments from command line
url = sys.argv[1]
dest_folder = sys.argv[2]

app = FirecrawlApp(api_url='http://localhost:3002', api_key='test')
scrape_status = app.scrape_url(
    url,
    params={'formats': ['markdown']}
)

content = scrape_status['markdown']
title = scrape_status['metadata']['title']
file_name = title.replace(' ', '_').replace('/', '-').replace('|', '_').lower() + '.md'
file_path = os.path.join(dest_folder, file_name)
with open(file_path, 'w') as f:
    f.write(content)
print(f"Scrape completed. Files saved to {file_path}")
