import sys
import os
from firecrawl import FirecrawlApp

# Check if all required arguments are provided
if len(sys.argv) != 4:
    print("Usage: python3 firecrawl.py <url> <max_pages> <destination_folder>")
    sys.exit(1)

# Get arguments from command line
url = sys.argv[1]
max_pages = int(sys.argv[2])
dest_folder = sys.argv[3]

app = FirecrawlApp(api_url='http://localhost:3002', api_key='test')
crawl_status = app.crawl_url(
    url,
    params={
        'limit': max_pages, 
        'scrapeOptions': {'formats': ['markdown']}
    }
)

if crawl_status['success']:
    for page in crawl_status['data']:
        content = page['markdown']
        file_name = page['metadata']['title'].replace(' ', '_').replace('/', '-').replace('|', '_').lower() + '.md'
        file_path = os.path.join(dest_folder, file_name)
        with open(file_path, 'w') as f:
            f.write(content)
    print(f"Crawl completed. Files saved in {dest_folder}")
else:
    print("Crawl failed:", crawl_status.get('error', 'Unknown error'))
