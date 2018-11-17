#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pybrainyquote

try:
    # raise "for test"
    quote = pybrainyquote.Quote.today()
    print(quote)
except:
    import random
    import yaml

    with open('quotes.yaml', encoding='utf-8') as fo:
        s = fo.read()
    quotes = yaml.load(s)
    print(random.choice(quotes))
