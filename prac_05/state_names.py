"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
Created on 16-12-2021 by Richard Reynard
"""

STATES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
          "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(STATES)

state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in STATES:
        print(state_code, "is", STATES[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

for state_code in STATES:
    print(f"{state_code:3} is {STATES[state_code]}")
