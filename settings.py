#!/usr/bin/python
# Copyright 2017 Luca Berton
__author__ = 'lucab85'

debug = True

PM_config = {
    'host': 'mdbus',
    'port': 502,
    'address': 10,
    'addressoffset': -1,
    'start_reg': 0,
    'max_regs': 125,
    'timeout': 2,
    'endian': 'big',
    'cacheEnabled': False,
    'base_commands': 5250,
}

InfluxDBConfig = [
    {
        'host': 'influxdb',
        'port':  8086,
        'username': 'admin', 
        'password':'admin',
        'database': 'db0'
    }
]

PM_settings = {
    'Set DateTime': {
        'command': 1003
    },
}

MODBUS_CONNECTIONRETRY = 3
PATH_LOGGING = 'configs/logging.json'
PATH_PM_SCHNEIDERELECTRICIEM3255 = 'configs/Map-Schneider-iEM3255.csv'
PM_SETTINGS_LABELS = [
      "Serial Number", "Hardware Revision", "Firmware Version"
    # "Manufacturer","Meter Name", "Meter Model",
    # "Meter Operation Timer", "Number of Phases", "Number of Wires",
    # "Power System", "Nominal Frequency", "Number VTs", "CT Primary", 
    # "CT Secondary",	"Number CTs", "CT Primary", "CT Secondary", 
    # "VT Connection Type", "Energy Pulse Duration", 
    # "Digital Output Association", "Pulse Weight"
]

