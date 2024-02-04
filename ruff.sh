#!/bin/bash

ruff format .
ruff check --fix --no-cache --unsafe-fixes .
