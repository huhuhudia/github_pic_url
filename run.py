import requests
import os
from requests.auth import HTTPBasicAuth
import json
from datetime import datetime
import time
from multiprocessing import Process
username = os.environ.get('github_username')
password = os.environ.get('github_password')
reponame = os.environ.get('github_repo')
local_repo_path = os.environ.get('local_repo_path')
repo_url =  "https://api.github.com/repos/%s/%s/contents"%(username,reponame)
print(repo_url)
urls_old = []
urls_new = {}
def ask_for_newpic():
    global urls_old
    global urls_new
    r = requests.get(repo_url, auth=HTTPBasicAuth(username, password))
    content = r.json()
   
    mark_time = datetime.now()
    for item in content:
        pic_url = item['download_url']
        if pic_url not in urls_new:
            urls_old.append(pic_url)
            urls_new[pic_url] = datetime.now()

    for url in urls_new:
        if urls_new[url] > mark_time :
            print('[+] url: ', url, " "*5,"/%s/"%urls_new[url])

# file_count = len(os.listdir(local_repo_path))

# def listening_local_repo(path,file_count):
    
#     while True:
#         cur_files = len(os.listdir(local_repo_path))
#         if cur_files != file_count:
#             file_count = cur_files
#             os.chdir(path)
#             os.system('git add .')
#             os.system('git commit -m "auto save"')
#             os.system('git push ')

#         time.sleep(6)
# listening_process = Process(target=listening_local_repo, args=(local_repo_path,file_count))
# listening_process.start()

while True:
    time.sleep(1)
    ask_for_newpic()
    