#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def func():
    print('FUNC() in ONE.PY')

print('TOP LEVEL IN ONE.PY')

if __name__ == '__main__':
    print('ONE.PY is being run DIRECTLY!')
else:
    print('ONE.PY has been imported')