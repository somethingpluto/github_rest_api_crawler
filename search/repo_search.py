from model.repo_info import RepoInfoModel


def search_repo_detail_info(context:dict, url:str,record_data:dict):
    """根据url 获取github 仓库全部信息

    Args:
        context (dict): 上下文对象
        url (str): 请求url
        record_data (dict): 数据记录字典
    """
    print(f"获取仓库信息:{url}")
    client = context.get('client')
    repo_response = client.get(url, headers=context['header'])
    repo_response = repo_response.json()
    repo_info = RepoInfoModel(**repo_response)
    record_data["repo_info"]=repo_info