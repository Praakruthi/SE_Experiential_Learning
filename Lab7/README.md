
# Lab 7 - Fuzz Testing for Input Validation Bugs

## Objective

To explore fuzz testing as a security and quality assurance
technique using the Hypothesis library in Python.

The experiment focuses on identifying and fixing input
validation bugs in a Parking Fee application.

## Technologies Used

- Python 3.8+
- Hypothesis
- Pytest
- Regular Expressions

## Project Structure

```text
Lab7/
│
├── parking_fee.py
├── test_parking_fee.py
├── README.md
└── screenshots/
    ├── 01_original_output.png
    ├── 02_failing_tests.png
    ├── 03_fixed_application.png
    └── 04_passing_tests.png
```

## Functions Tested

### 1. minutes_parked()

Calculates parking duration in minutes using entry and exit
times.

### 2. hourly_rate()

Returns the parking rate based on the vehicle type:
- Bike: 10
- Car: 30
- Truck: 60

### 3. format_plate()

Formats a vehicle registration number into the expected
two-letter, two-digit, two-letter, four-digit structure.

## Testing Methodology

Hypothesis was used to generate random Unicode strings and
None values to identify unexpected input-related failures.

The following edge cases were investigated:

- Empty strings
- Invalid time formats
- Invalid vehicle types
- Incorrect registration numbers
- Unexpected data types
- None values
- Malformed inputs

## Bugs Identified and Fixed

| Function | Issue | Fix |
|---|---|---|
| minutes_parked | Invalid time input | Input and time validation |
| hourly_rate | Unknown vehicle type | Safe dictionary lookup |
| format_plate | Invalid registration number | Format validation |

Invalid inputs return None instead of causing unexpected
exceptions.

## Execution Instructions

Install dependencies:

```bash
python -m pip install hypothesis pytest
```

Run the application:

```bash
python parking_fee.py
```

Run the tests:

```bash
python -m pytest test_parking_fee.py -v
```

## Results

The original application was tested using Hypothesis to
identify input validation bugs.

After implementing defensive input validation, the
application was tested again.

All seven tests passed in the final verification.

## Screenshots

1. Original application output
2. Failing tests on original application
3. Fixed application output
4. Passing tests after fixes

