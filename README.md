Power Cycle the USB connected plug.

Clone this repo into the NUC home user directory : <code>git clone https://github.com/ben-EDT/usb-power.git rts</code>

<code>cd rts</code>

Install requirements : <code>pip3 install -r  power.req</code>

<code>mv power_cycle ../</code>

To power cycle the RTS DUT you can run from ~/ : <code>sudo ./power_cycle</code>

Which has a 1 second pause between power off and power on.

NB: You need to run as root in order to have enough privileges.

* python3 power.py query
* python3 power.py on
* python3 power.py off
* python3 power.py reboot < seconds to wait between power off and power on >
