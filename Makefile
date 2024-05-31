SHELL=/bin/bash
PATH := .venv/bin:$(PATH)
export TEST?=./tests
export REPO=transferpy
export ENV?=dev

install-local:
	@( \
		if [ ! -d .venv ]; then python3 -m venv .venv; fi; \
		source .venv/bin/activate; \
		pip install -qU pip; \
		pip install -r requirements-dev.txt; \
		pip install -r requirements.txt; \
	)

setup:
	@if [ ! -f .env ] ; then cp .env.mock .env ; fi;
	@make install;

autoflake:
	@autoflake . --check --recursive --remove-all-unused-imports --remove-unused-variables --exclude .venv;

black:
	@black . --check --exclude '.venv|build|target|dist|.cache|node_modules';

isort:
	@isort . --check-only;

lint: black isort autoflake

lint-fix:
	@black . --exclude '.venv|build|target|dist';
	@isort .;
	@autoflake . --in-place --recursive --exclude .venv --remove-all-unused-imports --remove-unused-variables;

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
	@source .venv/bin/activate;
	@python app.py;

.PHONY: tests tests_local docs