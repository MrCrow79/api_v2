import requests

server = 'dev'

bo_part_url = 'https://{0}'.format(server)
values_for_cookie_aspxauth = ""


# helper funcs
def send_request(api_instance):
    cookie = get_cookies()
    headers = {'Content-Type': 'application/json', 'Cookie': cookie}
    url = bo_part_url + api_instance.full_url
    if api_instance.type.lower() == 'get':
        request = requests.get(url=url, headers=headers)
    elif api_instance.type.lower() in ('post', 'put'):
        request = requests.get(url=url, headers=headers, data=str(api_instance.data))
    elif api_instance.type.lower() == 'delete':
        pass

    return request


def get_cookies():
    """
    Func for set get and set cookies
    """
    pass

