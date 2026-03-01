from device.fake_device import FakeDevice
from device.device_client import DeviceClient

def test_firmware_version(client):
    assert client.get_firmware_version() == "1.0.0"

def test_hello():   
        print("Hello, World!")
        assert True