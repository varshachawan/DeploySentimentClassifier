#!/usr/bin/env bash

gunicorn --config config.py classifier:app
