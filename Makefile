#!/usr/bin/env make
#

V := 0
AT_0 := @
AT_1 :=
AT = $(AT_$(V))

MOD_PATH := $(dir $(realpath $(lastword $(MAKEFILE_LIST))))

SHELL := $(shell command -v bash 2>/dev/null)

SOURCES := Makefile nagioscheck.py \
    $(shell find tests -type f \
	-not \( \
	  -name '.*.swp' -or \
	  -name '.*.pyc' -or \
	  -name '__pycache__' \
	\) \
)

TOOLS = nosetests pytest unit2

all: test-stamp

coverage: test-stamp
	$(AT)coverage report -m | tee coverage

test: tests

tests: test-stamp

test-stamp: $(SOURCES)
	$(AT)rm -f .coverage
	$(AT)for tool in $(TOOLS); do \
	  toolpath=$$(command -v $$tool 2>/dev/null) && \
	  echo "==> Running $$tool:" && \
	  PYTHONPATH="$(MOD_PATH):${PYTHONPATH}" $$toolpath && \
	  echo; \
	done
	$(AT)echo "==> Running coverage:" && \
	cat tests/ORDER | while read t; do \
	  echo "$${t}:" && \
	  PYTHONPATH="$(MOD_PATH):${PYTHONPATH}" coverage run -a "$$t"; \
	done; \
	echo
	$(AT)touch $@

.PHONY: all coverage test tests
