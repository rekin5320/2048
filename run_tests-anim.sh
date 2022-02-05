#!/bin/bash

path=$(dirname "$0")
cd $path
/usr/bin/env python3 -m unittest tests-anim.py
