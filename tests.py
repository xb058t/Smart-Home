import unittest
from DeviceController import DeviceController
from Devices import Light, Thermostat, Window, CCTV

class TestGeneralLogic(unittest.TestCase):
    """TestGeneralLogic tests the basic functionality of the DeviceController class."""

    def test_init(self):
        """test_init tests the initialization of a DeviceController instance."""
        ctrl = DeviceController()
        self.assertEqual(len(ctrl.devices), 0)
        
    def test_add_device(self):
        """test_add_device tests the addition of a device to the DeviceController."""
        ctrl = DeviceController()
        ctrl.add_device(Light())
        self.assertEqual(len(ctrl.devices), 1)

    def test_get_devices(self):
        """test_get_devices tests the retrieval of all devices from the DeviceController."""
        ctrl = DeviceController()
        ctrl.add_device(Light())
        ctrl.add_device(Thermostat())
        ctrl.add_device(Window())
        ctrl.add_device(CCTV())
        self.assertEqual(len(ctrl.get_devices()), 4)

    def test_get_device(self):
        """test_get_device tests the retrieval of a specific device from the DeviceController."""
        ctrl = DeviceController([Light()])
        device = ctrl.get_device("Light")
        self.assertEqual(device.id, "Light")
        self.assertEqual(device.mode, "Off")

    def test_get_device_none(self):
        """test_get_device_none tests the retrieval of a non-existent device from the DeviceController."""
        ctrl = DeviceController()
        device = ctrl.get_device("Thermostat")
        self.assertEqual(device, None)

    def test_getter(self):
        """test_getter tests the getter methods of a Light device."""
        ctrl = DeviceController([Light()])
        device = ctrl.get_device("Light")
        self.assertEqual(device.get_mode(), "Off")
        self.assertEqual(device.get_brightness(), 0)

    def test_setter(self):
        """test_setter tests the setter and toggle methods of a Thermostat device."""
        ctrl = DeviceController([Thermostat()])
        device = ctrl.get_device("Thermostat")
        device.set_mode(True)
        self.assertEqual(device.get_mode(), "On")
        device.set_mode(False)
        self.assertEqual(device.get_mode(), "Off")
        device.turn_on()
        self.assertEqual(device.get_mode(), "On")
        device.turn_off()
        self.assertEqual(device.get_mode(), "Off")
        device.set_temperature(30)
        self.assertEqual(device.get_temperature(), 30)

class TestRandomizer(unittest.TestCase):
    """TestRandomizer tests the randomizer method of the DeviceController class."""

    def test_randomizer_all(self):
        """test_randomizer_all tests the randomizer on all types of devices."""
        ctrl = DeviceController([Light(), Thermostat(), Window(), CCTV()])
        for _ in range(100):
            ctrl.randomizer()
        for device in ctrl.devices:
            if device.id == "Window":
                self.assertTrue(device.get_mode() in ["Open", "Closed"])
                continue
            self.assertTrue(device.get_mode() in ["On", "Off"])

    def test_randomizer_light(self):
        """test_randomizer_light tests the randomizer on a Light device."""
        ctrl = DeviceController([Light()])
        device = ctrl.get_device("Light")
        device.set_brightness(50)
        ctrl.randomizer()
        self.assertTrue(device.get_mode() in ["On", "Off"])
        self.assertTrue(49 <= device.get_brightness() <= 51)

    def test_randomizer_thermostat(self):
        """test_randomizer_thermostat tests the randomizer on a Thermostat device."""
        ctrl = DeviceController([Thermostat()])
        device = ctrl.get_device("Thermostat")
        device.set_temperature(10)
        ctrl.randomizer()
        self.assertTrue(device.get_mode() in ["On", "Off"])
        self.assertTrue(9 <= device.get_temperature() <= 11)

    def test_randomizer_window(self):
        """test_randomizer_window tests the randomizer on a Window device."""
        ctrl = DeviceController([Window()])
        device = ctrl.get_device("Window")
        device.set_mode("Closed")
        ctrl.randomizer()
        self.assertTrue(device.get_mode() in ["Open", "Closed"])

    def test_randomizer_cctv(self):
        """test_randomizer_cctv tests the randomizer on a CCTV device."""
        ctrl = DeviceController([CCTV()])
        device = ctrl.get_device("CCTV")
        device.set_mode("Off")
        ctrl.randomizer()
        self.assertTrue(device.get_mode() in ["On", "Off"])

class DeviceSpecific(unittest.TestCase):
    """DeviceSpecific tests specific functionality of the CCTV and Window devices."""

    def test_motion(self):
        """test_motion tests the motion detection and infrared functionality of a CCTV device."""
        ctrl = DeviceController([CCTV()])
        device = ctrl.get_device("CCTV")
        device.set_motion(True)
        self.assertEqual(device.get_motion(), "On")
        device.toggle_motion()
        self.assertEqual(device.get_motion(), "Off")
        device.set_infrared(True)
        self.assertEqual(device.get_infrared(), "On")
        device.toggle_infrared()
        self.assertEqual(device.get_infrared(), "Off")

    def test_window(self):
        """test_window tests the open and close functionality of a Window device."""
        ctrl = DeviceController([Window()])
        device = ctrl.get_device("Window")
        device.window_close()
        self.assertEqual(device.get_mode(), "Closed")
        device.window_open()
        self.assertEqual(device.get_mode(), "Open")

if __name__ == '__main__':
    """The script is executed with the unittest.main() function, which runs all the test cases."""
    unittest.main()