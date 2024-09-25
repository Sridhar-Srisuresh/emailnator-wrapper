import requests
from urllib.parse import unquote
import time


class EmailnatorWrapper:
    def __init__(self):
        self.base_url = "https://www.emailnator.com"
        self.session = requests.Session()
        self.xsrf_token = None

    def refresh_xsrf_token(self):
        response = self.session.get(self.base_url)
        self.xsrf_token = unquote(self.session.cookies.get('XSRF-TOKEN'))

    def generate_email(self):
        if not self.xsrf_token:
            self.refresh_xsrf_token()

        headers = {
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json",
            "x-requested-with": "XMLHttpRequest",
            "x-xsrf-token": self.xsrf_token,
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        }

        data = {"email": ["dotGmail"]}

        response = self.session.post(
            f"{self.base_url}/generate-email",
            headers=headers,
            json=data
        )

        if response.status_code == 200:
            json_response = response.json()
            if 'email' in json_response:
                # Return the first email in the list
                return json_response["email"][0]
        return None

    def get_messages(self, email):
        if not self.xsrf_token:
            self.refresh_xsrf_token()

        headers = {
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json",
            "x-requested-with": "XMLHttpRequest",
            "x-xsrf-token": self.xsrf_token,
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        }

        data = {"email": email}

        response = self.session.post(
            f"{self.base_url}/message-list",
            headers=headers,
            json=data
        )

        if response.status_code == 200:
            json_response = response.json()
            if 'messageData' in json_response:
                return json_response['messageData']
        return []