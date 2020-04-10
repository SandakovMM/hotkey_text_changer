#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import argparse

import function_loader
from changers import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Clie version of text_changer.')
    parser.add_argument('-c', '--command', dest='command',
                        help='command for text treatment')
    args = parser.parse_args()

    if 3 <= sys.version_info.major:
        geted_str = input()
    else:
        geted_str = raw_input()

    func_loader = function_loader.FunctionStorage()
    function = func_loader.find_command_by_key(args.command)
    print (function(geted_str))