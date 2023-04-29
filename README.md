# MAC Changer

A Python script to change the MAC address of a specified network interface.

## Requirements

* Python 3.x
* `optparse` library
* `re` library

## Usage

The script takes two command-line arguments: `-c` (or `--class`) to specify the network interface class to change, and `-m` (or `--mac`) to specify the new MAC address.

Example usage:

```
python3 mac_changer.py -c eth0 -m 00:11:22:33:44:55
```

## Future Improvements

The following improvements could be made to the script in the future:

* Add a network scanner to get the MAC address of the host network automatically.
* Automate the changing of the MAC address based on the host network device.