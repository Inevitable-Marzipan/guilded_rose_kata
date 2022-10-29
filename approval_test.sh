#!/bin/bash

pytest --cov=src --cov-report=html --approvaltests-use-reporter='PythonNative' tests_approval/test_approval.py -s