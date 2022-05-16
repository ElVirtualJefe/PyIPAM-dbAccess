
print("Loading app...")

import app


# -*- encoding: utf-8 -*-
'''
Copyright (c) 2021 - ElVirtualJefe
'''

from re import match
import sys

if len(sys.argv) > 1:
    for i,arg in enumerate(sys.argv):
        if i == 0:
            continue
        match arg:
            case "dbAccess":
                app.serve('dbAccess')
            case _:
                print(f"No such option found: {arg}")

#scanAgent()

