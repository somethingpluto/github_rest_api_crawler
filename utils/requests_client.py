import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class HttpClient:
    def __init__(self, retries=3, backoff_factor=0.3, proxy=None, headers=None):
        # 初始化请求客户端配置
        self.session = requests.Session()

        # 设置重试机制
        retry = Retry(
            total=retries,  # 最大重试次数
            backoff_factor=backoff_factor,  # 退避因子
        )

        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

        # 设置代理
        if proxy:
            self.session.proxies.update(proxy)

        # 设置请求头
        if headers:
            self.session.headers.update(headers)

    def get(self, url, params=None):
        try:
            response = self.session.get(url, params=params, timeout=10)  # 设置请求超时时间
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None

    def post(self, url, data=None, json=None):
        try:
            response = self.session.post(url, data=data, json=json, timeout=10)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None
