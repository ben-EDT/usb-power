Power Cycle the USB connected plug.

Clone this repo into the NUC home user directory : <code>git clone https://github.com/ben-EDT/usb-power.git rts</code>

<code>cd rts</code>

Install requirements : <code>pip3 install -r  requirements.txt</code>

<code>mv power_cycle ../</code>

To power cycle the RTS DUT you can run from ~/ : <code>sudo ./power_cycle</code>

Which has a 1-second pause between power off and power on.

NB: You need to run as root in order to have enough privileges.

* python3 power.py query
* python3 power.py toggle
* python3 power.py state
* python3 power.py cycle

You can pass an integer or float to "cycle" to determine the pause (in seconds) between power off and power on. Defaults to 1.
