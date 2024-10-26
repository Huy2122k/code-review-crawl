# GitHub Crawler

A Python-based GitHub data crawler that utilizes the `requests` library to scrape and analyze information from GitHub repositories. This tool can fetch data such as pull requests, issues, commits, and more from specified repositories, allowing you to gather insights directly from the GitHub API.

## Features

- Crawl public repositories for:
  - Pull requests (open/closed)
  - Issues (open/closed)
  - Commit history
  - Repository metadata (stars, forks, contributors)
- Supports pagination for large repositories.
- Customizable headers and request parameters.
- Handles rate limiting and authentication.
- Saves crawled data in JSON or CSV formats.

## Prerequisites

- Python 3.7 or higher
- GitHub API token (for authenticated requests to avoid rate limits)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/github-crawler.git
   cd github-crawler
Install the required dependencies:


```
pip install -r requirements.txt
```
The requirements.txt file includes:

requests: For making HTTP requests.
pandas: For data manipulation and storage (if exporting to CSV).
PyYAML (optional): For configuration management.
Set up your GitHub API token:

Create a .env file in the root directory:

```
GITHUB_TOKEN=your_github_personal_access_token
Replace your_github_personal_access_token with your actual token.
```

# Usage
## 1. Fetch Pull Requests
To crawl closed pull requests from a specific repository, run:
```
python github_crawler.py --repo "owner/repo" --data "pulls" --state "closed"
```
## 2. Fetch Issues
To crawl open issues from a specific repository, run:
```
python github_crawler.py --repo "owner/repo" --data "issues" --state "open"
```
## 3. Fetch Repository Metadata
To fetch general information about a repository (stars, forks, contributors):
```
python github_crawler.py --repo "owner/repo" --data "repo"
```
## 4. Export Data
By default, the crawler will save the results as a JSON file in the output directory. To export data as CSV, use:
```
python github_crawler.py --repo "owner/repo" --data "issues" --output "csv"

Command-line Arguments
--repo: The target repository in owner/repo format.
--data: Type of data to fetch (pulls, issues, repo).
--state: (Optional) The state of the data (open, closed, all).
--output: (Optional) The output format (json, csv).
Handling Rate Limiting
To avoid hitting GitHub's rate limits, the script includes a delay between requests and supports using a GitHub Personal Access Token for authenticated requests. Ensure your token has appropriate permissions for the actions you want to perform.
```
Example
Here's an example of using the script to fetch closed pull requests from the home-assistant/core repository:
```
python github_crawler.py --repo "home-assistant/core" --data "pulls" --state "closed" --output "json"
```
This will create a JSON file containing all closed pull requests from the specified repository.

Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request with improvements or bug fixes. Please ensure your changes pass existing tests and add tests for any new features.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Acknowledgements
Requests Library - For making HTTP requests.
GitHub API Documentation - For details on the GitHub REST API.
Special thanks to the open-source community for their valuable tools and resources.