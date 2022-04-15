import requests


class CiscoDNA:
    def __init__(self, auth):
        self.auth = auth
        self.baseUrl = "https://sandboxdnac.cisco.com"
        self.UrlExtend = ""
        self.header = {"Content-Type": "application/json"}
        self.token = ""

    def get_token(self, urlExtend):
        self.UrlExtend = urlExtend
        response = requests.post(f"{self.baseUrl}{self.UrlExtend}", auth=self.auth, headers=self.header)
        if response.ok:
            self.token = response.json()["Token"]
            return self.token
        else:
            print("Failed with status {}".format(response.status_code))
            return
    def get_devices(self, urlExtend):
        self.UrlExtend = urlExtend
        self.header = {"Content-Type": "application/json", "X-Auth-Token": self.token}
        response = requests.get(f"{self.baseUrl}{self.UrlExtend}", auth=self.auth, headers=self.header)
        if response.ok:
            return response.json()
        else:
            print("Failed with status: {}".format(response.status_code))
            print("Body: {}".format(response.text))
            return

