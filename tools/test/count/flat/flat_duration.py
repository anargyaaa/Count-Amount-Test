from model.price import ParkingPriceModel
from utility.count_price import CountPrice


class FlatDurationTest:
    def __init__(self):
        self._base_data = [
            {
                "fine": 0,
                "fine_type": "",
                "grace_period": 5,
                "initial_time": 0,
                "max_hour": 0,
                "min_hour": 0,
                "discount": 0,
                "max_price": 0,
                "next_price": 0,
                "overnight_price": 7000,
                "price": 2000,
                "stay_time": 0,
                "type": "FLAT",
                "count_type": "INCREMENT",
                "vehicle_code": "MT1",
                "vehicle_name": "Motor",
                "overstay_type": "PROGRESSIVE",
                "overstay_parameter": "DURATION",
                "overstay_duration": 6,
                "overstay_affected_user": "ALL",
                "overstay_product_member": [],
                "overstay_start": None,
                "overstay_end": None,
                "overstay_start_price": 7000,
                "overstay_next_price": 7000,
                "overstay_progressive_time_start": 1,
                "overstay_progressive_time_next": 1,
                "overstay_max_hours": 1,
                "overstay_max_price": 1,
                "period_data": [],
            },
            {
                "fine": 0,
                "fine_type": "",
                "grace_period": 5,
                "initial_time": 0,
                "max_hour": 0,
                "min_hour": 0,
                "discount": 0,
                "max_price": 0,
                "next_price": 0,
                "overnight_price": 10000,
                "price": 4000,
                "stay_time": 0,
                "type": "FLAT",
                "count_type": "INCREMENT",
                "vehicle_code": "MB1",
                "vehicle_name": "Mobil",
                "overstay_type": "PROGRESSIVE",
                "overstay_parameter": "DURATION",
                "overstay_duration": 6,
                "overstay_affected_user": "ALL",
                "overstay_product_member": [],
                "overstay_start": None,
                "overstay_end": None,
                "overstay_start_price": 10000,
                "overstay_next_price": 10000,
                "overstay_progressive_time_start": 1,
                "overstay_progressive_time_next": 1,
                "overstay_max_hours": 1,
                "overstay_max_price": 1,
                "period_data": [],
            }
        ]

        self._list_test = [
            self._test_one,
            self._test_seven
        ]

    def execute(self):
        for get_test in self._list_test:
            current_vehicle, time_in, time_out, price_payload, expectation = get_test()
            count_price = CountPrice(
                time_in=time_in,
                time_out=time_out,
                price_payload=price_payload,
                current_vehicle=current_vehicle
            )
            response: ParkingPriceModel = count_price.execute()
            requirement = expectation['parking_price'] == response.parking_price \
                            and expectation['total_price'] == response.total_amount \
                                and expectation['overstay_price'] == response.overnight_price
            
            print(f"""
Result test:
    Counted Parking Price = {response.parking_price}
    Expected Parking Price = {expectation['parking_price']}

    Counted Total Price = {response.total_amount}
    Expected Total Price = {expectation['total_price']}

    Counted Overstay Price = {response.overnight_price}
    Expected Overstay Price = {expectation['overstay_price']}
            """)
            
            if not requirement:
                raise Exception(f"Test {get_test.__name__} failed")
            
            print(f"Test {get_test.__name__} success")
            
            

    def _test_one(self):
        expectation = {
            "parking_price": 0,
            "total_price": 0,
            "overstay_price": 0
        }

        current_vehicle = "MT1"

        time_in = 1783987200000
        time_out = 1783987200000
        price_payload = next(
            (item for item in self._base_data if item["vehicle_code"] == "MT1"),
            {}
        )

        return current_vehicle, time_in, time_out, price_payload, expectation

    def _test_seven(self):
        expectation = {
            "parking_price": 2000,
            "total_price": 9000,
            "overstay_price": 7000
        }

        current_vehicle = "MT1"

        time_in = 1783987200000
        time_out = 1784008800000
        price_payload = next(
            (item for item in self._base_data if item["vehicle_code"] == "MT1"),
            {}
        )

        return current_vehicle, time_in, time_out, price_payload, expectation