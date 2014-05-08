# Relay module

Controls relay module with GPIO pins, the Adafruit GPIO libraries are needed.

## Example usage

BeagleBone - turn on relay at GPIO P8_10

    > python driver.py -p P8_10 -m on


BeagleBone - turn on reverse-logic relay at GPIO P8_10 

    > python driver.py -p P8_10 -m on -r on


Raspberry Pi - turn off relay at GPIO #4 on board

    > python driver.py -p 4 -m off


Raspberry Pi - turn on relay at GPIO #18 on expansion board

    > python driver.py -p BMC18 -m on -r on