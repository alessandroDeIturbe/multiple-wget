import requests
import os
import sys

currentdir = os.getcwd()
os.chdir(currentdir)

files = {}

while True:
    url = input('Insert the download link (leave empty to start the download): ')
    if url == '':
        break
    name = ''
    while name == '':
        name = input('Insert the name of the file: ')
        if os.path.exists(name):
            print('File already exists!')
            name = ''
        else:
            break
    
    files[name] = {'url': url, 'name': name}

print('Start downloading...')
for key, value in files.items():
    
    with open(value['name'], 'wb') as f:
        print('Downloading: ' + value['name'])
        r = requests.get(value['url'], stream=True, allow_redirects=True)
        total_length = r.headers.get('content-length')

        if total_length is None: # no content length header
            f.write(r.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in r.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                done = int(50 * dl / total_length)
                sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)))
                sys.stdout.flush()
