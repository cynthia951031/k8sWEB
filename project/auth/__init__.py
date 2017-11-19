#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import BluePrint

auth = BluePrint('auth', __name__)

from . import routes