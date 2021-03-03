import collections
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
  """ Gets first link from a page and returns the tag of it
  """
  body = soup.find(name='div', class_='mw-parser-output')
  for p in body.find_all(name='p', recursive=False):
    for a in p.find_all(name='a', href=re.compile('^(/wiki/).*$'), recursive=False):
      if a.text and a.text[0] != '(':
        return a
  return None

leads_to_fail = set()
def find_philosphy(url: str) -> (bool, int, set, list):
  path = []
  visited = set()
  while url not in visited:
    # Update visited set and path to this url
    path.append(url.split('/')[-1])
    visited.add(url)

    if url in leads_to_fail:
      # Check if we know this path leads to failure already
      return (False, 0, visited, path)

    # Get the page from wikipedia and find the first link
    page = get_wikipedia_page(url)
    anchor = get_first_anchor(page)

    if anchor == None: 
      # The page, suprisingly, has no links
      return (False, 0, visited, path)

    if anchor.get('href') == '/wiki/Philosophy':
      # First link is philosophy
      path.append('Philosophy')
      return (True, len(path) + 1, visited, path)

    # Set url for next iterator
    url = f"https://en.wikipedia.org{anchor.get('href')}"

  # We entered a loop
  print('Loop ', end='')
  path.append(url.split('/')[-1])
  return (False, 0, visited, path)

pass_count = 0
fail_count = 0
max_path_len = -1
last_page_frequencies = collections.defaultdict(int)
for i in range(100):
  result, count, visited, path = find_philosphy(random_url())
  last_page_frequencies[path[-1]] += 1
  if result:
    pass_count += 1
    max_path_len = max(count, max_path_len)
    print('~~~ Path Found: ', ' -> '.join(path))
  else:
    fail_count += 1
    leads_to_fail = leads_to_fail | visited
    print('Failure: ', ' -> '.join(path))

print('Passes: ', pass_count)
print('Fails: ', fail_count)
print('Longest path: ', max_path_len)
print('\nFrequencies of the last page in the chain:')
for k,v in last_page_frequencies.items():
  print(k, ': ', v)
