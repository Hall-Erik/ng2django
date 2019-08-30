import argparse
import os
import sys

my_parser = argparse.ArgumentParser(
    prog='ng2django',
    description='Convert an Angular2+ generated HTML file to Django Template Language')

my_parser.add_argument(
    'Path',
    metavar='path',
    type=str,
    help='the path to the list')

my_parser.add_argument(
    '-n',
    '--nodelete',
    action='store_true',
    help='do not delete the original file')

my_parser.add_argument(
    '-p',
    '--pretty',
    action='store_true',
    help='do not uglify the output file')

args = my_parser.parse_args()

input_path = args.Path

if not os.path.isdir(input_path):
    print('The specified path does not exist')
    sys.exit()

print(args.pretty)

print('\n'.join(os.listdir(input_path)))