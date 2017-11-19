#! /usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint
interface_blueprint = Blueprint('interface', __name__)

from . import API_manage