# AutomationSystem.py
from Devices import Thermostat, Light, CCTV, Window

class AutomationSystem:
    def __init__(self):
        self.devices = [] # List of devices

    def discover_device(self, device): # Add device to list of devices 
        self.devices.append(device) 

    def execute_automation_tasks(self): # Execute automation tasks for each device
        for device in self.devices:
            if isinstance(device, Thermostat):
                self.automation_task_thermostat(device)
            elif isinstance(device, CCTV):
                self.automation_task_cctv(device)
            elif isinstance(device, Light):
                self.automation_task_lights(device)
            elif isinstance(device, Window):
                self.automation_task_window(device)

    def automation_task_thermostat(self, thermostat): 
        pass

    def automation_task_cctv(self, cctv):
        pass

    def automation_task_lights(self, lights):
        pass

    def automation_task_window(self, window):
        pass
