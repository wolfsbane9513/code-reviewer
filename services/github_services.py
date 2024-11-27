# services/github_service.py
import requests
import base64
from config.config import Config

class GitHubService:
    def __init__(self):
        self.headers = {
            'Authorization': f'token {Config.GITHUB_KEY}',
            'X-GitHub-Api-Version': '2022-11-28'
        }
    
    def get_file_tree(self, owner, repo, path='', level=0):
        global_path = ""
        api_url = f"https://api.github.com/repos/{owner}/{repo}/contents/"
        response = requests.get(api_url, headers=self.headers)
        items = response.json()
        
        return self._process_items(items, level, Config.IGNORE_DIRS)
    
    def get_file_content(self, owner, repo, path):
        api_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
        response = requests.get(api_url, headers=self.headers)
        
        if response.status_code != 200:
            return f"Error: {response.status_code} - {response.reason}"
            
        file_content = response.json()
        
        if file_content['size'] > Config.MAX_FILE_SIZE:
            return "Skipped: File size is greater than 1 MB."
            
        content_str = base64.b64decode(file_content['content']).decode('utf-8')
        
        if len(content_str.split('\n')) > Config.MAX_LINES:
            return "Skipped: File contains more than 500 lines."
            
        return content_str