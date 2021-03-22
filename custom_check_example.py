#!/usr/bin/env python
"""
This is an example of how to extend the default environment
and/or loader to add your own filter logic.
"""
import jinja2

from j2lint import AbsolutePathLoader, main

FILTER = ["to_nice_json"]

ENV = jinja2.Environment(loader=AbsolutePathLoader())
ENV.filters.update({name: lambda: None for name in FILTER})

main(env=ENV)
