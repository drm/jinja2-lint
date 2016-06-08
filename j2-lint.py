"""
@author Gerard van Helden <gerard@zicht.nl>
@license DBAD, see <http://www.dbad-license.org/>

Simple j2 linter, useful for checking jinja2 template syntax
"""
import jinja2
import os.path
from functools import reduce


class AbsolutePathLoader(jinja2.BaseLoader):
    def get_source(self, environment, path):
        if not os.path.exists(path):
            raise jinja2.TemplateNotFound(path)
        mtime = os.path.getmtime(path)
        with open(path) as f:
            source = f.read()
        return source, path, lambda: mtime == os.path.getmtime(path)


def check(template, out, err):
    env = jinja2.Environment(loader=AbsolutePathLoader())

    try:
        env.get_template(template)
        out.write("%s: Syntax OK\n" % template)
        return 0
    except jinja2.TemplateNotFound:
        err.write("%s: File not found\n" % template)
        return 2
    except jinja2.exceptions.TemplateSyntaxError as e:
        err.write("%s: Syntax check failed: %s in %s at %d\n" % (template, e.message, e.filename, e.lineno))
        return 1


if __name__ == "__main__":
    import sys

    try:
        sys.exit(reduce(lambda r, fn: r + check(fn, sys.stdout, sys.stderr), sys.argv[1:], 0))
    except IndexError:
        sys.stdout.write("Usage: j2-lint.py filename [filename ...]\n")
