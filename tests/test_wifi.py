import pytest
from fake_device import (FakeDevice, WiFiAlreadyConnectedError)
from device_client import DeviceClient

def test_wifi_connection(client):
    # Initially, the wifi should be disconnected
    assert client.get_wifi_status() == "WIFI_DISCONNECTED"
    
    # Connect to wifi and check status
    assert client.connect_wifi() == "WIFI_CONNECTED"
    assert client.get_wifi_status() == "WIFI_CONNECTED"
    
    # Disconnect from wifi and check status
    assert client.disconnect_wifi() == "WIFI_DISCONNECTED"
    assert client.get_wifi_status() == "WIFI_DISCONNECTED"

def test_connect_twice_raises_wifi_error(client):
    # Connect to wifi should succeed
    assert client.connect_wifi() == "WIFI_CONNECTED"
    
    # Attempt to connect again should raise wifi error
    with pytest.raises(WiFiAlreadyConnectedError):
        client.connect_wifi()
