#!/bin/bash
echo "======== ISORT =========="
isort config lms users
echo "======== BLACK =========="
black config lms users
echo "======== FLAKE8 =========="
flake8 config lms users
#echo "======== MYPY =========="
#mypy config mailing users
