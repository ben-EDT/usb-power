Power Cycle the USB connected plug.

Install "pyusb"

pip3 install -r  power.req


NB: You need to run as root in order to have enough privileges.

* python3 power.py query
* python3 power.py on
* python3 power.py off
* python3 power.py reboot << seconds to wait between off and power on >>


To power cycle the RTS DUT you can also just run:

sudo ./power_cycle

Which has a 1 second pause between power off and power on.
