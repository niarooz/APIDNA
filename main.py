import dnaAPI
import json
if __name__ == "__main__":
    Niaz = dnaAPI.CiscoDNA(("devnetuser", "Cisco123!"))
    token = Niaz.get_token("/dna/system/api/v1/auth/token")
    # print(token)

    device_list = Niaz.get_devices("/dna/intent/api/v1/network-device")
    print(json.dumps(device_list, indent=4))