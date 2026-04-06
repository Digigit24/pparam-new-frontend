import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
urls = set()

for html in html_files:
    with open(html, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        matches = re.findall(r'https?://[^\s\"\'\>]+', content)
        for m in matches:
            urls.add(m)

for url in sorted(urls):
    print(url)
