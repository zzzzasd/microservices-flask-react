# users-service/project/tests/base.py

from flask_testing import TestCase

from project import db
from project import create_app

app = create_app()

class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object('project.config.TestingConfig')
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        