import pytest
from parking_fee import parking_fee, find_slot, monthly_pass


def test_parking_fee_free_stay():
    assert parking_fee("car", 30, False, False) == 0


def test_parking_fee_rounds_up_to_next_hour():
    assert parking_fee("bike", 61, False, False) == 20


def test_parking_fee_exact_hour():
    assert parking_fee("car", 60, False, False) == 30


def test_parking_fee_ev_discount():
    assert parking_fee("car", 60, True, False) == 15


def test_parking_fee_truck_no_ev_discount():
    assert parking_fee("truck", 60, True, False) == 60


def test_parking_fee_lost_ticket_surcharge():
    assert parking_fee("bike", 60, False, True) == 210


def test_parking_fee_unknown_vehicle():
    with pytest.raises(ValueError, match="unknown vehicle"):
        parking_fee("bus", 60, False, False)


def test_parking_fee_negative_duration():
    with pytest.raises(ValueError, match="invalid duration"):
        parking_fee("car", -1, False, False)


def test_find_slot_full():
    assert find_slot("car", 0, True) == "full"


def test_find_slot_disabled_ground_floor():
    assert find_slot("car", 2, True) == "ground floor"


def test_find_slot_truck_basement():
    assert find_slot("truck", 2, False) == "basement"


def test_find_slot_any_floor():
    assert find_slot("bike", 2, False) == "any floor"


def test_monthly_pass_bike():
    assert monthly_pass("bike", False) == 500


def test_monthly_pass_bike_resident():
    assert monthly_pass("bike", True) == 400


def test_monthly_pass_car():
    assert monthly_pass("car", False) == 1500


def test_monthly_pass_car_resident():
    assert monthly_pass("car", True) == 1200


def test_monthly_pass_unsupported_vehicle():
    with pytest.raises(ValueError, match="no pass for this vehicle"):
        monthly_pass("truck", False)
