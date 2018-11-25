# Keng Finder Client

A simple device made by [ESP8266](https://www.espressif.com/zh-hans/products/hardware/esp8266ex/overview) and some sensors.

Firmware written by [MicroPython](https://micropython.org/).

<img src="https://raw.githubusercontent.com/lvidarte/esp8266/master/nodemcu_pins.png">

### Dev log

#### Deploying MicroPython:

Install esptool first.
```bash
pip install esptool
```

Erase flash with the command:
```bash
esptool.py --port /dev/tty.SLAB_USBtoUART erase_flash
```

And then deploy the new firmware using:
```bash
esptool.py --port /dev/tty.SLAB_USBtoUART --baud 115200 write_flash --flash_size=detect 0 ~/Downloads/esp8266-20180511-v1.9.4.bin
```

Deploy your code to ESP8266
```bash
ampy -p /dev/tty.SLAB_USBtoUART put ...
```