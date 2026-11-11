
from hypothesis import given, strategies as st
from parking_fee import minutes_parked, hourly_rate, format_plate


# Test 1: Fuzz testing minutes_parked()
@given(st.text() | st.none())
def test_minutes_parked_no_crash(s):
    try:
        minutes_parked(s)
    except Exception as e:
        assert False, f"minutes_parked crashed with input {s!r}: {e}"


# Test 2: Fuzz testing hourly_rate()
@given(st.text() | st.none())
def test_hourly_rate_no_crash(s):
    try:
        hourly_rate(s)
    except Exception as e:
        assert False, f"hourly_rate crashed with input {s!r}: {e}"


# Test 3: Fuzz testing format_plate()
@given(st.text() | st.none())
def test_format_plate_no_crash(s):
    try:
        format_plate(s)
    except Exception as e:
        assert False, f"format_plate crashed with input {s!r}: {e}"


# Additional functional tests for valid inputs

def test_minutes_parked_valid():
    assert minutes_parked("09:30-11:45") == 135


def test_hourly_rate_valid():
    assert hourly_rate("car") == 30
    assert hourly_rate("BIKE") == 10
    assert hourly_rate("Truck") == 60


def test_format_plate_valid():
    assert format_plate("ka01ab1234") == "KA 01 AB 1234"


# Additional tests for invalid inputs

def test_invalid_inputs():
    assert minutes_parked("invalid") is None
    assert hourly_rate("plane") is None
    assert format_plate("123") is None
