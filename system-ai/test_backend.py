"""Smoke tests for SYSTEM AI's local Flask backend.

Run after installing requirements.txt:
    python -m unittest test_backend.py
"""
import unittest

import app


class BackendSmokeTests(unittest.TestCase):
    def setUp(self):
        app.app.config["TESTING"] = True
        self.client = app.app.test_client()

    def test_health_is_online_and_does_not_expose_secret(self):
        response = self.client.get("/api/health")
        self.assertEqual(response.status_code, 200)
        payload = response.get_json()
        self.assertTrue(payload["ok"])
        self.assertFalse(payload["secrets_in_browser"])

    def test_study_command(self):
        response = self.client.post("/api/chat", json={"message": "study"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("JEE Scholar", response.get_json()["reply"])

    def test_empty_message_is_rejected(self):
        response = self.client.post("/api/chat", json={"message": " "})
        self.assertEqual(response.status_code, 400)

    def test_long_message_is_rejected(self):
        response = self.client.post("/api/chat", json={"message": "x" * 2001})
        self.assertEqual(response.status_code, 413)

    def test_search_returns_google_link(self):
        response = self.client.get("/api/search?q=JEE+physics")
        self.assertEqual(response.status_code, 200)
        self.assertIn("https://www.google.com/search?q=", response.get_json()["url"])

    def test_dashboard_is_served(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"SYSTEM AI", response.data)


if __name__ == "__main__":
    unittest.main()
