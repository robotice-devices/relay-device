
# Relay module

Controls relay module with GPIO pins

## Example usage

### BeagleBone - turn on relay at GPIO #44


    python driver.py -a armv7l -p 44 -m on


### Raspberry Pi - turn off relay at GPIO #4 on board


    python driver.py -a armv6l -p 4 -m off


### Raspberry Pi - turn on relay at GPIO #18 on expansion board


    python driver.py -a armv6l -p BMC18 -m on -r on

