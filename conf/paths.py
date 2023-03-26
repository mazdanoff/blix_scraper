import os

project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

drivers_dir = os.path.join(project_path, "drivers")
geckodriver_dir = os.path.join(drivers_dir, "geckodriver.exe")
screenshots_dir = os.path.join(project_path, "screenshots")
