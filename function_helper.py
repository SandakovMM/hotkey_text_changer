#!/usr/bin/python3
# -*- coding: utf-8 -*-

def arguments_not_none():
    def decorate(wrapped):
        def _wrapper(*args, **kwargs):
            for arg in args:
                if arg is None:
                    return None
            return wrapped(*args, **kwargs)
        return _wrapper
    return decorate