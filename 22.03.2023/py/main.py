# Write a function that when given a URL as a string,
# parses out just the domain name and returns it as a string


class WrongType(Exception):
    pass

# Solution one
from urllib.parse import urlparse

def domain_name_one(url: str) -> str:
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url

    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    domain_parts = domain.split('.')

    if len(domain_parts) > 2 and domain_parts[0] == 'www':
        domain_name = domain_parts[1]
    else:
        domain_name = domain_parts[0]

    return domain_name

# Solution two
import re

def domain_name_two(url: str) -> str:
    domain_pattern = re.compile(r'(?:https?://)?(?:www\.)?([^./]+)')
    match = domain_pattern.search(url)
    if match:
        return match.group(1)
    else:
        return ''

# Solution three
def domain_name_three(url: str) -> str:
    url = url.strip()

    # Remove URL scheme if present
    if url.startswith("http://"):
        url = url[len("http://"):]
    elif url.startswith("https://"):
        url = url[len("https://"):]

    # Remove 'www.' if present
    if url.startswith("www."):
        url = url[len("www."):]

    # Find the first occurrence of a period or a slash
    end_index = min(url.find('.'), url.find('/'))
    if end_index == -1:
        end_index = max(url.find('.'), url.find('/'))

    # Return the domain name
    return url[:end_index]

# Solution four
def extract_domain(netloc: str) -> str:
    parts = netloc.split('.')

    if len(parts) > 2 and parts[0] == 'www':
        return parts[1]
    else:
        return parts[0]

def domain_name_four(url: str) -> str:
    url = url.strip()

    # Remove URL scheme if present
    if url.startswith("http://"):
        url = url[len("http://"):]
    elif url.startswith("https://"):
        url = url[len("https://"):]

    # Split the URL using the first forward slash
    url_parts = url.split('/', 1)

    # Extract and return the domain name from the first part
    return extract_domain(url_parts[0])


import cProfile
import time
from timeit import default_timer as timer


if __name__ == '__main__':
    cProfile.run('domain_name_one("http://google.com")')
    cProfile.run('domain_name_two("http://google.com")')
    cProfile.run('domain_name_three("http://google.com")')
    cProfile.run('domain_name_four("http://google.com")')

    start_time = time.time()
    domain_name_one('http://google.com')
    domain_name_two('http://google.com')
    domain_name_three('http://google.com')
    domain_name_four('http://google.com')
    end_time = time.time()

    print('', end_time - start_time)
