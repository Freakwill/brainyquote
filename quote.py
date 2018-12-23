#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib
from pybrainyquote import Quote


_HomePath = pathlib.Path('~').expanduser()
_WidgetPath = _HomePath / 'Library/Application Support/Übersicht/widgets/brainyquote'

topic = None  # set topic what you want, e.g. love, health

try:
    if topic:
        print(Quote.random(topic).toHTML())
    else:
        print(Quote.today().toHTML())
except Exception as e:
    quote = Quote.choice_yaml(_WidgetPath / 'quotes.yaml')
    print(quote.toHTML())
