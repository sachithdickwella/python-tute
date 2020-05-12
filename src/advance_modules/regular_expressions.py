#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 
# https://docs.python.org/3/library/re.html

import re

pattern = ['term1', 'term2']
text = 'This is a string with term1, but not other term.'

match = re.search('hello', 'hello world')
print(match)

match = re.search(pattern[0], text)
print(type(match))
print(match)
print(f'Match start: {match.start()}, match end: {match.end()}')

# Regex important.

split_term = '@'
phrase = 'What is your email, is it sachith_prasanna@live.com?'

r = re.split(split_term, phrase)
print(r)

r = re.findall('match', "Here's a first match and here's the second match")
print(r)
