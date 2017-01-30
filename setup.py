from setuptools import setup

setup(name="systeminfo",
      version="0.1",
      description="Basic system information for COMP30670",
      url="",
      author="Wen-Ting, Chang",
      author_email="wen-ting.chang@ucdconnect.ie",
      licence="GPL3",
      package=['systeminfo'],
      entry_points={
          'console_scripts':['comp30670_systeminfo=systeminfo.main:main']
          }
      )