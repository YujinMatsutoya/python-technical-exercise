import pytest
from fake_device import FakeDevice
from device_client import DeviceClient

@pytest.fixture
def client():
    device = FakeDevice()
    return DeviceClient(device)
