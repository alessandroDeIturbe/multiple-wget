import requests
import os
import sys

currentdir = os.getcwd()
os.chdir(currentdir)

urls = []

while True:
    url = input('Insert the download link (leave empty to start the download): ')
    
    if url == '':
        break

    urls.append(url)
    
print('Start downloading the file/s')
for u in urls:
    print('Downloading: %s' % u)
    file_name = input('Enter the file name (with extension): ')
    
    with open(file_name, 'wb') as f:
        r = requests.get(u, allow_redirects=True, stream=True)
        total_length = r.headers.get('content-length')

        if total_length is None:
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
