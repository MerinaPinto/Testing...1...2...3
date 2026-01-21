import conversion 

def test_celsius_to_fahrenheit():
    assert conversion.C_to_F(0) == 32.00


def test_fahrenheit_to_celsius():
    assert conversion.F_to_C(212) == 100.00


def test_kelvin_to_celsius():
    assert conversion.K_to_C(273.15) == 0.00

def test_same_unit_conversion():
    assert conversion.C_to_C(25) == 25.00


def test_invalid_temperature():
    assert conversion.C_to_F("abc") == "Invalid temperature input"

def test_invalid_unit():
    assert conversion(80, "C", "Z") == "Invalid unit input"

def test_freezing_and_boiling_points():
    assert conversion.C_to_K(0) == 273.15
    assert conversion.C_to_F(100) == 212.00
