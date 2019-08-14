import os
import unittest

from flask import current_app
from flask_testing import TestCase

from manage import app
from app.main.config import basedir


class TestDevConfig(TestCase):

    def create_app(self):
        app.config.from_object('app.main.config.DevConfig')
        return app

    def test_app_is_dev(self):
        self.assertFalse(app.config['SECRET_KEY'] is 'my_secret_key')
        self.assertFalse(current_app is None)
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertTrue(app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_main.db'))


if __name__ == "__main__":
    unittest.main()
