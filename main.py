#!/usr/bin/env python3

# Main entrypoint of runtime microservice

from src.runtime import Runtime
import argparse

parser = argparse.ArgumentParser(
                    prog = 'LNX-Runtime',
                    description = 'Create game environment and run users code in it',
                    epilog = 'Owner: blazej.smorawski@gmail.com')
parser.add_argument('code_file_path')

args = parser.parse_args()    

if __name__ == '__main__':
     with open(args.code_file_path, 'r') as code_file:
          code = code_file.read()
          runtime = Runtime(code)
          runtime.run()