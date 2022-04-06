import requests
import sys
import os

'''
   Este código foi retirado de
   https://sumit-ghosh.com/articles/python-download-progress-bar/
'''
#TODO: tratar: requests.exceptions.InvalidURL
def download(url, filename):
    with open(filename, 'wb') as f:
        response = requests.get(url, stream=True)
        total = response.headers.get('content-length')

        if total is None:
            f.write(response.content)
        else:
            downloaded = 0
            total = int(total)
            for data in response.iter_content(chunk_size=max(int(total/1000), 1024*1024)):
                downloaded += len(data)
                f.write(data)
                done = int(50*downloaded/total)
                sys.stdout.write('\r[{}{}]'.format('█' * done, '.' * (50-done)))
                sys.stdout.flush()
    sys.stdout.write('\n')

def check_download_size(url):
    response = requests.get(url, stream=True)
    total = response.headers.get('content-length')
    
    return int(total)


def compare_files_size(url, file_path):
    remote_file_size = check_download_size(url)
    local_file_size = os.path.getsize(file)

    return remote_file_size == local_file_size


