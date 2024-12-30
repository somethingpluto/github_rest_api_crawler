class RepoCommitUrlTemplate:
    """分页获取仓库的commit请求 url构造器
    """
    def __init__(self,repo_owner,repo_name,per_page=100,page=1):
        self.base_url = "https://api.github.com/repos"
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.per_page= per_page
        self.page = page
        self._full_request_url = self.base_url+f"/{self.repo_owner}/{self.repo_name}/commits?per_page={self.per_page}&page={self.page}"
    
    def url(self):
        """
        docstring
        """
        return self._full_request_url