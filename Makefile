#!/usr/bin/env make

all:
	@echo "Available targets: clean, distclean, tarballs, test(s)"

.PHONY: clean
clean:
	@echo "Cleaning up..."
	@rm -Rf .coverage build
	@find dist -depth -maxdepth 1 -type f -exec rm -rf '{}' +
	@find . -depth -type d -name "__pycache__" -exec rm -Rf '{}' +
	@find . -depth -type f -name "*.py[cod]" -exec rm -f '{}' +

.PHONY: distclean
distclean: clean
	@rm -Rf .eggs .tox htmlcov *.egg-info

.PHONY: tarballs
tarballs: distclean
	@echo "Building tarballs..."
	@tox -e tarballs

.PHONY: test
test: tests

.PHONY: tests
tests:
	@echo "Running tests..."
	@tox
