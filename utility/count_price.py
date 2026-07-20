from model.price import ParkingPriceModel
from spnapiutilities.builders.parking_amount_builder import ParkingAmountBuilder
from spnapiutilities.core.price.price_model import PriceModel
from utility.count import CountUtility
from utility.time import TimeUtility


class CountPrice:
    '''
    Count price and amount goes here

    Purpose:
    - Parking and overstay
    '''

    def __init__(self,
                 time_in: int,
                 time_out: int,
                 price_payload: dict,
                 membership_product: str = '',
                 current_vehicle: str = ''):

        self.time_in = time_in
        self.price_payload = price_payload
        self.membership_product = membership_product
        self.current_vehicle = current_vehicle
        self.time_out = time_out

        self.worker_name = self.__class__.__name__

    def execute(self) -> ParkingPriceModel:
        try:
            # Validate - time difference
            if self.time_in > self.time_out:
                raise ValueError(
                    f"{self.worker_name} - Terjadi kesalahan pada setting waktu!")

            # Get - count hours
            count_hours = CountUtility.count_hours_with_data(
                time_in=int(self.time_in),
                time_out=int(self.time_out)
            )

            # Init - Variable Adds
            vehicle_name = self.price_payload.get('vehicle_name', '') \
                if not self.current_vehicle \
                else self.current_vehicle

            # Init - Parking price model
            parking_model = ParkingPriceModel(time_out=self.time_out,
                                              vehicle_name=vehicle_name)

            # Get - Price model libs
            price_model = self._get_price_model()

            # Init - Counting parking amount libs
            count_total_payment = ParkingAmountBuilder(model=price_model)
            count_total_payment = count_total_payment.build()
            if not count_total_payment:
                return parking_model

            # Override - Payload inside parking price model
            parking_model.amount = count_total_payment['parking']['amount']
            parking_model.price = count_total_payment['price']
            parking_model.total_amount = count_total_payment['total_amount']
            parking_model.time_in = self.time_in
            parking_model.time_out = self.time_out
            parking_model.total_hours = count_total_payment['total_hours']
            parking_model.discount = 0
            parking_model.parking_price = count_total_payment['parking']['amount']
            parking_model.overnight_price = count_total_payment['overnight_price']
            parking_model.grace_period = count_total_payment['grace_period'] \
                if count_total_payment['amount'] \
                or count_total_payment['overnight_price'] \
                else True
            parking_model.count_hours = count_hours

            return parking_model

        except Exception as e:
            import traceback
            traceback.print_exc()
            raise e

    def _get_price_model(self) -> PriceModel:
        # Init - Price model libs
        price_model = PriceModel()

        # Price model - Setter
        price_model.set_id(
            self.price_payload.get("id"))
        price_model.set_is_membership(
            self.membership_product)
        price_model.set_time_in(
            self.time_in)
        price_model.set_time_out(
            self.time_out)
        price_model.set_total_hours()
        price_model.set_price(
            self.price_payload.get("price"))
        price_model.set_price_type(
            self.price_payload.get('type'))
        price_model.set_count_type(
            self.price_payload.get('count_type'))
        price_model.set_grace_period(
            self.price_payload.get("grace_period") or 0)
        price_model.set_start_price(
            self.price_payload.get('price'))
        price_model.set_next_price(
            self.price_payload.get('next_price'))
        price_model.set_max_price(
            self.price_payload.get('max_price'))
        price_model.set_next_hours(
            self.price_payload.get('stay_time'))
        price_model.set_start_hours(
            self.price_payload.get("initial_time"))
        price_model.set_max_hours(
            self.price_payload.get("max_hour"))
        price_model.set_overstay_price(
            self.price_payload.get("overnight_price")
            if self.price_payload.get('overnight_price')
            else 0)
        price_model.set_overstay_affected_user(
            self.price_payload.get("overstay_affected_user"))
        price_model.set_overstay_start(self.price_payload.get(
            "overstay_start") if self.price_payload.get("overstay_start") else None)
        price_model.set_overstay_end(
            self.price_payload.get("overstay_end")
            if self.price_payload.get("overstay_end")
            else None)
        price_model.set_overstay_duration(
            self.price_payload.get("overstay_duration"))
        price_model.set_period_data(
            self.price_payload.get("period_data"))
        price_model.set_overstay_parameter(
            self.price_payload.get('overstay_parameter'))
        price_model.set_overstay_type(
            self.price_payload.get('overstay_type'))
        price_model.set_overstay_progressive_time_start(
            self.price_payload.get('overstay_progressive_time_start'))
        price_model.set_overstay_progressive_time_next(
            self.price_payload.get('overstay_progressive_time_next'))
        price_model.set_overstay_start_price(
            self.price_payload.get('overstay_start_price'))
        price_model.set_overstay_next_price(
            self.price_payload.get('overstay_next_price'))
        price_model.set_overstay_max_price(
            self.price_payload.get('overstay_max_price'))
        price_model.set_overstay_max_hours(
            self.price_payload.get('overstay_max_hours'))
        price_model.set_overstay_product_member(
            self.price_payload.get('overstay_product_member'))
        # Get timezone
        price_model.set_timezone(
            TimeUtility.get_local_time())

        return price_model
