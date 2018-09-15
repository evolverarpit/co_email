# coding=utf-8
import re

import requests
from bs4 import BeautifulSoup


def get_email(links, domain, email_to_search):
    if not email_to_search:
        email_to_search = domain
    for link in links:
        try:
            data = requests.get(link).text
            if data:
                html = BeautifulSoup(data, 'html.parser')
                try:
                    email = clean_email(html.find(text=re.compile(
                        r'{}'.format(email_to_search))).strip(), domain)
                    if email:
                        return email.lower()
                except:
                    try:
                        email = clean_email(html.find(text=re.compile(
                            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")).strip(), domain)
                        if email:
                            return email.lower()
                    except:
                        email = clean_email(html.find(text=re.compile(
                            r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)')).strip(), domain)
                        if email:
                            return email.lower()
            raise ValueError
        except:
            continue
    else:
        return None


def clean_email(text, domain):
    text = text.split()
    if len(text) > 1:
        for txt in text:
            if domain in txt:
                text[0] = txt
    match = re.search(
        r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', text[0])
    if match:
        return match.group().strip()
    else:
        return None

def get_urls(file):
    urls = []
    with open(file, 'r') as f:
        data = f.readlines()
        for url in data:
            urls.append(url.strip())
    return urls
