import pytest
from fake_device import FakeDevice
from device_client import DeviceClient

def test_firmware_version(client):
    # Test that the firmware version is correctly retrieved
    assert client.get_firmware_version() == "1.0.0"

@pytest.mark.parametrize("method_name, expected_state", [("turn_led_on", "LED_ON"), ("turn_led_off", "LED_OFF")])
def test_led_state(client, method_name, expected_state):
    # Test expected LED states
    led_method = getattr(client, method_name)
    assert led_method() == expected_state
    