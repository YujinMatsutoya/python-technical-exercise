class DeviceClient:
    # This class serves as a client interface to interact with the FakeDevice
    def __init__(self, device):
        self.device = device

    def get_firmware_version(self):
        return self.device.process_command("GET_FW")

    def connect_wifi(self):
        return self.device.process_command("CONNECT_WIFI")
    
    def disconnect_wifi(self):
        return self.device.process_command("DISCONNECT_WIFI")
    
    def get_wifi_status(self):
        return self.device.process_command("GET_WIFI_STATUS")
    
    def turn_led_on(self):
        return self.device.process_command("TURN_LED_ON")
    
    def turn_led_off(self):
        return self.device.process_command("TURN_LED_OFF")
