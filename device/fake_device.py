class FakeDevice:
    def __init__(self):
        self.firmware_version = "1.0.0"
        self.wifi_connected = False

    def process_command(self, command: str) -> str:
        
        if command == "GET_FW":
            return self.firmware_version
        
        elif command == "CONNECT_WIFI":
            self.wifi_connected = True
            return "WIFI_CONNECTED"
        
        elif command == "DISCONNECT_WIFI":
            self.wifi_connected = False
            return "WIFI_DISCONNECTED"
        
        elif command == "GET_WIFI_STATUS":
            return "WIFI_CONNECTED" if self.wifi_connected else "WIFI_DISCONNECTED"
        
        else: 
            # add error handling
            return "UNKNOWN_COMMAND"
