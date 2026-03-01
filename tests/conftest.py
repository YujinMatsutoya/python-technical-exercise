import pytest
from fake_device import FakeDevice
from device_client import DeviceClient

# This fixture creates a DeviceClient instance with a FakeDevice for testing
@pytest.fixture
def client():
    device = FakeDevice()
    return DeviceClient(device)
