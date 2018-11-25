# -*- coding: utf-8 -*-
import machine
import network
import utime
from config import Config
from machine import Pin

sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)
# Active sta_if
sta_if.active(True)

sta_if.connect(Config.WIFI_SSID, Config.WIFI_PASSWD)
pin_status = Pin(Config.STATUS_LED, Pin.OUT)
    while not sta_if.isconnected():
        pin_status.off()    # Blue LED on board, reversed.
        utime.sleep(1.0)
        pin_status.on()

    pin_status.off()    # off() = light on
