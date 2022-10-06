#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import argparse

import function_loader
from changers import *

if __name__ == "__main__":
    func_loader = function_loader.FunctionStorage()
    commands_description = 'Can be choosed one of:'
    for command in func_loader.get_commands_visable_data():
        commands_description += "\n\t" + command

    parser = argparse.ArgumentParser(description='Clie version of text_changer.',
        formatter_class=argparse.RawDescriptionHelpFormatter, epilog=commands_description)
    parser.add_argument('-c', '--command', dest='command',
                        help='Command for text treatment. ')
    args = parser.parse_args()

    if 3 <= sys.version_info.major:
        geted_str = input()
    else:
        geted_str = raw_input()

    function = func_loader.find_command_by_key(args.command)
    print (function(geted_str))