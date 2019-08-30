import argparse
import os
import sys

parser = argparse.ArgumentParser(
    prog='ng2django',
    description='Convert an Angular2+ generated HTML file to Django Template Language')

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
    '-n',
    '--nodelete',
    action='store_true',
    help='do not delete the original file')

parser.add_argument(
    '-p',
    '--pretty',
    action='store_true',
    help='do not uglify the output file')

args = parser.parse_args()

source_path = args.source
dest_path = args.dest

if not os.path.isfile(source_path):
    print('The specified source file does not exist')
    sys.exit()

print(args.pretty)
