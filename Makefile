SHELL := /bin/bash

all:

.PHONY : all

lint:
	uv run --frozen ruff check ./pyngeso ./tests

lint_fix:
	uv run --frozen ruff format ./pyngeso ./tests
	uv run --frozen ruff check ./pyngeso ./tests --fix

type_check:
	uv run --frozen mypy ./pyngeso ./tests

test:
	uv run --frozen pytest tests -v -r fEs
