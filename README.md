# Linter for jinja2 #

Every now and then, it's pretty useful to just have a cli tool that does the job. This does it.

## Usage: ##
```
cp j2lint.py /usr/local/bin/
j2lint.py my-template.jinja
```

It accepts multiple arguments so shell expansion and/or combining with find is no issue:

```
j2lint.py *.jinja
find src -type f -name "*.jinja" -exec j2lint.py '{}' +
```

```
usage: j2lint.py [-h] [--quiet] [--filter filter [filter ...]] file [file ...]

Lint jinja files

positional arguments:
  file                  the files to lint

optional arguments:
  -h, --help            show this help message and exit
  --quiet               Only print errors
  --filter filter [filter ...]
                        Add custom jinja filter
```

## Usage with custom filters, tests, etc ##

If you want to use this linter with custom filters, tests, etc, you can easily
extend the main cli endpoint by passing in a `env` keyword argument.

The file [custom_check_example.py](custom_check_example.py) provides a working example for the filter
'to_nice_json'. 

You also have the option of specifying custom filters via the command line with
the `--filter` argument:

```
usage: j2lint.py --filter=to_nice_json *.jinja
```

Note that for linting it is not necessary to refer to the actual implementation
of the filters, jinja2 only needs to know they exist.

## Usage with docker ##

To run this using docker, run:

```
docker run --rm -v "$(pwd)":/check kaictl/j2lint
```

Important options:

* `-e CUSTOMLINT=path/to/custom/lint`: the path to a custom lint py file in the directory you're checking.
  By default we check for `/custom.py`, so you can mount a file there instead of specifying this.
* `-v "$(pwd)":/check`: mount the current directory to `/check` on the container