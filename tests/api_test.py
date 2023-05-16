import unittest
import sys

from src.serve.api import app

class FlaskTest(unittest.TestCase):
    
    #preveri če home page vrne kodo 200 success
    def test_index_success(self):
        tester = app.test_client(self)
        responce = tester.get("/")

        statuscode = responce.status_code
        self.assertEqual(statuscode, 200)