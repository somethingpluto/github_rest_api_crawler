import base64
from model.file_one_commit_info import FileOneCommitInfoModel


def search_file_commit_detail_info(context:dict, url:str, record_data:dict):
    """获取文件的一次commit详细信息

    Args:
        context (dict): 上下文对象
        url (str): 请求url
        record_data (dict): 数据记录字典
    """
    client = context.get('client') 
    headers = context.get('headers')
    detail_response = client.get(url, headers=headers)
    detail_data = detail_response.json()

    file_one_commit_info_data = FileOneCommitInfoModel(**detail_data)
    file_one_commit_info_data.content =decode_base64_content(file_one_commit_info_data.content)
    record_data['detail_info'] = file_one_commit_info_data

def decode_base64_content(content):
    utf8_line_arr = []
    base64_lines = content.split("\n")

    for line in base64_lines:
        try:
            decoded_bytes = base64.b64decode(line)
            decoded_string = decoded_bytes.decode('utf-8')
            utf8_line_arr.append(decoded_string)
        except Exception:
            utf8_line_arr.append("")
    combined_string = "\n".join(utf8_line_arr)
    return combined_string
