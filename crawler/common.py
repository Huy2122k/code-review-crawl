import pandas as pd


def extract_values(data, columns):
    def get_nested_value(data, keys):
        if not keys:
            return data
        key = keys[0]
        if isinstance(data, dict) and key in data:
            return get_nested_value(data[key], keys[1:])
        else:
            return None
    result = {}
    for column in columns:
        keys = column.split('.')
        value = get_nested_value(data, keys)
        result[column] = value
    return result


def extract_files(pr):
    py_files = []
    for f in pr.get_files():
        if f.filename.endswith(".py"):
            file_changes_info = file_changes_serializer(f)
            file_changes_info["pr_id"] = pr.id
            py_files.append(file_changes_info)
    return py_files

def pr_serializer(pr):
    target_data = pr.__dict__["_rawData"]
    columns = ["id", "title", "number", "state", "title", "body", "review_comments_url", "review_comment_url", "comments_url"]
    filtered = extract_values(target_data, columns)
    return filtered

def extract_pull_request_reviews(pr):
    reviews = []
    columns = ['id', 'body', 'state', 'user.login', 'user.type', 'submitted_at']
    
    for rv in pr.get_reviews():
        filtered = extract_values(rv.__dict__["_rawData"], columns)
        filtered["pr_id"] = pr.id
        reviews.append(filtered)
    
    return reviews

def extract_pull_request_review_comments(pr):
    comments = []
    columns = ['pull_request_review_id', 'id', 'diff_hunk', 'path', 'user.login', 'user.type', 'body', 'created_at', 'updated_at', 
               'reactions', 'start_line', 
               'original_start_line', 'start_side', 'line', 'original_line', 'original_position', 'position', 
               'subject_type']
    
    for cms in pr.get_review_comments():
        filtered = extract_values(cms.__dict__["_rawData"], columns)
        comments.append(filtered)
        
    return comments

def file_changes_serializer(file):
    return file.__dict__["_rawData"]
#     return {
#         "filename": file.filename,
#         "patch": file.patch,
#         "contents_url": f.contents_url,
#         "deletions": f.deletions,
#         "additions": f.additions,
#         "raw_url": f.raw_url,
#         "changes": f.changes,
#         "": f.
#     }