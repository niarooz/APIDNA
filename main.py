import dnaAPI
import json
if __name__ == "__main__":
    Niaz = dnaAPI.CiscoDNA(("devnetuser", "Cisco123!"))
    token = Niaz.get_token("/dna/system/api/v1/auth/token")
    # print(token)

    device_list = Niaz.get_devices("/dna/intent/api/v1/network-device")
    for device in device_list["response"]:
        print(f"Device ID: {device['id']}  Device IP: {device['managementIpAddress']}")

    new_device = {
        "ipAddress": ["192.0.2.1"],
        "snmpVersion": "v2",
        "snmpROCommunity": "readonly",
        "snmpRWCommunity": "readwrite",
        "snmpRetry": "1",
        "snmpTimeout": "60",
        "cliTransport": "ssh",
        "userName": "nick",
        "password": "secret123!",
        "enablePassword": "secret456!",
    }

    Niaz.add_device("/dna/intent/api/v1/network-device", new_device)


