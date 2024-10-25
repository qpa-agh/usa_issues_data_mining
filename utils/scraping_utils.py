import concurrent.futures
import requests
from bs4 import BeautifulSoup
import concurrent

session = requests.Session()
def get_html(url):
    response = session.get(url)
    if response.ok:
        return BeautifulSoup(response.content, features="lxml")
    return None

def parrarelize_processes(function, args_list, n_executors=5):
    assert n_executors < 30
    with concurrent.futures.ProcessPoolExecutor(max_workers=min(n_executors, len(args_list))) as executor:
        future_to_id = {executor.submit(function, *args): id for id, args in enumerate(args_list)}
        for future in concurrent.futures.as_completed(future_to_id):
            id = future_to_id[future]
            yield (id, future.result())
            del future_to_id[future]

def parrarelize_threads(function, args_list, n_executors=100):
    assert n_executors < 300
    with concurrent.futures.ThreadPoolExecutor(max_workers=min(n_executors, len(args_list))) as executor:
        future_to_id = {executor.submit(function, *args): id for id, args in enumerate(args_list)}
        for future in concurrent.futures.as_completed(future_to_id):
            id = future_to_id[future]
            yield (id, future.result())
            del future_to_id[future]
