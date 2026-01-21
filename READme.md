Test Case 1	Descrption	"	Prerequisites"	Test steps	"	Expected results"	"	Actual results"	Status
"Celsius_to_Fahrenheit
"	Verify correct conversion from Celsius to Fahrenheit	Program is running, valid input expected	User inputs 0 - selects C - selects F	Program outputs 32.00 F	Filled during testing	Pass / Fail
Fahrenheit_to_Celsius	Verify correct conversion from Fahrenheit to Celsius	Program is running	User inputs 212 - selects F - selects C	Program outputs 100.00 C	Filled during testing	Pass / Fail
Kelvin_to_Celsius	Verify correct conversion from Kelvin to Celsius	Program is running	"
User inputs 273.15 - selects K - selects C"	Program outputs 0.00 C	Filled during testing	Pass / Fail
Same_Unit_Conversion	Verify conversion when input and output units are the same	Program is running	User inputs 25 - selects C - selects C	Program outputs 25.00 C	Filled during testing	Pass / Fail
Invalid_Temperature	Verify non-numeric temperature input is rejected	Program is running	User inputs letter - re-enters valid number	Error message shown and re-prompt occurs	Filled during testing	Pass / Fail
Invalid_Unit_Input	Verify invalid unit input is rejected	Program is running	User inputs 80-selects unit Z -re-enters valid unit		Filled during testing	Pass / Fail
Exit	Verify program exits gracefully on Ctrl+C	Program is running	User presses Ctrl+C during input	Program exits with friendly message	Filled during testing	Pass / Fail
