import urllib.request
import unittest
from unittest.mock import patch

class WebRequet():
    def __init__(self, url):
        self.url = url

    def execute(self):
        response = urllib.request.urlopen(self.url)
        if response.status == 200:
            return "SUCCESS"

        return "FAILURE"

class WebRequetTest(unittest.TestCase):
    def test_execute_with_success_response(self):
        with patch('urllib.request.urlopen') as mock_urlopen:
            mock_urlopen.return_value.status = 200
            wr = WebRequet("http//:www.google.com")
            self.assertAlmostEqual(wr.execute(), "SUCCESS")

    def test_execute_with_failure_response(self):
        with patch('urllib.request.urlopen') as mock_urlopen:
            mock_urlopen.return_value.status = 404
            wr = WebRequet("http//:www.google.com")
            self.assertAlmostEqual(wr.execute(), "FAILURE")

if __name__ == "__main__":
    unittest.main()
