import pytest
from fake_device import FakeDevice
from device_client import DeviceClient

def test_firmware_version(client):
    assert client.get_firmware_version() == "1.0.0"

@pytest.mark.parametrize("method_name, expected_state", [("turn_led_on", "LED_ON"), ("turn_led_off", "LED_OFF")])
def test_led_state(client, method_name, expected_state):
    # Test turning LED on
    led_method = getattr(client, method_name)
    assert led_method() == expected_state
    