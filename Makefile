PACKAGE_NAME = qcs_api_client

.PHONY: install-dev \
	style style-check test \
	docs watch-docs

install-dev:
	poetry install --with dev

style: install-dev
	poetry run ruff format .
	poetry run ruff check --fix .

style-check: install-dev
	poetry run ruff check --diff .

test: install-dev
	poetry run pytest tests


docs: install-dev
	poetry run $(MAKE) -C docs html

watch-docs: install-dev
	sphinx-autobuild docs docs/_build/html
