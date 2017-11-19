#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import BluePrint

user = BluePrint('user', __name__)

from . import routes