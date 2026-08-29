PACKAGE_NAME = qcs_api_client

.PHONY: style style-check test docs watch-docs

style:
	uv run --group dev ruff format .
	uv run --group dev ruff check --fix .

style-check:
	uv run --group dev ruff check --diff .

test:
	uv run --group dev pytest tests

docs:
	uv run --group docs $(MAKE) -C docs html

watch-docs: install-dev
	sphinx-autobuild docs docs/_build/html
