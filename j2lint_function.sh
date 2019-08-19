#!/bin/sh

function j2lint() {

  volume="${volume:-/check/}"
  image="${image:-drm/jinja2-lint}"
  runner="${runner:-/j2lint.py}"

  while [ ! "$1" == "" ] ; do
    test_file="$1"
    shift

    directory="$(dirname "${test_file}")"
    filename="$(basename "${test_file}")"
    
    docker run -it --rm  -v "${directory}":"${volume}" ${image} ${runner} /${volume}/${filename} | sed -e "s|${volume}|${directory}|g" -e "s|//*|/|g"
  done
}
