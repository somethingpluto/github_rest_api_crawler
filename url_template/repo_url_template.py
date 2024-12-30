class RepoUrlTemplate:
    def __init__(self,repo_full_name):
        self.base_url = "https://api.github.com/repos/"
        self.repo_full_name = repo_full_name
        self.full_request_url = self.base_url+self.repo_full_name
    
    def url(self):
        return self.full_request_url
