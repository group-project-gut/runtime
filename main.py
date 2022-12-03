#!/usr/bin/env python3

# Main entrypoint of runtime microservice

import argparse

from src.runtime import Runtime


parser = argparse.ArgumentParser(
    prog='lynx-Runtime',
    description='Create game environment and run users code in it',
    epilog='Owner: blazej.smorawski@gmail.com')
parser.add_argument('code_file_path')
parser.add_argument('--interactive', '-i', action='store_true')

args = parser.parse_args()

if __name__ == '__main__':
    runtime = Runtime(args.code_file_path, args.interactive)
    runtime.run()
