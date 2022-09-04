# Flask
from flask_testing import TestCase
from flask import current_app, url_for
# App
from main import app

# TestCase for main file
class MainTest(TestCase):

    # about app
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app

    def test_app_exists(self):
        """
        ** Test if app is not None **
        """
        self.assertIsNotNone(current_app)

    def test_app_in_test_mode(self):
        """
        ** Test if app is in test mode **
        """
        self.assertTrue(current_app.config['TESTING'])

    # route index
    def test_index_redirects(self):
        """
        ** Test if from index path redirects to hello path **
        """
        response = self.client.get(url_for('index'))
        self.assertRedirects(response, url_for('hello'))

    # route hello
    def test_hello_get(self):
        """
        ** Test if hello path with "http get method" responds with status code 200 **
        """
        response = self.client.get(url_for('hello'))
        self.assert200(response)

    def test_hello_post(self):
        """
        ** Test if hello path with "http post method" responds with redirect to index path **
        """
        response = self.client.post(url_for('hello'))
        self.assertTrue(response.status_code, 405)

    # route auth
    def test_auth_blueprint_exists(self):
        """
        ** Test if auth blueprint exists **
        """
        self.assertIn('auth', self.app.blueprints)

    def test_auth_login_get(self):
        """
        ** Test if login (with http method 'get') responds with status code 200 **
        """
        response = self.client.get(url_for('auth.login'))
        self.assert200(response)

    def test_auth_login_template(self):
        """
        ** Test if login uses login.html template **
        """
        self.client.get(url_for('auth.login'))
        self.assertTemplateUsed('login.html')

    def test_auth_login_post(self):
        """
        ** Test if login (with http method 'post') redirects to index path **
        """
        fake_form = {
            'username': 'fake',
            'password': 'fake-password'
        }
        response = self.client.post(url_for('auth.login'), data=fake_form)
        self.assertRedirects(response, url_for('index'))
