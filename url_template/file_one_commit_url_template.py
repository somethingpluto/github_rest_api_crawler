

class FileOneCommitUrlTemplate:
    def __init__(self,repo_owner:str,repo_name:str,file_path:str,sha:str):
        self.base_url = "https://api.github.com/repos"
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.sha = sha
        self.file_path  = file_path
        self._full_request_url = self.base_url+f"/{self.repo_owner}/{self.repo_name}/contents/{self.file_path}?ref={self.sha}"
    
    def url(self):
        return self._full_request_url