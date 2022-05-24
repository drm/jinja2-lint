#!/usr/bin/env python
"""
@author Gerard van Helden <drm@melp.nl>
@license DBAD, see <http://www.dbad-license.org/>

Simple j2 linter, useful for checking jinja2 template syntax
"""
import os.path
from functools import reduce
from jinja2 import BaseLoader, TemplateNotFound, Environment, exceptions, filters
from jinja2_ansible_filters import AnsibleCoreFiltersExtension
from ansible_collections.ansible.netcommon.plugins.filter import ipaddr

filters.FILTERS['ipaddr'] = ipaddr
class AbsolutePathLoader(BaseLoader):
    def get_source(self, environment, template):
        if not os.path.exists(template):
            raise TemplateNotFound(template)
        mtime = os.path.getmtime(template)
        with open(template) as file:
            source = file.read()
        return source, template, lambda: mtime == os.path.getmtime(template)

def check(template, out, err,
  env=Environment(loader=AbsolutePathLoader(),extensions=[
    'jinja2.ext.i18n',
    'jinja2.ext.do',
    'jinja2.ext.loopcontrols',
    'jinja2_ansible_filters.AnsibleCoreFiltersExtension'
    ]
  )):
    try:
        env.get_template(template)
        out.write("%s: Syntax OK\n" % template)
        return 0
    except TemplateNotFound:
        err.write("%s: File not found\n" % template)
        return 2
    except exceptions.TemplateSyntaxError as ex:
        err.write("%s: Syntax check failed: %s in %s at %d\n"
                  % (template, ex.message, ex.filename, ex.lineno))
        return 1

def main(**kwargs):
    import sys
    try:
        sys.exit(reduce(lambda r, fn: r +
                        check(fn, sys.stdout, sys.stderr, **kwargs), sys.argv[1:], 0))
    except IndexError:
        sys.stdout.write("Usage: j2lint.py filename [filename ...]\n")

if __name__ == "__main__":
    main()
