#!/usr/bin/env python3
import argparse
from gendiff.engine import generate_diff
import os


def get_path(file_name):
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, 'fixtures', file_name)


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str,
                        default='stylish',
                        help='set format of output')
    args = parser.parse_args()
    print(generate_diff(get_path(args.first_file),
                        get_path(args.second_file), args.format))


if __name__ == '__main__':
    main()
