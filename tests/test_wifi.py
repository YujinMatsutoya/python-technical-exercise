from fake_device import FakeDevice
from device_client import DeviceClient

def test_wifi_connection(client):
    # Initially, the WiFi should be disconnected
    assert client.get_wifi_status() == "WIFI_DISCONNECTED"
    
    # Connect to WiFi and check status
    assert client.connect_wifi() == "WIFI_CONNECTED"
    assert client.get_wifi_status() == "WIFI_CONNECTED"
    
    # Disconnect from WiFi and check status
    assert client.disconnect_wifi() == "WIFI_DISCONNECTED"
    assert client.get_wifi_status() == "WIFI_DISCONNECTED"

