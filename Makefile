.PHONY: install, run, lint, fix, test, ci

install:
	docker-compose run --rm app poetry install

run:
	docker-compose run --rm app poetry run python log_parser

lint:
	docker-compose run --rm app poetry run mypy --explicit-package-bases .
	docker-compose run --rm app poetry run ruff check .
	docker-compose run --rm app poetry run black --check .

fix:
	docker-compose run --rm app poetry run ruff check . --fix-only --exit-zero
	docker-compose run --rm app poetry run black .

test:
	docker-compose run --rm app poetry run pytest

ci:
	make lint
	make test
