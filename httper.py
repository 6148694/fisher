import requests

class HTTP:
    @staticmethod   #静态方法   不需要用self
    def get(url,return_json=True):
        r = requests.get(url)
        if r.status_code !=200:
            return  {} if return_json  else ""
        return r.json() if return_json else r.text


if __name__ == '__main__':
    pass