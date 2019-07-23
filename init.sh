#!/usr/bin/env sh

export PYTHONPATH=/:"$PYTHONPATH"

if [ -f /custom.py ]; then
    _RUNNER=/custom.py
elif [ -f "/check/$CUSTOMLINT" ]; then
    _RUNNER=/check/$CUSTOMLINT
else
    _RUNNER=/j2lint.py
fi

find /check \( -name '*.jinja' -or -name '*.j2' \) -exec /usr/bin/python "${_RUNNER}" {} +