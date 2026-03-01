class DeviceClient:
    def __init__(self, device):
        self.device = device

    def get_firmware_version(self):
        return self.device.process_command("GET_FW")
        