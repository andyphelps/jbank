.PHONY: test lint format sast clean run
sync:
	uv sync --extra dev

run:
	uv run reflex run

test:
	uv run pytest

lint:
	uv run black --check src tests
	uv run isort --check-only src tests
	uv run flake8 src tests
	uv run mypy src tests

format:
	uv run black src tests
	uv run isort src tests

sast:
	uv run bandit -r src tests

build: lint sast test
	uv build

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -name "*.pyc" -delete
	rm -rf .coverage htmlcov dist build *.egg-info
