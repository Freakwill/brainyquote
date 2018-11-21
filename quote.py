#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib
import pybrainyquote


_HomePath = pathlib.Path('~').expanduser()
_WidgetPath = _HomePath / 'Library/Application Support/Übersicht/widgets/brainyquote'

topic = None  # set topic what you want, for example love, health

try:
    # raise "for test"
    if topic:
        quote = pybrainyquote.Quote.random(topic)
        print(quote.toHTML())
    else:
        quote = pybrainyquote.Quote.today()
        print(quote.toHTML())

except:
    import random
    import yaml

    with open(_WidgetPath / 'quotes.yaml', encoding='utf-8') as fo:
        s = fo.read()
    quotes = yaml.load(s)
    print(random.choice(quotes).toHTML())
