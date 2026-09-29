# inverter
# Python program for Single Phase Inverter

Vdc = float(input("Enter DC input voltage (V): "))
cycles = int(input("Enter number of cycles: "))

print("\nSingle Phase Inverter Output:")

for cycle in range(1, cycles + 1):
    print("\nCycle", cycle)
    print("Positive half-cycle: +", Vdc, "V")
    print("Negative half-cycle: -", Vdc, "V")

print("\nInverter operation completed.")
