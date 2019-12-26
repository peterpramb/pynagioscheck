#!/usr/bin/env make
#

V := 0
AT_0 := @
AT_1 :=
AT = $(AT_$(V))

SHELL := $(shell command -v bash 2>/dev/null)

SOURCES := Makefile nagioscheck.py \
    $(shell find tests -type f \
	-not \( \
	  -name '.*.swp' -or \
	  -name '.*.pyc' -or \
	  -name '__pycache__' \
	\) \
)

all: test-stamp

coverage: test-stamp
	$(AT)coverage report -m | tee coverage

test: tests

tests: test-stamp

test-stamp: $(SOURCES)
	$(AT)rm -f .coverage
	$(AT)coverage run -m nose; echo
	$(AT)touch $@

.PHONY: all coverage test tests
