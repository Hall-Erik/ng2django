from bs4 import BeautifulSoup
import argparse
import os
import sys

def main():
    parser = argparse.ArgumentParser(
        prog='ng2django',
        description='Convert an Angular2+ generated HTML'
        ' file to Django Template Language')

    parser.add_argument(
        'source',
        metavar='source',
        type=str,
        help='path to the Angular2+ generated HTML file')

    parser.add_argument(
        'dest',
        metavar='dest',
        type=str,
        help='path to the output Django Template file')

    parser.add_argument(
        '-s',
        '--subdir',
        type=str,
        help='subdirectory inside your Django static directory'
        ' to your Angular built files'
        ' (e.g. static/<subdir>/runtime-es2015.blahblah.js)',
        required=False
    )

    parser.add_argument(
        '-js',
        '--jsdir',
        type=str,
        help='subdirectory if you have your .js files in js dir.'
             ' (e.g. static/<optional-subdir>/<js>/runtime-es2015.js)',
        required=False
    )

    parser.add_argument(
        '-css',
        '--cssdir',
        type=str,
        help='subdirectory if you have your .css files in css dir.'
             ' (e.g. static/<optional-subdir>/<css>/style.css)',
        required=False
    )

    parser.add_argument(
        '-img',
        '--imgdir',
        type=str,
        help='subdirectory if you have your image files in e.g. img/image dir.'
             ' (e.g. static/<optional-subdir>/<img>/img.png)',
        required=False
    )

    parser.add_argument(
        '-n',
        '--nodelete',
        action='store_true',
        help='do not delete the original file')

    parser.add_argument(
        '-p',
        '--pretty',
        action='store_true',
        help='more readable output file')

    args = parser.parse_args()

    source_path = args.source
    dest_path = args.dest
    sub_path = args.subdir
    js_path = args.jsdir
    css_path = args.cssdir
    img_path = args.imgdir

    if not os.path.isfile(source_path):
        print('The specified source file does not exist')
        sys.exit()

    if sub_path:
        if sub_path[-1] != '/':
            sub_path = sub_path + '/'
    else:
        sub_path = ''

    if js_path:
        if js_path[-1] != '/':
            js_path = js_path + '/'
    else:
        js_path = ''

    if css_path:
        if css_path[-1] != '/':
            css_path = css_path + '/'
    else:
        css_path = ''

    if img_path:
        if img_path[-1] != '/':
            img_path = img_path + '/'
    else:
        img_path = ''

    with open(source_path) as index:
        soup = BeautifulSoup(index, 'html.parser')

    for el in soup.find_all('link'):
        if el.get("href") and el.get("href")[0:4] != "http":
            if el['href'].endswith('.css'):
                el['href'] = f'{{% static "{sub_path}{css_path}{el.get("href")}" %}}'
            else:
                if el['href'].lower().endswith(('ico', '.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
                    el['href'] = f'{{% static "{sub_path}{img_path}{el.get("href")}" %}}'

    for el in soup.find_all('script'):
        if el.get("src") and el.get("src")[0:4] != "http":
            el['src'] = f'{{% static "{sub_path}{js_path}{el.get("src")}" %}}'
            del el['nomodule']
            el['type'] = 'text/javascript'

    soup.insert(1,'{% load static %}')

    if args.pretty:
        output = soup.prettify('utf-8')
    else:
        output = soup.encode('utf-8')

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, 'wb') as f:
        f.write(output)

    if not args.nodelete:
        os.remove(source_path)
