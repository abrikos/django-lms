#!/bin/bash
echo "======== ISORT =========="
isort config mailing users
echo "======== BLACK =========="
black config mailing users
echo "======== FLAKE8 =========="
flake8 config mailing users
#echo "======== MYPY =========="
#mypy config mailing users
