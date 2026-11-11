
import re

RATES = {
    "bike": 10,
    "car": 30,
    "truck": 60
}


# Function 1: Calculate parking duration in minutes
def minutes_parked(times):
    if not isinstance(times, str):
        return None

    times = times.strip()

    pattern = (
        r"^((?:[01]\d|2[0-3]):[0-5]\d)-"
        r"((?:[01]\d|2[0-3]):[0-5]\d)$"
    )

    if not re.fullmatch(pattern, times):
        return None

    try:
        entry, exit_time = times.split("-")

        h1, m1 = map(int, entry.split(":"))
        h2, m2 = map(int, exit_time.split(":"))

        entry_minutes = h1 * 60 + m1
        exit_minutes = h2 * 60 + m2

        if exit_minutes < entry_minutes:
            return None

        return exit_minutes - entry_minutes

    except (ValueError, AttributeError):
        return None


# Function 2: Get hourly parking rate
def hourly_rate(vehicle):
    if not isinstance(vehicle, str):
        return None

    vehicle = vehicle.strip().lower()

    return RATES.get(vehicle)


# Function 3: Format vehicle registration number
def format_plate(plate):
    if not isinstance(plate, str):
        return None

    p = plate.strip().upper()

    if not re.fullmatch(r"[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}", p):
        return None

    return p[0:2] + " " + p[2:4] + " " + p[4:6] + " " + p[6:10]


# Main application
def main():
    print("==== Running minutes_parked ====")
    user_input = input("Enter entry and exit time (e.g. 09:30-11:45): ")
    result = minutes_parked(user_input)
    print("Minutes Parked:", result)

    print("\n==== Running hourly_rate ====")
    user_input = input("Enter vehicle type (bike/car/truck): ")
    result = hourly_rate(user_input)
    print("Hourly Rate:", result)

    print("\n==== Running format_plate ====")
    user_input = input("Enter a number plate (e.g. ka01ab1234): ")
    result = format_plate(user_input)
    print("Formatted Plate:", result)


if __name__ == "__main__":
    main()
