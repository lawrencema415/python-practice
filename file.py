from urllib.request import urlopen

print("Python practice for web scraping")

url = "http://olympus.realpython.org/profiles/aphrodite"
page = urlopen(url)
page

html_bytes = page.read()
html = html_bytes.decode("utf-8")

print(html)