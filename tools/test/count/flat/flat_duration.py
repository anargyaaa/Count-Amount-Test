from datetime import datetime

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
                "overstay_progressive_time_next": 6,
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
                "overstay_progressive_time_next": 6,
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
                "overstay_affected_user": "MEMBER",
                "overstay_product_member": [],
                "overstay_start": None,
                "overstay_end": None,
                "overstay_start_price": 7000,
                "overstay_next_price": 7000,
                "overstay_progressive_time_start": 1,
                "overstay_progressive_time_next": 6,
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
                "overstay_affected_user": "NON_MEMBER",
                "overstay_product_member": [],
                "overstay_start": None,
                "overstay_end": None,
                "overstay_start_price": 7000,
                "overstay_next_price": 7000,
                "overstay_progressive_time_start": 1,
                "overstay_progressive_time_next": 6,
                "overstay_max_hours": 1,
                "overstay_max_price": 1,
                "period_data": [],
            }
        ]

        self._list_test = [
            self._test_1, self._test_2, self._test_3, self._test_4,
            self._test_5, self._test_6, self._test_7, self._test_8,
            self._test_9, self._test_10, self._test_11, self._test_12,
            self._test_13, self._test_14, self._test_15, self._test_16,
            self._test_17, self._test_18, self._test_19, self._test_20,
            self._test_21, self._test_22, self._test_23, self._test_24,
            self._test_25, self._test_26, self._test_27, self._test_28,
            self._test_29, self._test_30, self._test_31, self._test_32,
            self._test_33, self._test_34,
        ]

    def execute(self):
        for get_test in self._list_test:
            current_vehicle, time_in, time_out, price_payload, expectation = get_test()

            membership_product = expectation.get("membership_product", "")

            count_price = CountPrice(
                time_in=time_in,
                time_out=time_out,
                price_payload=price_payload,
                membership_product=membership_product,
                current_vehicle=current_vehicle
            )
            response: ParkingPriceModel = count_price.execute()
            requirement = expectation['parking_price'] == response.parking_price \
                            and expectation['total_price'] == response.total_amount \
                                and expectation['overstay_price'] == response.overnight_price

            self._print_result(
                test_name=get_test.__name__,
                current_vehicle=current_vehicle,
                price_payload=price_payload,
                time_in=time_in,
                time_out=time_out,
                response=response,
                expectation=expectation,
                membership_product=membership_product,
                passed=requirement
            )

            if not requirement:
                raise Exception(f"Test {get_test.__name__} failed")

    def _print_result(self, test_name, current_vehicle, price_payload,
                       time_in, time_out, response: ParkingPriceModel,
                       expectation, membership_product, passed):
        separator = "=" * 79

        vehicle_name = price_payload.get("vehicle_name", "")
        grace_period = price_payload.get("grace_period", 0)
        overstay_affected_user = price_payload.get("overstay_affected_user", "")

        jam_masuk = datetime.utcfromtimestamp(time_in / 1000 + 7 * 3600).strftime("%H:%M:%S")
        jam_keluar = datetime.utcfromtimestamp(time_out / 1000 + 7 * 3600).strftime("%H:%M:%S")
        lama_parkir_jam = -(-(time_out - time_in) // (3600 * 1000))

        is_overstay = response.overnight_price > 0
        is_affected_user_test = "membership_product" in expectation

        is_grace = (
            not is_affected_user_test
            and response.parking_price == 0
            and response.overnight_price == 0
        )

        parking_display = "Grace" if is_grace else expectation["parking_price"]
        total_display = "Grace" if is_grace else expectation["total_price"]

        print(separator)
        print(f"{'RESULT TEST':^79}")
        print(separator)
        print(f"Test Name        : {test_name}")
        print(f"Vehicle          : {vehicle_name} ({current_vehicle})")
        print(f"Grace Time       : {grace_period} Menit")

        if is_affected_user_test:
            print(f"Affected User    : {overstay_affected_user}")
            print(f"User             : {'Member' if membership_product else 'Casual'}")

        print()
        print(f"Jam Masuk        : {jam_masuk}")
        print(f"Jam Keluar       : {jam_keluar}")
        print(f"Lama Parkir      : {lama_parkir_jam} Jam")
        print(f"Is Overstay      : {'TRUE' if is_overstay else 'FALSE'}")
        print()
        print("Parking Price")
        print(f"    Expected     : {parking_display}")
        print(f"    Calculated   : {response.parking_price}")
        print()
        print("Overstay Price")
        print(f"    Expected     : {expectation['overstay_price']}")
        print(f"    Calculated   : {response.overnight_price}")
        print()
        print("Total Price")
        print(f"    Expected     : {total_display}")
        print(f"    Calculated   : {response.total_amount}")
        print()
        print(f"Status           : {'PASSED' if passed else 'FAILED'}")
        print(separator)
        print()

    
    def _test_1(self):
        expectation = {
            "parking_price": 0,
            "total_price": 0,
            "overstay_price": 0
        }

        current_vehicle = "MT1"

        time_in = 1783987200000
        time_out = 1783987200000
        price_payload = next(
            (item for item in self._base_data if item["vehicle_code"] == "MT1" and item["overstay_affected_user"] == "ALL"),
            {}
        )

        return current_vehicle, time_in, time_out, price_payload, expectation

    def _test_2(self):
        expectation = {
            "parking_price": 0,
            "total_price": 0,
            "overstay_price": 0
        }

        current_vehicle = "MT1"

        time_in = 1783987200000
        time_out = 1783987499000
        price_payload = next(
            (item for item in self._base_data if item["vehicle_code"] == "MT1" and item["overstay_affected_user"] == "ALL"),
            {}
        )

        return current_vehicle, time_in, time_out, price_payload, expectation

    def _test_3(self):
        expectation = {
            "parking_price": 0,
            "total_price": 0,
            "overstay_price": 0
        }

        current_vehicle = "MT1"

        time_in = 1783987200000
        time_out = 1783987500000
        price_payload = next(
            (item for item in self._base_data if item["vehicle_code"] == "MT1" and item["overstay_affected_user"] == "ALL"),
            {}
        )

        return current_vehicle, time_in, time_out, price_payload, expectation

    def _test_4(self):
        expectation = {
            "parking_price": 2000,
            "total_price": 2000,
            "overstay_price": 0
        }

        current_vehicle = "MT1"

        time_in = 1783987200000
        time_out = 1783987501000
        price_payload = next(
            (item for item in self._base_data if item["vehicle_code"] == "MT1" and item["overstay_affected_user"] == "ALL"),
            {}
        )

        return current_vehicle, time_in, time_out, price_payload, expectation

    def _test_5(self):
        expectation = {
            "parking_price": 2000,
            "total_price": 2000,
            "overstay_price": 0
        }

        current_vehicle = "MT1"

        time_in = 1783987200000
        time_out = 1783990800000
        price_payload = next(
            (item for item in self._base_data if item["vehicle_code"] == "MT1" and item["overstay_affected_user"] == "ALL"),
            {}
        )

        return current_vehicle, time_in, time_out, price_payload, expectation

    def _test_6(self):
        expectation = {
            "parking_price": 2000,
            "total_price": 2000,
            "overstay_price": 0
        }

        current_vehicle = "MT1"

        time_in = 1783987200000
        time_out = 1784008799000
        price_payload = next(
            (item for item in self._base_data if item["vehicle_code"] == "MT1" and item["overstay_affected_user"] == "ALL"),
            {}
        )

        return current_vehicle, time_in, time_out, price_payload, expectation

    def _test_7(self):
        expectation = {
            "parking_price": 2000,
            "total_price": 9000,
            "overstay_price": 7000
        }

        current_vehicle = "MT1"

        time_in = 1783987200000
        time_out = 1784008800000
        price_payload = next(
            (item for item in self._base_data if item["vehicle_code"] == "MT1" and item["overstay_affected_user"] == "ALL"),
            {}
        )

        return current_vehicle, time_in, time_out, price_payload, expectation

    def _test_8(self):
        expectation = {
            "parking_price": 2000,
            "total_price": 9000,
            "overstay_price": 7000
        }

        current_vehicle = "MT1"

        time_in = 1783987200000
        time_out = 1784008801000
        price_payload = next(
            (item for item in self._base_data if item["vehicle_code"] == "MT1" and item["overstay_affected_user"] == "ALL"),
            {}
        )

        return current_vehicle, time_in, time_out, price_payload, expectation

    def _test_9(self):
        expectation = {
            "parking_price": 2000,
            "total_price": 9000,
            "overstay_price": 7000
        }

        current_vehicle = "MT1"

        time_in = 1783987200000
        time_out = 1784030399000
        price_payload = next(
            (item for item in self._base_data if item["vehicle_code"] == "MT1" and item["overstay_affected_user"] == "ALL"),
            {}
        )

        return current_vehicle, time_in, time_out, price_payload, expectation

    def _test_10(self):
        expectation = {
            "parking_price": 2000,
            "total_price": 16000,
            "overstay_price": 14000
        }

        current_vehicle = "MT1"

        time_in = 1783987200000
        time_out = 1784030400000
        price_payload = next(
            (item for item in self._base_data if item["vehicle_code"] == "MT1" and item["overstay_affected_user"] == "ALL"),
            {}
        )

        return current_vehicle, time_in, time_out, price_payload, expectation

    def _test_11(self):
        expectation = {
            "parking_price": 2000,
            "total_price": 16000,
            "overstay_price": 14000
        }

        current_vehicle = "MT1"

        time_in = 1783987200000
        time_out = 1784030401000
        price_payload = next(
            (item for item in self._base_data if item["vehicle_code"] == "MT1" and item["overstay_affected_user"] == "ALL"),
            {}
        )

        return current_vehicle, time_in, time_out, price_payload, expectation

    def _test_12(self):
        expectation = {
            "parking_price": 2000,
            "total_price": 23000,
            "overstay_price": 21000
        }

        current_vehicle = "MT1"

        time_in = 1783987200000
        time_out = 1784073599000
        price_payload = next(
            (item for item in self._base_data if item["vehicle_code"] == "MT1" and item["overstay_affected_user"] == "ALL"),
            {}
        )

        return current_vehicle, time_in, time_out, price_payload, expectation

    def _test_13(self):
        expectation = {
            "parking_price": 2000,
            "total_price": 30000,
            "overstay_price": 28000
        }

        current_vehicle = "MT1"

        time_in = 1783987200000
        time_out = 1784073600000
        price_payload = next(
            (item for item in self._base_data if item["vehicle_code"] == "MT1" and item["overstay_affected_user"] == "ALL"),
            {}
        )

        return current_vehicle, time_in, time_out, price_payload, expectation

    def _test_14(self):
        expectation = {
            "parking_price": 4000,
            "total_price": 32000,
            "overstay_price": 28000
        }

        current_vehicle = "MT1"

        time_in = 1783987200000
        time_out = 1784073601000
        price_payload = next(
            (item for item in self._base_data if item["vehicle_code"] == "MT1" and item["overstay_affected_user"] == "ALL"),
            {}
        )

        return current_vehicle, time_in, time_out, price_payload, expectation

   
    def _test_15(self):
        expectation = {
            "parking_price": 0,
            "total_price": 0,
            "overstay_price": 0
        }

        current_vehicle = "MB1"

        time_in = 1783987200000
        time_out = 1783987200000
        price_payload = next(
            (item for item in self._base_data if item["vehicle_code"] == "MB1"),
            {}
        )

        return current_vehicle, time_in, time_out, price_payload, expectation

    def _test_16(self):
        expectation = {
            "parking_price": 0,
            "total_price": 0,
            "overstay_price": 0
        }

        current_vehicle = "MB1"

        time_in = 1783987200000
        time_out = 1783987499000
        price_payload = next(
            (item for item in self._base_data if item["vehicle_code"] == "MB1"),
            {}
        )

        return current_vehicle, time_in, time_out, price_payload, expectation

    def _test_17(self):
        expectation = {
            "parking_price": 0,
            "total_price": 0,
            "overstay_price": 0
        }

        current_vehicle = "MB1"

        time_in = 1783987200000
        time_out = 1783987500000
        price_payload = next(
            (item for item in self._base_data if item["vehicle_code"] == "MB1"),
            {}
        )

        return current_vehicle, time_in, time_out, price_payload, expectation

    def _test_18(self):
        expectation = {
            "parking_price": 4000,
            "total_price": 4000,
            "overstay_price": 0
        }

        current_vehicle = "MB1"

        time_in = 1783987200000
        time_out = 1783987501000
        price_payload = next(
            (item for item in self._base_data if item["vehicle_code"] == "MB1"),
            {}
        )

        return current_vehicle, time_in, time_out, price_payload, expectation

    def _test_19(self):
        expectation = {
            "parking_price": 4000,
            "total_price": 4000,
            "overstay_price": 0
        }

        current_vehicle = "MB1"

        time_in = 1783987200000
        time_out = 1783990800000
        price_payload = next(
            (item for item in self._base_data if item["vehicle_code"] == "MB1"),
            {}
        )

        return current_vehicle, time_in, time_out, price_payload, expectation

    def _test_20(self):
        expectation = {
            "parking_price": 4000,
            "total_price": 4000,
            "overstay_price": 0
        }

        current_vehicle = "MB1"

        time_in = 1783987200000
        time_out = 1784008799000
        price_payload = next(
            (item for item in self._base_data if item["vehicle_code"] == "MB1"),
            {}
        )

        return current_vehicle, time_in, time_out, price_payload, expectation

    def _test_21(self):
        expectation = {
            "parking_price": 4000,
            "total_price": 14000,
            "overstay_price": 10000
        }

        current_vehicle = "MB1"

        time_in = 1783987200000
        time_out = 1784008800000
        price_payload = next(
            (item for item in self._base_data if item["vehicle_code"] == "MB1"),
            {}
        )

        return current_vehicle, time_in, time_out, price_payload, expectation

    def _test_22(self):
        expectation = {
            "parking_price": 4000,
            "total_price": 14000,
            "overstay_price": 10000
        }

        current_vehicle = "MB1"

        time_in = 1783987200000
        time_out = 1784008801000
        price_payload = next(
            (item for item in self._base_data if item["vehicle_code"] == "MB1"),
            {}
        )

        return current_vehicle, time_in, time_out, price_payload, expectation

    def _test_23(self):
        expectation = {
            "parking_price": 4000,
            "total_price": 14000,
            "overstay_price": 10000
        }

        current_vehicle = "MB1"

        time_in = 1783987200000
        time_out = 1784030399000
        price_payload = next(
            (item for item in self._base_data if item["vehicle_code"] == "MB1"),
            {}
        )

        return current_vehicle, time_in, time_out, price_payload, expectation

    def _test_24(self):
        expectation = {
            "parking_price": 4000,
            "total_price": 24000,
            "overstay_price": 20000
        }

        current_vehicle = "MB1"

        time_in = 1783987200000
        time_out = 1784030400000
        price_payload = next(
            (item for item in self._base_data if item["vehicle_code"] == "MB1"),
            {}
        )

        return current_vehicle, time_in, time_out, price_payload, expectation

    def _test_25(self):
        expectation = {
            "parking_price": 4000,
            "total_price": 24000,
            "overstay_price": 20000
        }

        current_vehicle = "MB1"

        time_in = 1783987200000
        time_out = 1784030401000
        price_payload = next(
            (item for item in self._base_data if item["vehicle_code"] == "MB1"),
            {}
        )

        return current_vehicle, time_in, time_out, price_payload, expectation

    def _test_26(self):
        expectation = {
            "parking_price": 4000,
            "total_price": 34000,
            "overstay_price": 30000
        }

        current_vehicle = "MB1"

        time_in = 1783987200000
        time_out = 1784073599000
        price_payload = next(
            (item for item in self._base_data if item["vehicle_code"] == "MB1"),
            {}
        )

        return current_vehicle, time_in, time_out, price_payload, expectation

    def _test_27(self):
        expectation = {
            "parking_price": 4000,
            "total_price": 44000,
            "overstay_price": 40000
        }

        current_vehicle = "MB1"

        time_in = 1783987200000
        time_out = 1784073600000
        price_payload = next(
            (item for item in self._base_data if item["vehicle_code"] == "MB1"),
            {}
        )

        return current_vehicle, time_in, time_out, price_payload, expectation

    def _test_28(self):
        expectation = {
            "parking_price": 8000,
            "total_price": 48000,
            "overstay_price": 40000
        }

        current_vehicle = "MB1"

        time_in = 1783987200000
        time_out = 1784073601000
        price_payload = next(
            (item for item in self._base_data if item["vehicle_code"] == "MB1"),
            {}
        )

        return current_vehicle, time_in, time_out, price_payload, expectation

    def _test_29(self):
        expectation = {
            "parking_price": 0,
            "total_price": 7000,
            "overstay_price": 7000,
            "membership_product": "MBR-001",
        }

        current_vehicle = "MT1"

        time_in = 1783987200000
        time_out = 1784008800000
        price_payload = next(
            (item for item in self._base_data if item["vehicle_code"] == "MT1" and item["overstay_affected_user"] == "ALL"),
            {}
        )

        return current_vehicle, time_in, time_out, price_payload, expectation

    def _test_30(self):
        expectation = {
            "parking_price": 2000,
            "total_price": 9000,
            "overstay_price": 7000,
            "membership_product": "",
        }

        current_vehicle = "MT1"

        time_in = 1783987200000
        time_out = 1784008800000
        price_payload = next(
            (item for item in self._base_data if item["vehicle_code"] == "MT1" and item["overstay_affected_user"] == "ALL"),
            {}
        )

        return current_vehicle, time_in, time_out, price_payload, expectation

    def _test_31(self):
        expectation = {
            "parking_price": 0,
            "total_price": 7000,
            "overstay_price": 7000,
            "membership_product": "MBR-001",
        }

        current_vehicle = "MT1"

        time_in = 1783987200000
        time_out = 1784008800000
        price_payload = next(
            (item for item in self._base_data if item["vehicle_code"] == "MT1" and item["overstay_affected_user"] == "MEMBER"),
            {}
        )

        return current_vehicle, time_in, time_out, price_payload, expectation

    def _test_32(self):
        expectation = {
            "parking_price": 2000,
            "total_price": 2000,
            "overstay_price": 0,
            "membership_product": "",
        }

        current_vehicle = "MT1"

        time_in = 1783987200000
        time_out = 1784008800000
        price_payload = next(
            (item for item in self._base_data if item["vehicle_code"] == "MT1" and item["overstay_affected_user"] == "MEMBER"),
            {}
        )

        return current_vehicle, time_in, time_out, price_payload, expectation

    def _test_33(self):
        expectation = {
            "parking_price": 0,
            "total_price": 0,
            "overstay_price": 0,
            "membership_product": "MBR-001",
        }

        current_vehicle = "MT1"

        time_in = 1783987200000
        time_out = 1784008800000
        price_payload = next(
            (item for item in self._base_data if item["vehicle_code"] == "MT1" and item["overstay_affected_user"] == "NON_MEMBER"),
            {}
        )

        return current_vehicle, time_in, time_out, price_payload, expectation

    def _test_34(self):
        expectation = {
            "parking_price": 2000,
            "total_price": 9000,
            "overstay_price": 7000,
            "membership_product": "",
        }

        current_vehicle = "MT1"

        time_in = 1783987200000
        time_out = 1784008800000
        price_payload = next(
            (item for item in self._base_data if item["vehicle_code"] == "MT1" and item["overstay_affected_user"] == "NON_MEMBER"),
            {}
        )

        return current_vehicle, time_in, time_out, price_payload, expectation