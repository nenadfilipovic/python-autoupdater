import os
import gc
import time
import requests

github_url = ''
directory = 'project_root'


def http_request(url):
    headers = {
        'User-Agent': 'My User Agent 1.0',
        'Content-Type': 'application/json',
    }
    response = requests.get(url, headers=headers)
    return response


def parser(main_url):
    main_url = main_url.rstrip('/').replace('https://github.com', 'https://api.github.com/repos')
    return main_url


def remove(root):
    for root, dirs, files in os.walk(root, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
            print("| Removing... ", os.path.join(root, name))
            time.sleep(1)
        for name in dirs:
            os.rmdir(os.path.join(root, name))
            print("| Removing... ", os.path.join(root, name))
            time.sleep(1)
    os.rmdir(root)
    print("| Removing... ", root)
    time.sleep(1)


def version(directory):
    print("| Checking versions...")
    time.sleep(1)
    remote_version = http_request(parser(github_url) + '/releases/latest').json()['tag_name']
    print("| Remote version... ", remote_version)
    time.sleep(1)
    if '.version' in os.listdir(directory):
        with open(directory + '/.version', 'r') as version_file:
            local_version = version_file.read()
            version_file.close()
            print("| Local version... ", local_version)
            time.sleep(1)
            if remote_version > local_version:
                print("| Update is available...")
                time.sleep(1)
                print("| Preparing to download update...")
                os.mkdir('project_root_update')
                with open('project_root_update/.version', 'w') as version_file:
                    version_file.write(remote_version)
                    version_file.close()
                get(parser(github_url + '/contents/'), remote_version)
                remove(directory)
                os.rename('project_root_update', directory)
                print("| Finishing applying update...")
            else:
                print("| No update available.")
                print("| Booting your project...")
                time.sleep(1)
    else:
        print("| Local version file doesn't exist.")
        print("| Do you want to create version file yourself? (Yes or No)")
        user_input = input()
        if user_input == 'Yes':
            print("| Enter version value: ")
            user_input = input()
            with open(directory + '/.version', 'w') as version_file:
                version_file.write(user_input)
                version_file.close()
        else:
            print("| Quiting...")
            quit()


def get(main_url, remote_version):
    response = http_request(main_url + '?ref=refs/tags/' + remote_version)
    for item in response.json():
        if item['type'] == 'file':
            download_url = item['download_url']
            download_path = 'project_root_update/' + item['path']
            download(download_url.replace('refs/tags/', ''), download_path)
        elif item['type'] == 'dir':
            directory = 'project_root_update/' + item['path']
            print("| Creating directory... ", directory)
            os.mkdir(directory)
            get(main_url + '/' + item['name'] + '/', remote_version)


def download(download_url, download_path):
    print("| Downloading... ", download_path)
    with open(download_path, 'w') as download_file:
        try:
            response = http_request(download_url)
            download_file.write(response.text)
        finally:
            response.close()
            download_file.close()
            gc.collect()


def boot():
    version(directory)
    print("OK")


boot()
