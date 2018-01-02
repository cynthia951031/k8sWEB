#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
config.py 是初始化 Flask app 的配置文件,当创建一个 app 时,将选择一种配置进行初始化
项目用到的全局变量也写在这个文件中,主要包括多种模式下的配置类型和全局参数（如密钥、连接数据库的 URL）等

config.py、APP/init.py 以及 manage.py 之间的关系：
1. config.py 是创建app时需参考的配置文件,即使用何种配置（生产环境或开发环境）
2. APP/init.py 是创建app的具体工厂函数，并包括了路由的配置。该文件使用了config.py中的配置。
3. manage.py 是创建以及运行app的一个通用脚本，该文件使用了 APP/init.py
"""


class Config:
    SECRET_KEY = 'secret'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///k8s.db'

class TestingConfig(Config):
    TESTING = True
    SECRET_KEY = 'secret'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///k8s.db'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///k8s.db'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
