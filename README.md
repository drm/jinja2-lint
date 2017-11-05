# Linter for jinja2 #

Every now and then, it's pretty useful to just have a cli tool that does the job. This does it.

## Usage: ##
```
python j2lint.py my-template.j2
```

It accepts multiple arguments so shell expansion and/or combining with find is no issue:

```
python j2lint.py *.j2
find src -type f -name "*.j2" -exec python j2lint.py '{}' +
```

