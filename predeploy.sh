#!/usr/bin/env bash

./manage.py migrate --no-input
./manage.py collectstatic --no-input
