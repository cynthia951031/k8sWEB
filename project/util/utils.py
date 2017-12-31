#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random
import string

"""
    本文件包含一些常用的工具函数
"""


def get_login_data(user):
    """得到该用户的登录数据"""
    return '{"username":"%s"}' % (user.name)

