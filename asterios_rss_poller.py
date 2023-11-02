#!/usr/bin/env python3

from flask import Flask
import xml.etree.ElementTree as ET
import requests
import sys
import time

app = Flask(__name__,)

MAX_ATTEMPTS = 10
RETRY_DELAY_SEC = 5

DEFAULT_PORT = 8080
port = DEFAULT_PORT

rss_url = None

@app.route("/<lookup_srings_csv>")
def get_rss_filtered(lookup_srings_csv):
    if 'favicon.ico' in lookup_srings_csv:
        return 'n/a'

    lookup_srings = list(map(lambda s: s.strip().lower(), lookup_srings_csv.split(',')))

    root = None
    attempt = 1
    
    while attempt <= MAX_ATTEMPTS:
        try:
            res = requests.get(rss_url)

            root = ET.fromstring(res.content)
            break
        except Exception as e:
            print('request try #{} failed'.format(attempt))
            attempt += 1
            time.sleep(RETRY_DELAY_SEC)
        
    if root == None:
        err_msg = 'error parsing RSS feed URL. Probably bad URL or server is down'
        print(err_msg)
        
        return err_msg, 500
    
    channel = root.find('channel')

    items_to_delete = []
    for item in channel.iter('item'):
        item_title = item.find('title').text.lower()

        item_matches = False

        for lookup_sring in lookup_srings:
            if lookup_sring in item_title:
                item_matches = True
                
                break
        
        if not item_matches:
            items_to_delete.append(item)

    for item in items_to_delete:
        channel.remove(item)
        
    return ET.tostring(root, encoding='utf8'), {"Content-type": "text/xml"}

if __name__ == '__main__':
    program_name = sys.argv[0]
    
    if program_name.endswith('py'):
        program_name = 'python ' + program_name
    
    if len(sys.argv) not in [2, 3] or sys.argv[1] in ['help', '-help', '--help', '?']:
        print('usage: ')
        print('       {} "<URL>"'.format(program_name))
        print('       {} "<URL>" <PORT>'.format(program_name))
        print('')
        print('Find URL of RSS feed for your server:')
        print('1. open this in browser: https://asterios.tm/index.php?cmd=rss&serv=0')
        print('2. select your server on that web page (x5, x7 etc), take URL from browser address bar and add trailing &out=xml')
        print('3. use resulting URL as an argument for this program (use quotes). Like this:')
        print('{} "https://asterios.tm/index.php?cmd=rss&serv=0&out=xml"'.format(program_name))
        print('')
        print('Найдите URL ленты RSS для вашего сервера:')
        print('1. откройте эту ссылку в браузере: https://asterios.tm/index.php?cmd=rss&serv=0')
        print('2. выберите ваш сервер на открывшейся странице (x5, x7 итп), возьмите URL из адресной строки браузера и добавьте в конец &out=xml')
        print('3. используйте получившийся URL в качестве аргумента к данной программе (используйте кавычки). Вот так:')
        print('{} "https://asterios.tm/index.php?cmd=rss&serv=0&out=xml"'.format(program_name))

        sys.exit(0)
    
    if len(sys.argv) == 3:
        port = sys.argv[2]
    
    rss_url = sys.argv[1]

    app.run(host='0.0.0.0', port=port)
