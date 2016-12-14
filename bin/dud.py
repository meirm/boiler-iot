#!/usr/bin/env python
"""Simple control of Relay
Code by "Meir Michanie"
Turned structured code to OO class.

Original code from "Stefan Mavrodiev"
2014, Olimex LTD
email "support@olimex.com"
"""

import os
import sys

if not os.getegid() == 0:
    sys.exit('Script must be run as root')


from pyA20.gpio import gpio
from pyA20.gpio import port

__author__ = "Meir Michanie"
__copyright__ = "Copyright 2016, RIUNX"
__credits__ = ["Meir Michanie"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = __author__
__email__ = "meirm@riunx.com"

relayPort = port.PA6
state = 0

gpio.init()
gpio.setcfg(relayPort, gpio.OUTPUT)

def setRelay(relaySet):
    gpio.output(relayPort,relaySet)
    return(relaySet)

def statusRelay():
    state = gpio.input(relayPort)
    return(state)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print statusRelay()
    else:
        relaySet=int(sys.argv[1])
        try:
            setRelay(relaySet)
            print ("%d"%(relaySet))
        except:
            print ("-1")
