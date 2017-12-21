SHELL := /bin/bash
MAKEFILE_RULES := $(shell cat Makefile | grep "^[A-Za-z]" | awk '{print $$1}' | sed "s/://g" | sort -u)
PYTHON_EXE := python3
PYTHON_ENV := ./env
PYTHON_BIN := $(PYTHON_ENV)/bin
PYTHON_REQUIREMENTS := ./requirements.txt


DEFAULT: help


#================================================================================
# Environment
#================================================================================

.PHONY: requirements.txt
requirements.txt:  ## Write the requirements.txt file.
requirements.txt: virtualenv
	$(PYTHON_BIN)/pip freeze > $(PYTHON_REQUIREMENTS)


virtualenv:  ## Build the python virtual environment.
	@echo -e "Building/verifying virtualenv at $(PYTHON_ENV) based on $(PYTHON_REQUIREMENTS)\n"
	@command -v pip >/dev/null 2>&1 || { echo >&2 "I require pip but it's not installed.  Aborting."; exit 1; }
	@if [ ! -f "$(PYTHON_ENV)/bin/activate" ] ; then \
		 virtualenv -p $(PYTHON_EXE) $(PYTHON_ENV) ; \
	fi
	$(PYTHON_BIN)/pip install -q -r $(PYTHON_REQUIREMENTS)
	$(PYTHON_BIN)/pip install -q flake8


#================================================================================
# Distribution
#================================================================================

package: dist

dist:  ## Build the Annotator package binaries.
dist:
	$(PYTHON_BIN)/$(PYTHON_EXE) setup.py sdist bdist bdist_wheel


#================================================================================
# Cleanliness
#================================================================================

lint: pylint
flake8: pylint

.PHONY: lint
pylint:  ## Lint the Python app.
pylint: virtualenv
	$(PYTHON_BIN)/flake8 *.py j2lint/*.py


#================================================================================
# Extras
#================================================================================

.PHONY: help
help:  ## This help dialog.
	@echo -e  "You can run the following commands from this$(MAKEFILE_LIST):\n"
	@IFS=$$'\n' ; \
	help_lines=(`fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//'`) ; \
	for help_line in $${help_lines[@]}; do \
		IFS=$$'#' ; \
		help_split=($$help_line) ; \
		help_command=`echo $${help_split[0]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		help_info=`echo $${help_split[2]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		printf "  %-27s %s\n" $$help_command $$help_info ; \
	done
