from setuptools import setup
import os

home = os.environ['HOME']

if os.path.exists(f"{home}/.config/Layout_Helper"):
    os.system(f"mkdir {home}/.config/Layout_Helper")

os.system(f"cp layouts/* {home}/.config/Layout_Helper")

setup(name="Layout Helper",
      version="0.1",
      description="shows the keyboard layout",
      author="horse",
      author_email="horsescary@gmail.com",
      license="GPL3",
      packages=['layout_helper'],
      zip_safe=False,
      scripts=["bin/layout_helper"])
