def F_to_C(temp):
    return (temp - 32) * 5 / 9


def F_to_K(temp):
    return (temp - 32) * 5 / 9 + 273.15


def C_to_F(temp):
    return temp * 9 / 5 + 32


def C_to_K(temp):
    return temp + 273.15


def K_to_C(temp):
    return temp - 273.15


def K_to_F(temp):
    return (temp - 273.15) * 9 / 5 + 32


CONVERSIONS = {
    ("F", "C"): F_to_C,
    ("F", "K"): F_to_K,
    ("C", "F"): C_to_F,
    ("C", "K"): C_to_K,
    ("K", "C"): K_to_C,
    ("K", "F"): K_to_F,
}


def get_temperature():
    while True:
        try:
            return float(input("Enter the temperature value: "))
        except ValueError:
            print("❌ Please enter a valid number.\n")
        except KeyboardInterrupt:
            print("\n👋 Program exited by user.")
            exit()


def get_unit(prompt):
    while True:
        try:
            unit = input(prompt).upper()
            if unit in ("C", "F", "K"):
                return unit
            print("Invalid unit. Please enter C, F, or K.\n")
        except KeyboardInterrupt:
            print("\n👋 Program exited by user.")
            exit()


def main():
    print("=== Temperature Converter ===")
    print("Units: C (Celsius), F (Fahrenheit), K (Kelvin)\n")

    while True:
        temp = get_temperature()
        input_unit = get_unit("Enter the input unit (C, F, K): ")
        output_unit = get_unit("Enter the output unit (C, F, K): ")

        if input_unit == output_unit:
            result = temp
        else:
            result = CONVERSIONS[(input_unit, output_unit)](temp)

        print(f"\n Result: {result:.2f} {output_unit}\n")

        try:
            again = input("Convert another temperature? (y/n): ").lower()
            if again != "y":
                print("\n Goodbye!")
                break
        except KeyboardInterrupt:
            print("\n Program exited by user.")
            break


# run program
main()
