#!/usr/bin/env python
"""
This is an example of how to extend the default environment
and/or loader to add your own filter logic.
"""
import jinja2
from j2lint import main, AbsolutePathLoader

filters = ['to_nice_json']

env = jinja2.Environment(loader=AbsolutePathLoader())
env.filters.update({name: lambda: None for name in filters})

main(env=env)
