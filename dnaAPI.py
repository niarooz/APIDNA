import requests


class CiscoDNA:
    def __init__(self, auth):
        self.auth = auth
        self.baseUrl = "https://sandboxdnac.cisco.com"
        self.UrlExtend = ""
        self.header = {"Content-Type": "application/json"}
        self.token = ""
        self.taskID= ""

    def get_token(self, urlExtend):
        self.UrlExtend = urlExtend
        response = requests.post(f"{self.baseUrl}{self.UrlExtend}", auth=self.auth, headers=self.header)
        if response.ok:
            self.token = response.json()["Token"]
            return self.token
        else:
            print("Failed to get token: {}".format(response.status_code))
            return
    def get_devices(self, urlExtend):
        self.UrlExtend = urlExtend
        self.header = {"Content-Type": "application/json", "X-Auth-Token": self.token}
        response = requests.get(f"{self.baseUrl}{self.UrlExtend}", auth=self.auth, headers=self.header)
        if response.ok:
            return response.json()
        else:
            print("\nFailed to get device list: {}".format(response.status_code))
            print("Body: {}".format(response.text))
            return

    def add_device(self, urlExtend, device):
        self.UrlExtend = urlExtend
        self.header = {"Content-Type": "application/json", "X-Auth-Token": self.token}
        response = requests.post(f"{self.baseUrl}{self.UrlExtend}", json=device, headers=self.header)
        if response.ok:
            self.taskID = response.json()["response"]["taskid"]
            return response.json()
        else:
            print("\nFailed to add device: {}".format(response.status_code))
            print("Body: {}".format(response.text))
            return

    def get_taskStatus(self, urlExtend):
        self.UrlExtend = urlExtend
        self.header = {"Content-Type": "application/json", "X-Auth-Token": self.token}
        response = requests.post(f"{self.baseUrl}{self.UrlExtend}{self.taskID}", headers=self.header)
        if response.ok:
            while response.json()["response"]["isError"]:
                response.json()["response"]["progress"]
                print("Waiting for response...")
            print("device added successfully")
            return
        else:
            print("\nFailed to retrieve status: {}".format(response.status_code))
            print("Body: {}".format(response.text))
            return

    # def del_device(self, urlExtend, devID):
    #     self.UrlExtend = urlExtend
    #     response = requests.post(f"{self.baseUrl}{self.UrlExtend}{self.taskID}", headers=self.header)
    #     if response.ok:
    #         pass




