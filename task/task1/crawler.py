import argparse
from http import client
import json
from multiprocessing import context
from tqdm import tqdm
from search.file_all_commit_search import search_file_all_commit
from search.repo_all_commit_search import search_repo_all_commit
from search.repo_search import search_repo_detail_info
from url_template.file_commit_url_template import FileCommitUrlTemplate
from url_template.repo_commit_url_template import RepoCommitUrlTemplate
from url_template.repo_url_template import RepoUrlTemplate
from utils.requests_client import HttpClient




def parse_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-f', type=str, help='language url file', required=True)
    parser.add_argument('-t', type=str, help='github access token', required=True)
    parser.add_argument('-o', type=str, help="output json_data path", required=True)
    parser.add_argument('-l', type=str, help="language", required=True)
    args = parser.parse_args()
    return args

def prepare_context(args):
    headers = {
        'Accept': 'application/vnd.github.text-match+json',
        'Authorization': f'Bearer {args.t}',
        'X-GitHub-Api-Version': '2022-11-28'
    }
    client = HttpClient(retries=5,headers=headers)
    return {
        "client":client,
        "headers":headers,
        "file_info":{}
    }

if __name__ == '__main__':
    args = parse_args()
    context = prepare_context(args=args)
    client = context.get('client')
    file_info = context.get('file_info')
    # 读取url配置文件
    with open(args.f, "r", encoding="utf8") as file:
        url_lines = file.readlines()
        url_list = [line.strip() for line in url_lines]
    # 遍历每一页数据
    with tqdm(desc="Processing items", unit="item", total=len(url_list) * 100) as pbar:
        for url in url_list:
            response = client.get(url)
            if response.status_code == 422:
                break
            elif response.status_code == 200:
                resp_data = response.json()
                print(resp_data)
                for index, item in enumerate(resp_data['items']):
                    try:
                        record_data = {}
                        print(f"获取仓库概要信息:{url}")
                        repo_info = item['repository']
                        # 1.获取仓库名称
                        file_info['repo_name'] = repo_info.get('name', '')
                        # 2.获取仓库作者名称
                        file_info['repo_owner'] = repo_info['owner']['login']
                        # 3.获取文件地址
                        file_info['file_path'] = item.get('path')
                        # 获取仓库信息
                        repo_info_url = RepoUrlTemplate(repo_full_name=file_info['repo_owner']+"/"+file_info['repo_name']).url()
                        search_repo_detail_info(context=context, url=repo_info_url,record_data=record_data)
                        print("仓库信息获取完毕")
                        # 获取仓库所有commit
                        repo_all_commit_url = RepoCommitUrlTemplate(repo_owner=file_info['repo_owner'],repo_name=file_info['repo_name']).url()
                        record_data['repo_all_commit_info_list'] = []
                        search_repo_all_commit(context=context, url=repo_all_commit_url, record_data=record_data)
                        print("仓库commit信息获取完毕")

                        # 获取某个文件的所有commit信息
                        file_commit_url = FileCommitUrlTemplate(repo_owner=file_info['repo_owner'],repo_name=file_info['repo_name'],file_path=file_info['file_path'])
                        record_data['file_all_commit_info_list'] = []
                        search_file_all_commit(context=context, url=file_commit_url, record_data=record_data)
                        print("文件commit信息获取完毕")
                        # 将得到的item信息写入jsonl文件
                        with open(args.o, "a+", encoding='utf8') as file:
                            json_str = json.dumps(record_data, ensure_ascii=False)
                            file.write(json_str + "\n" + "")
                            file.flush()
                    except Exception:
                        with open(f"./url/{args.l}_failed.txt", "a+", encoding="utf8") as file:
                            file.write(f"{url}#{index}\n")
                    with open(f"./url/{args.l}_success.txt", "a+", encoding='utf8') as file:
                        file.write(f"{url}#{index}\n")
                        file.flush()
                    print("=======================================")
                    pbar.update(1)
