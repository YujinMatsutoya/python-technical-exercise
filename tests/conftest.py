import pytest
from device.fake_device import FakeDevice
from device.device_client import DeviceClient

@pytest.fixture
def client():
    device = FakeDevice()
    return DeviceClient(device)
