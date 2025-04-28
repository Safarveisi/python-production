#!/bin/bash

EXIT_STATUS=0

black --config pyproject.toml . || ((EXIT_STATUS++))
pylint --rcfile .pylintrc *.py || ((EXIT_STATUS++))
flake8 --config .flake8 . || ((EXIT_STATUS++))
mypy . --exclude venv || ((EXIT_STATUS++))
ruff --config ruff.toml check . || ((EXIT_STATUS++))
isort . --settings .isort.cfg || ((EXIT_STATUS++))

echo exiting with status $EXIT_STATUS

exit $EXIT_STATUS