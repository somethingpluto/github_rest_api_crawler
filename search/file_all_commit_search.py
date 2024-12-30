from model.file_commit_list_item_model import FileCommitListItemModel
from search.file_one_commit_search import search_file_commit_detail_info
from url_template.file_one_commit_url_template import FileOneCommitUrlTemplate


def search_file_all_commit(context:dict, url:str, record_data:dict, file_path:str):
    """获取文件的所有commit信息

    Args:
        context (dict): 上下文对象
        url (str): 请求url
        record_data (dict): 数据记录字典
        file_path (str): 文件路径
    """
    commit_info_list= record_data['file_all_commit_info_list']
    client = context.get('client')
    headers = context.get('headers')
    file_info = context.get('file_info')
    while True:
        print(f"获取{file_path}的所有commit信息{url}")
        file_commit_resp = client.get(url, headers=headers)
        file_commit_data = file_commit_resp.json()
        if isinstance(file_commit_data, list):
            for commit in file_commit_data:
                temp_dict = {
                    "basic_info":None,
                    "detail_info":None
                }
                detail_url = FileOneCommitUrlTemplate(repo_owner=file_info['file_info'],repo_name=file_info['file_name'],file_path=file_info['file_path'],sha=commit['sha'])
                temp_dict['basic_info'] =FileCommitListItemModel(**commit)
                search_file_commit_detail_info(context=context, url=detail_url, record_data=temp_dict)
                commit_info_list.append()
        elif isinstance(file_commit_data, dict):
            for commit in file_commit_data['items']:
                temp_dict = {
                    "basic_info":None,
                    "detail_info":None
                }
                detail_url = FileOneCommitUrlTemplate(repo_owner=file_info['file_info'],repo_name=file_info['file_name'],file_path=file_info['file_path'],sha=commit['sha'])
                temp_dict['basic_info'] =FileCommitListItemModel(**commit)
                search_file_commit_detail_info(context=context, url=detail_url, temp_dict=temp_dict)
                commit_info_list.append(temp_dict)
        link = str(file_commit_resp.headers.get('link', None))
        print(link)
        if link is not None:
            larr = link.split(",")[0]
            if "next" in larr:
                next_url = larr.split("; ")[0].replace("b'<", "").replace(">", "").replace("<", "")
                url = next_url
            else:
                break
        else:
            break