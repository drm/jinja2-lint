# Linter for jinja2 #

Every now and then, it's pretty useful to just have a cli tool that does the job. This does it.

## Usage: ##
```
cp j2lint.py /usr/local/bin/
j2lint.py my-template.j2
```

It accepts multiple arguments so shell expansion and/or combining with find is no issue:

```
j2lint.py *.j2
find src -type f -name "*.j2" -exec j2lint.py '{}' +
```

## Usage with custom filters, tests, etc ##

If you want to use this linter with custom filters, tests, etc, you can easily
extend the main cli endpoint by passing in a `env` keyword argument.

The file [custom_check_example.py](custom_check_example.py) provides a working example for the filter
'to_nice_json'. 

Note that for linting it is not necessary to refer to the actual implementation
of the filters, jinja2 only needs to know they exist.
