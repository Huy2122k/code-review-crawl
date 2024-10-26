import json
import time
from multiprocessing import Pool
from types import MethodType

import pandas as pd
from common import *
from github import Auth, Github
from override import get_pulls
from tqdm import tqdm

# using an access token
auth = Auth.Token("")

# First create a Github instance:

# Public Web Github
g = Github(auth=auth)

repo = g.get_repo("home-assistant/core")

# repo.get_pulls = MethodType(get_pulls, repo) 
# pulls = repo.get_pulls(state='closed', extra={'reviewed': 'changes-requested' }, sort='created')


def fetch_pull(p_id):
    global repo
    pr = repo.get_pull(p_id)
    print("processing:", p_id)
    try:
        data = [{
            "pr_id": p_id,
            "files": json.dumps(extract_files(pr)),
            "info": json.dumps(pr_serializer(pr)),
            "reviews": json.dumps(extract_pull_request_reviews(pr)),
            "comments": json.dumps(extract_pull_request_review_comments(pr)),
        }]
    except Exception as e:
        print("ERROR === ", p_id, "====: ", e)
        return
    
    pd.DataFrame(data).to_csv("final_data.csv", mode="a", header=False, index=False)
    with open("mark_pr.txt", 'a') as file1:
        file1.write(f"{p_id},")
    print("DONE:", p_id)


if __name__ == "__main__":
    pulls = pd.read_csv("prs_home_assistant_core.csv")
    pull_ids = pulls.ID.values.tolist()

    with open("mark_pr.txt", 'r') as file1:
        mark = file1.read().split(",")
    
    mark = [int(id) for id in mark if id]
    pull_ids = list(set(pull_ids) - set(mark))
    
    with Pool(processes=8) as pool:  
        result = pool.map(fetch_pull, pull_ids)

    print("SUCCESSFUL")
    
# if __name__ == "__main__":
    # pulls = pd.read_csv("prs_home_assistant_core_approve.csv")
    # pull_ids = pulls.ID.values.tolist()
#     with open("mark_pr_approved.txt", 'r') as file1:
#         mark = file1.read().split(",")
    
#     mark = [int(id) for id in mark if id]
#     pull_ids = list(set(pull_ids) - set(mark))
    
#     with Pool(processes=8) as pool:  
#         result = pool.map(fetch_pull, pull_ids)

#     print("SUCCESSFUL")