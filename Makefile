SHELL=/bin/bash
PATH := .venv/bin:$(PATH)
export TEST?=./tests
export REPO=transferpy
export ENV?=dev

install-local:
	uv sync --all-groups

setup:
	@if [ ! -f .env ] ; then cp .env.mock .env ; fi;
	@make install;

lint: 
	@uv run ruff check .
	@uv run ruff format --check .

lint-fix:
	@uv run ruff check . --fix
	@uv run ruff format .

tests:
	@cp .env .env.back && cp .env.test .env;
	@docker compose up --build test;
	@docker compose down && docker compose rm test -f;
	@cp .env.back .env && rm .env.back;

tests-local:
	@cp .env .env.back && cp .env.local .env;
	@docker compose up -d db-testing;
	@python -B -m pytest -l --color=yes \
		--cov=core_app \
		--cov-config=./tests/.coveragerc \
		--cov-report term \
		--cov-report html:coverage \
		--junit-xml=junit.xml \
		--rootdir=. $${TEST};
	@docker compose down;
	@cp .env.back .env && rm .env.back;

app-dev:
	@cp .env .env.back && cp .env.dev .env;
	@docker compose up --build app-dev;
	@cp .env.back .env && rm .env.back;

run-local:
	@cp .env .env.back && cp .env.local .env;
	@docker compose up -d db_dev;
	@uv run app.py;

.PHONY: tests tests_local docs