from dataclasses import dataclass


@dataclass
class ParkingPriceModel:
    amount: int = 0
    total_amount: int = 0

    price: int = 0
    parking_price: int = 0
    time_in: int = 0
    time_out: int = 0
    total_hours: int = 0

    fine: int = 0

    price_payload: int = 0
    discount: int = 0

    overnight_days: int = 0
    overnight_price: int = 0

    parking_price_payload: int = 0
    overnight_price_payload: int = 0

    count_hours: dict = None
    vehicle_name: str = ''

    grace_period: bool = False