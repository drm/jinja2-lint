#!/usr/bin/env python
"""
@author Gerard van Helden <drm@melp.nl>
@license DBAD, see <http://www.dbad-license.org/>

Simple j2 linter, useful for checking jinja2 template syntax
"""
from jinja2 import BaseLoader, TemplateNotFound, Environment, exceptions
import os.path
from functools import reduce


class AbsolutePathLoader(BaseLoader):
    def get_source(self, environment, path):
        if not os.path.exists(path):
            raise TemplateNotFound(path)
        mtime = os.path.getmtime(path)
        with open(path) as f:
            source = f.read().decode('utf-8')
        return source, path, lambda: mtime == os.path.getmtime(path)


def check(template, out, err, env=Environment(loader=AbsolutePathLoader())):
    try:
        env.get_template(template)
        out.write("%s: Syntax OK\n" % template)
        return 0
    except TemplateNotFound:
        err.write("%s: File not found\n" % template)
        return 2
    except exceptions.TemplateSyntaxError as e:
        err.write("%s: Syntax check failed: %s in %s at %d\n" % (template, e.message, e.filename, e.lineno))
        return 1

def main(**kwargs):
    import sys
    try:
        sys.exit(reduce(lambda r, fn: r + check(fn, sys.stdout, sys.stderr, **kwargs), sys.argv[1:], 0))
    except IndexError:
        sys.stdout.write("Usage: j2lint.py filename [filename ...]\n")

if __name__ == "__main__":
    main()

