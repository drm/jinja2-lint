#!/usr/bin/env python3
"""
@author Gerard van Helden <drm@melp.nl>
@license DBAD, see <http://www.dbad-license.org/>

Simple j2 linter, useful for checking jinja2 template syntax
"""
import argparse
import os.path
import sys
from functools import reduce

from jinja2 import BaseLoader, Environment, TemplateNotFound, exceptions


class AbsolutePathLoader(BaseLoader):
    def get_source(self, environment, template):
        if not os.path.exists(template):
            raise TemplateNotFound(template)
        mtime = os.path.getmtime(template)
        with open(template) as file:
            source = file.read()
        return source, template, lambda: mtime == os.path.getmtime(template)


env = Environment(
    loader=AbsolutePathLoader(),
    extensions=["jinja2.ext.i18n", "jinja2.ext.do", "jinja2.ext.loopcontrols"],
)


def check(
    template,
    out,
    err,
):
    try:
        env.get_template(template)
        if not args.quiet:
            out.write("%s: Syntax OK\n" % template)
        return 0
    except TemplateNotFound:
        err.write("%s: File not found\n" % template)
        return 2
    except exceptions.TemplateSyntaxError as ex:
        err.write(
            "%s: Syntax check failed: %s in %s at %d\n"
            % (template, ex.message, ex.filename, ex.lineno)
        )
        return 1


def main(**kwargs):
    global args
    parser = argparse.ArgumentParser(description="Lint jinja files")
    parser.add_argument("--quiet", action="store_true", help="Only print errors")
    parser.add_argument(
        "--filter",
        metavar="filter",
        type=str,
        nargs="+",
        help="Add custom jinja filter",
    )
    parser.add_argument(
        "files", metavar="file", type=str, nargs="+", help="the files to lint"
    )
    args = parser.parse_args()
    if args.filter:
        env.filters.update({name: lambda: None for name in args.filter})
    try:
        status_code = reduce(
            lambda r, fn: r + check(fn, sys.stdout, sys.stderr, **kwargs), args.files, 0
        )
        sys.exit(status_code)
    except IndexError:
        print("Usage: j2lint.py filename [filename ...]\n")


if __name__ == "__main__":
    main()
