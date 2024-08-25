from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import sys
import asyncio
import aiohttp
import csv
import re
from collections import deque

def clean_text(text):
    return ' '.join(re.findall(r'\S+', text))

async def crawl_url(session, url, base_domain, visited, to_visit, results):
    if url in visited:
        return

    try:
        async with session.get(url, timeout=10) as response:
            if response.status != 200:
                return
            content = await response.text()
            soup = BeautifulSoup(content, 'lxml')
            text_content = clean_text(' '.join(soup.stripped_strings))
            results.append((url, text_content))
            visited.add(url)
            print(f"Crawled: {url}")

            new_urls = {
                urljoin(url, link['href'])
                for link in soup.find_all('a', href=True)
                if urlparse(urljoin(url, link['href'])).netloc == base_domain
                and '#' not in link['href']
                and urljoin(url, link['href']) not in visited
                and urljoin(url, link['href']) not in to_visit
            }
            to_visit.extend(new_urls)
    except (aiohttp.ClientError, asyncio.TimeoutError):
        print(f"Error crawling: {url}")

async def crawl_website(base_url, output_file):
    base_domain = urlparse(base_url).netloc
    visited = set()
    to_visit = deque([base_url])
    results = []

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=50)) as session:
        tasks = set()
        while to_visit or tasks:
            while to_visit and len(tasks) < 50:
                url = to_visit.popleft()
                if url not in visited:
                    task = asyncio.create_task(crawl_url(session, url, base_domain, visited, to_visit, results))
                    tasks.add(task)
            
            if tasks:
                done, tasks = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
                for task in done:
                    await task

    unique_results = list({result[0]: result for result in results}.values())

    with open(f"{output_file}.csv", mode='w', newline='', encoding='utf-8') as fp:
        writer = csv.writer(fp, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["URL", "Content"])
        writer.writerows(unique_results)

    print(f"Crawling completed! Total crawled URLs: {len(unique_results)}")

async def main():
    if len(sys.argv) != 3:
        print("Usage: python webcrawling2csv.py <base_url> <output_file>")
        sys.exit(1)
    
    base_url = sys.argv[1]
    output_file = sys.argv[2]
    await crawl_website(base_url, output_file)

if __name__ == "__main__":
    asyncio.run(main())