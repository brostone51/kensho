import re

import requests
from bs4 import BeautifulSoup

def random_url():
  """ Returns a random wikipedia url
  """
  page = requests.get('https://en.wikipedia.org/wiki/Special:Random')
  return page.url

def get_wikipedia_page(url: str) -> BeautifulSoup:
  """ Make soup from a wiki page
  """
  page = requests.get(url)
  soup = BeautifulSoup(page.text, 'html.parser')
  return soup

def get_first_anchor(soup: BeautifulSoup):
  """ Gets first link from a page and retuns the tag of it
  """
  body = soup.find(name='div', id='bodyContent')
  for p in soup.find_all(name=['p', 'ul']):
    for a in p.find_all(name='a', href=re.compile('^(/wiki/).*$')):
      if a.text and a.text[0] != '(':
        return a
  return None

leads_to_pass = set()
leads_to_fail = set()
def find_philosphy(url: str) -> (bool, int, set):
  visited = set()
  while url not in visited:
    print(f"Visiting {url}...")
    visited.add(url)
    if url in leads_to_fail:
        print(f'We know where {url} leads us... :(')
        return (False, 0, visited)
    if url in leads_to_pass:
      print(f'We know where {url} leads us!!! :)')
      return (True, len(visited), visited)
    page = get_wikipedia_page(url)
    anchor = get_first_anchor(page)
    if anchor == None: return (False, 0, visited)
    if anchor.get('href') == '/wiki/Philosophy': return (True, len(visited), visited)
    url = f"https://en.wikipedia.org{anchor.get('href')}"
  return (False, 0, visited)

pass_count = 0
fail_count = 0
max_path_len = -1
for i in range(100):
  result, count, visited = find_philosphy(random_url())
  if result:
    pass_count += 1
    max_path_len = max(count, max_path_len)
    leads_to_pass = leads_to_pass | visited
  else:
    fail_count += 1
    leads_to_fail = leads_to_fail | visited

print('Passes: ', pass_count)
print('Fails: ', fail_count)
print('Longest path: ', max_path_len)
