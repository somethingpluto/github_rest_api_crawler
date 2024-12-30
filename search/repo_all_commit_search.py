from model.repo_one_commit_info import RepoOneCommitInfoModel


def search_repo_all_commit(context:dict, url:str, record_data:dict):
    """获取仓库的所有commit信息

    Args:
        context (dict): 上下文对象
        url (str): 请求url
        record_data (dict): 数据存储字典
    """
    commit_info_list = record_data['repo_all_commit_info_list']
    client = context.get('context')
    header = context.get('header')
    while True:
        print(f"获取仓库所有commit信息:{url}")
        repo_all_commit_response = client.get(url, headers=header)
        repo_all_commit_data = repo_all_commit_response.json()
        if isinstance(repo_all_commit_data, list):
            for commit in repo_all_commit_data:
                repo_one_commit_info_data = RepoOneCommitInfoModel(**commit)
                commit_info_list.append(repo_one_commit_info_data)
        elif isinstance(repo_all_commit_data, dict):
            for commit in repo_all_commit_data['items']:
                repo_one_commit_info_data = RepoOneCommitInfoModel(**commit)
                commit_info_list.append(repo_one_commit_info_data)
        link = str(repo_all_commit_response.headers.get('link', None))
        if link is not None:
            larr = link.split(",")[0]
            if "next" in larr:
                next_url = larr.split("; ")[0].replace("b'<", "").replace(">", "").replace("<", "")
                url = next_url
            else:
                break
        else:
            break