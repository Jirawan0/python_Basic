"""
# Part: Python PIP
#
"""

# pip list
# python.exe -m pin install --upgrade pip
# pip install camelcase
# pip uninstall camelcase

import cachetools
camel = cachetools.CamelCase()
txt = "hello world"
print(camel.hump(txt))