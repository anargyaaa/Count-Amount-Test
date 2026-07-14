from utility.time import TimeUtility


class CountUtility:
    @staticmethod
    def count_hours_with_data(time_in: int,
                              time_out: int) -> dict:

        hours = 1
        total_minutes = TimeUtility.get_different_time_in_minutes(
            start=time_in, end=time_out)
        overstay = TimeUtility.get_different_time_in_minutes(
            start=time_in, end=time_out, overstay=True)

        data = {"hours": 0, "minutes": total_minutes, "count": 1, "round_up": 1,
                "hours_overstay": 0, "minutes_overstay": overstay, "round_overstay": 0}

        if total_minutes > 60:
            # Get hours with floor division
            _hours = total_minutes // 60
            _hours_overstay = overstay // 60
            # Get additional minutes with modulus
            _minutes = total_minutes % 60
            _minutes_overstay = overstay % 60

            hours = TimeUtility.get_different_time_in_hours(
                start=time_in, end=time_out)
            hours_overstay = TimeUtility.get_different_time_in_hours(
                start=time_in, end=time_out, overstay=True)

            data = {"hours": _hours, "minutes": _minutes, "count": hours, "round_up": hours,
                    "hours_overstay": _hours_overstay, "minutes_overstay": _minutes_overstay, "round_overstay": hours_overstay}
        return data