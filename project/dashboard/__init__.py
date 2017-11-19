#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flash import Blueprint

dashboard = Blueprint('dashboard', __name__)

from . import routes