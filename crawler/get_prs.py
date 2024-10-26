from multiprocessing import Pool

import pandas as pd
import requests as rq
from bs4 import BeautifulSoup
from tqdm import tqdm
import time

def parse_pr_html(html_content):
    # Parse HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Tìm các pull request
    pull_requests = soup.find_all('div', class_='js-issue-row')

    # Tạo list để chứa dữ liệu
    data = []

    # Lấy ID và tiêu đề
    for pr in pull_requests:
        pr_id = pr.get('id').replace('issue_', "")
        pr_title = pr.find('a', class_='js-navigation-open').text.strip()
        data.append({'ID': pr_id, 'Title': pr_title})

    # Tạo DataFrame
    return data

def call(page):
    res = rq.get(f'https://github.com/home-assistant/core/pulls?page={page}&q=is%3Apr+is%3Aclosed+review%3Achanges-requested', headers = {'User-agent': 'your bot 0.1'})
    print(res.status_code)
    if res.status_code != 200:
        time.sleep(2)
        res = call(page)
    
    return res

def get_pr_by_page(page):
    res = call(page)
    data = parse_pr_html(res.content)
    return data


with Pool(processes=4) as pool:  
    dfs = list(tqdm(pool.imap(get_pr_by_page, range(1, 137)), total=136))

arr = []
for ar in dfs:
    arr += ar
    
df_prs = pd.DataFrame(arr)
df_prs.to_csv("prs_home_assistant_core.csv")