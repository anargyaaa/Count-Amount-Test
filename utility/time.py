import math
from datetime import datetime


class TimeUtility:
    @staticmethod
    def get_different_time_in_minutes(start: int,
                                      end: int,
                                      overstay: bool = False) -> int:
        difference = end - start
        # Overstay
        if overstay:
            difference = math.floor(difference / 1000 / 60)
        # Normal counting
        else:
            difference = math.ceil(difference / 1000 / 60)
        return difference

    @staticmethod
    def get_different_time_in_hours(start: int,
                                    end: int,
                                    overstay: bool = False) -> int:
        difference = end - start
        # Overstay
        if overstay:
            difference = math.floor(difference / 1000 / 60 / 60)
        # Normal counting
        else:
            difference = math.ceil(difference / 1000 / 60 / 60)
        return difference
    
    @staticmethod
    def get_local_time() -> str:
        """Get local timezone name."""
        try:
            # Get current local timezone
            local_tz = datetime.now().astimezone().tzinfo
            return str(local_tz.tzname(None))
        except Exception:
            return "WIB"  # Default to WIB if unable to get timezone