from urllib.request import urlopen
# import re

# print("Python practice for web scraping")

# url = "http://olympus.realpython.org/profiles/poseidon"
# page = urlopen(url)
# page

# html_bytes = page.read()
# html = html_bytes.decode("utf-8")

# print(html)

# title_index = html.find("<title>")
# 14

url = "http://olympus.realpython.org/profiles/dionysus"
html_page = urlopen(url)
html_text = html_page.read().decode("utf-8")

for string in ["Name: ", "Favorite Color:"]:
    string_start_idx = html_text.find(string)
    text_start_idx = string_start_idx + len(string)

    next_html_tag_offset = html_text[text_start_idx:].find("<")
    text_end_idx = text_start_idx + next_html_tag_offset

    raw_text = html_text[text_start_idx : text_end_idx]
    clean_text = raw_text.strip(" \r\n\t")
    print(clean_text)