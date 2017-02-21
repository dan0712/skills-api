# -*- coding: utf-8 -*-

"""
server
~~~~~~

Local web server for the Open Data API.

"""

import os

from app.app import app
from flask_script import Manager

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

manager = Manager(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
