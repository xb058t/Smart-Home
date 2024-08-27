from tkinter import *
from tkinter import ttk
from Devices import Thermostat, CCTV, Light, Window
from DeviceController import DeviceController
import random

class SmartHome:
    """
    SmartHome is a class that represents a smart home
    system. It uses tkinter for the GUI and DeviceController
    to manage the devices.
    """
    ctrl = DeviceController()
    id = None
    delay = 600

    def __init__(self, root):
        """
        Initializes the SmartHome system with a tkinter root,
        adds devices to the controller, and sets up the GUI.
        """
        self.afters = []
        root.title("Smart Home")
        root.geometry("400x600")

        # Init all devices
        self.ctrl.add_device(Thermostat())
        self.ctrl.add_device(CCTV())
        self.ctrl.add_device(Light())
        self.ctrl.add_device(Window())

        self.thermostat_label = ttk.Label(root, text="Thermostat: Off")
        thermostat = self.ctrl.get_device("Thermostat")

        # Label that shows the current temperature
        self.thermostat_temperature_label = ttk.Label(root, text=thermostat.get_temperature())

        # Turn on and off buttons for the thermostat
        self.thermostat_turn_on_button = ttk.Button(root, text="Turn On", command=lambda: self.update_thermostat_mode_label(True))
        self.thermostat_turn_off_button = ttk.Button(root, text="Turn Off", command=lambda: self.update_thermostat_mode_label(False))

        # Increase and decrease buttons for temperature
        self.thermostat_increase_temperature_button = ttk.Button(root, text="Increase Temperature", command=lambda: self.update_thermostat_temp_label(True))
        self.thermostat_decrease_temperature_button = ttk.Button(root, text="Decrease Temperature", command=lambda: self.update_thermostat_temp_label(False))

        cctv = self.ctrl.get_device("CCTV")

        self.cctv_label = ttk.Label(root, text=f"CCTV Rec: {cctv.get_mode()} Infrared: {cctv.get_infrared()}")
        self.cctv_turn_on_button = ttk.Button(root, text="Turn On", command=lambda: self.update_cctv_mode_label(1))
        self.cctv_turn_off_button = ttk.Button(root, text="Turn Off", command=lambda: self.update_cctv_mode_label(0))

        self.infrared_toggle_button = ttk.Button(root, text="Toggle Infrared", command=lambda: self.update_cctv_mode_label(3))

        self.cctv_motion_label = ttk.Label(root, text="Simulate Motion: Off")
        self.cctv_motion_button = ttk.Button(root, text="Simulate Motion", command=lambda: self.update_cctv_motion_label())

        # lights
        lights = self.ctrl.get_device("Light")

        self.lights_label = ttk.Label(root, text=f"Lights: {lights.get_mode()}")
        self.lights_turn_on_button = ttk.Button(root, text="Turn On", command=lambda: self.update_lights_label(True))
        self.lights_turn_off_button = ttk.Button(root, text="Turn Off", command=lambda: self.update_lights_label(False))

        # Create a horizontal scrollbar for brightness
        self.lights_brightness_label = ttk.Label(root, text="Brightness: " + str(lights.get_brightness()))

        self.lights_brightness_scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=lambda value: self.update_brightness_label(value))
        self.lights_brightness_scale.set(lights.get_brightness())

        # window
        window = self.ctrl.get_device("Window")

        self.window_label = ttk.Label(root, text="Window: Closed")
        window_open_button = ttk.Button(root, text="Open", command=lambda: self.update_window_label(True))
        window_close_button = ttk.Button(root, text="Close", command=lambda: self.update_window_label(False))

        for child in root.winfo_children():
            child.pack()

        self.run_simulation()
        root.mainloop()

    def run_simulation(self):
        """
        Runs a simulation where the state of the devices is 
        randomly changed every delay milliseconds.
        """
        self.ctrl.randomizer()
        self.simulate_thermostat()
        self.simulate_cctv()
        self.simulate_lights()
        self.simulate_window()
        self.id = root.after(self.delay, self.run_simulation)

    def update_thermostat_temp_label(self, bool):
        """
        Updates the thermostat temperature label in the GUI.
        """
        thermostat = self.ctrl.get_device("Thermostat")
        if bool:
            thermostat.increase_temperature()
        else:
            thermostat.decrease_temperature()
        self.thermostat_temperature_label.configure(text=thermostat.get_temperature())

    def update_thermostat_mode_label(self, value):
        """
        Updates the thermostat mode label in the GUI.
        """
        thermostat = self.ctrl.get_device("Thermostat")
        thermostat.set_mode(value)
        self.thermostat_label.configure(text="Thermostat: " + thermostat.get_mode())

    def update_cctv_mode_label(self, value):
        """
        Updates the CCTV mode label in the GUI.
        """
        cctv = self.ctrl.get_device("CCTV")
        if value in [0,1]:
            cctv.set_mode(value)
        elif value == 3:
            cctv.toggle_infrared()
        else:
            cctv.set_infrared(True)
        self.cctv_label.configure(text="CCTV Rec: " + cctv.get_mode() + " Infrared: " + cctv.get_infrared())

    def update_cctv_motion_label(self):
        """
        Updates the CCTV motion label in the GUI.
        """
        cctv = self.ctrl.get_device("CCTV")
        cctv.toggle_motion()
        self.cctv_motion_label.configure(text="Simulate Motion: " + cctv.get_motion())
        self.update_cctv_mode_label(4)

    def update_lights_label(self, command):
        """
        Updates the lights mode label in the GUI.
        """
        lights = self.ctrl.get_device("Light")
        lights.set_mode(command)
        self.lights_label.configure(text="Lights: " + lights.get_mode())

    def update_brightness_label(self, value):
        """
        Updates the lights brightness label in the GUI.
        """
        lights = self.ctrl.get_device("Light")
        lights.set_brightness(int(value))
        self.lights_brightness_label.config(text="Brightness: " + str(lights.get_brightness()))

    def update_window_label(self, state):
        """
        Updates the window mode label in the GUI.
        """
        window = self.ctrl.get_device("Window")
        if state:
            window.window_open()
        else:
            window.window_close()
        self.window_label.configure(text="Window: " + window.get_mode())

    def simulate_thermostat(self):
        """
        Simulates the thermostat by updating the GUI labels.
        """
        thermostat = self.ctrl.get_device("Thermostat")
        self.temperature_label = ttk.Label(root, text="Thermostat: " + thermostat.get_mode())
        self.thermostat_temperature_label.configure(text=thermostat.get_temperature())

    def simulate_cctv(self):
        """
        Simulates the CCTV by updating the GUI labels.
        """
        cctv = self.ctrl.get_device("CCTV")
        self.cctv_motion_label.configure(text="Simulate Motion: " + cctv.get_motion())

    def simulate_lights(self):
        """
        Simulates the lights by updating the GUI labels.
        """
        lights = self.ctrl.get_device("Light")
        self.lights_label.configure(text="Lights: " + lights.get_mode())
        self.lights_brightness_scale.set(lights.get_brightness())

    def simulate_window(self):
        """
        Simulates the window by updating the GUI labels.
        """
        window = self.ctrl.get_device("Window")
        self.window_label.configure(text="Window: " + window.get_mode())
    
if __name__ == "__main__":
    root = Tk()
    SmartHome(root)