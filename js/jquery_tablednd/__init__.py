# -*- coding: utf-8 -*-

"""
Created on 2013-02-22
"""

from fanstatic import Library
from fanstatic import Resource
from js.jquery import jquery

library = Library(
    'jquery_tablednd',
    'resources'
    )
jquery_tablednd = Resource(
    library,
    'jquery.tablednd.js',
    minified='jquery.tablednd.min.js',
    depends=[jquery, ]
    )
