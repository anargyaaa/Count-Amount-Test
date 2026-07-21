class PriceList:
    @staticmethod
    def get_price_flat_duration():
        return [
            {
                "fine": 0,
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
                "overstay_parameter": "DURATION",
                "overstay_duration": 6,
                "overstay_affected_user": "ALL",
                "overstay_product_member": [],
                "overstay_start": "",
                "overstay_end": ""
            },
            {
                "fine": 0,
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
                "overstay_parameter": "DURATION",
                "overstay_duration": 6,
                "overstay_affected_user": "ALL",
                "overstay_product_member": [],
                "overstay_start": "",
                "overstay_end": ""
            }
        ]

    @staticmethod
    def get_price_flat_range():
        return [
            {
                "fine": 0,
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
                "overstay_parameter": "TIME",
                "overstay_duration": None,
                "overstay_affected_user": "ALL",
                "overstay_product_member": [],
                "overstay_start": "00: 00",
                "overstay_end": "06: 00"
            },
            {
                "fine": 0,
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
                "overstay_parameter": "TIME",
                "overstay_duration": None,
                "overstay_affected_user": "ALL",
                "overstay_product_member": [],
                "overstay_start": "00: 00",
                "overstay_end": "06: 00"
            }
        ]

    @staticmethod
    def get_price_limited_progressive_duration():
        return [
            {
                "fine": 0,
                "grace_period": 5,
                "initial_time": 1,
                "max_hour": 12,
                "min_hour": 0,
                "discount": 0,
                "max_price": 10000,
                "next_price": 1000,
                "overnight_price": 4000,
                "price": 2000,
                "stay_time": 1,
                "type": "LIMITED_PROGRESSIVE",
                "count_type": "INCREMENT",
                "vehicle_code": "MT1",
                "vehicle_name": "Motor",
                "overstay_parameter": "DURATION",
                "overstay_duration": 6,
                "overstay_affected_user": "ALL",
                "overstay_product_member": [],
                "overstay_start": "",
                "overstay_end": ""
            },
            {
                "fine": 0,
                "grace_period": 5,
                "initial_time": 1,
                "max_hour": 12,
                "min_hour": 0,
                "discount": 0,
                "max_price": 40000,
                "next_price": 3000,
                "overnight_price": 10000,
                "price": 5000,
                "stay_time": 1,
                "type": "LIMITED_PROGRESSIVE",
                "count_type": "INCREMENT",
                "vehicle_code": "MB1",
                "vehicle_name": "Mobil",
                "overstay_parameter": "DURATION",
                "overstay_duration": 6,
                "overstay_affected_user": "ALL",
                "overstay_product_member": [],
                "overstay_start": "",
                "overstay_end": ""
            }
        ]

    @staticmethod
    def get_price_limited_progressive_range():
        return [
            {
                "fine": 0,
                "grace_period": 5,
                "initial_time": 1,
                "max_hour": 12,
                "min_hour": 0,
                "discount": 0,
                "max_price": 10000,
                "next_price": 1000,
                "overnight_price": 4000,
                "price": 2000,
                "stay_time": 1,
                "type": "LIMITED_PROGRESSIVE",
                "count_type": "INCREMENT",
                "vehicle_code": "MT1",
                "vehicle_name": "Motor",
                "overstay_parameter": "TIME",
                "overstay_duration": None,
                "overstay_affected_user": "ALL",
                "overstay_product_member": [],
                "overstay_start": "00: 00",
                "overstay_end": "06: 00"
            },
            {
                "fine": 0,
                "grace_period": 5,
                "initial_time": 1,
                "max_hour": 12,
                "min_hour": 0,
                "discount": 0,
                "max_price": 40000,
                "next_price": 3000,
                "overnight_price": 10000,
                "price": 5000,
                "stay_time": 1,
                "type": "LIMITED_PROGRESSIVE",
                "count_type": "INCREMENT",
                "vehicle_code": "MB1",
                "vehicle_name": "Mobil",
                "overstay_parameter": "TIME",
                "overstay_duration": None,
                "overstay_affected_user": "ALL",
                "overstay_product_member": [],
                "overstay_start": "00: 00",
                "overstay_end": "06: 00"
            }
        ]
    
    @staticmethod
    def get_price_inap_limited_progressive_range_member():
        return [
            {
                "fine": 0,
                "fine_type": "",
                "grace_period": 5,
                "initial_time": 1,
                "max_hour": 0,
                "min_hour": 0,
                "discount": 0,
                "max_price": 0,
                "next_price": 1000,
                "overnight_price": 2000,
                "price": 5000,
                "stay_time": 1,
                "type": "PROGRESSIVE",
                "overstay_type": "LIMITED_PROGRESSIVE",
                "count_type": "INCREMENT",
                "vehicle_code": "MT1",
                "vehicle_name": "Motor",
                "overstay_parameter": "TIME",
                "overstay_duration": None,
                "overstay_affected_user": "ALL",
                "overstay_product_member": [],
                "overstay_start": "23:00",
                "overstay_end": "05:00",
                "overstay_progressive_time_start": 1,
                "overstay_progressive_time_next": 1,
                "overstay_start_price": 5000,
                "overstay_next_price": 2000,
                "overstay_max_price": 7000,
                "overstay_max_hours": 3
            }
        ]
    
    @staticmethod
    def get_price_inap_limited_progressive_duration_member_max_hour_3():
        return [
            {
                "fine": 0,
                "fine_type": "",
                "grace_period": 5,
                "initial_time": 1,
                "max_hour": 0,
                "min_hour": 0,
                "discount": 0,
                "max_price": 0,
                "next_price": 1000,
                "overnight_price": 2000,
                "price": 5000,
                "stay_time": 1,
                "type": "PROGRESSIVE",
                "overstay_type": "LIMITED_PROGRESSIVE",
                "count_type": "INCREMENT",
                "vehicle_code": "MT1",
                "vehicle_name": "Motor",
                "overstay_parameter": "DURATION",
                "overstay_duration": 6,
                "overstay_affected_user": "ALL",
                "overstay_product_member": [],
                "overstay_start": "",
                "overstay_end": "",
                "overstay_progressive_time_start": 1,
                "overstay_progressive_time_next": 1,
                "overstay_start_price": 5000,
                "overstay_next_price": 2000,
                "overstay_max_price": 7000,
                "overstay_max_hours": 3,
            }
        ]
    
    @staticmethod
    def get_price_inap_limited_progressive_duration_member_max_hour_6():
        return [
            {
                "fine": 0,
                "fine_type": "",
                "grace_period": 5,
                "initial_time": 1,
                "max_hour": 0,
                "min_hour": 0,
                "discount": 0,
                "max_price": 0,
                "next_price": 1000,
                "overnight_price": 2000,
                "price": 5000,
                "stay_time": 1,
                "type": "PROGRESSIVE",
                "overstay_type": "LIMITED_PROGRESSIVE",
                "count_type": "INCREMENT",
                "vehicle_code": "MT1",
                "vehicle_name": "Motor",
                "overstay_parameter": "DURATION",
                "overstay_duration": 6,
                "overstay_affected_user": "ALL",
                "overstay_product_member": [],
                "overstay_start": "",
                "overstay_end": "",
                "overstay_progressive_time_start": 1,
                "overstay_progressive_time_next": 1,
                "overstay_start_price": 5000,
                "overstay_next_price": 2000,
                "overstay_max_price": 7000,
                "overstay_max_hours": 6,
            }
        ]
    
    @staticmethod
    def get_price_inap_progressive_range_member():
        return [
            {
                "fine": 0,
                "fine_type": "",
                "grace_period": 5,
                "initial_time": 1,
                "max_hour": 0,
                "min_hour": 0,
                "discount": 0,
                "max_price": 0,
                "next_price": 1000,
                "overnight_price": 2000,
                "price": 5000,
                "stay_time": 1,
                "type": "PROGRESSIVE",
                "overstay_type": "PROGRESSIVE",
                "count_type": "INCREMENT",
                "vehicle_code": "MT1",
                "vehicle_name": "Motor",
                "overstay_parameter": "TIME",
                "overstay_duration": None,
                "overstay_affected_user": "MEMBER",
                "overstay_product_member": ["411d0df8-320a-4036-b844-728bbae59781"],
                "overstay_start": "23:00",
                "overstay_end": "05:00",
                "overstay_progressive_time_start": 1,
                "overstay_progressive_time_next": 1,
                "overstay_start_price": 5000,
                "overstay_next_price": 2000,
            }
        ]
    
    @staticmethod
    def get_price_inap_progressive_range_casual():
        return [
            {
                "fine": 0,
                "fine_type": "",
                "grace_period": 5,
                "initial_time": 1,
                "max_hour": 0,
                "min_hour": 0,
                "discount": 0,
                "max_price": 0,
                "next_price": 1000,
                "overnight_price": 2000,
                "price": 5000,
                "stay_time": 1,
                "type": "PROGRESSIVE",
                "overstay_type": "PROGRESSIVE",
                "count_type": "INCREMENT",
                "vehicle_code": "MT1",
                "vehicle_name": "Motor",
                "overstay_parameter": "TIME",
                "overstay_duration": None,
                "overstay_affected_user": "ALL",
                "overstay_product_member": [],
                "overstay_start": "23:00",
                "overstay_end": "05:00",
                "overstay_progressive_time_start": 1,
                "overstay_progressive_time_next": 1,
                "overstay_start_price": 5000,
                "overstay_next_price": 2000,
            }
        ]
    
    @staticmethod
    def get_price_inap_progressive_duration_member():
        return [
            {
                "fine": 0,
                "fine_type": "",
                "grace_period": 5,
                "initial_time": 1,
                "max_hour": 0,
                "min_hour": 0,
                "discount": 0,
                "max_price": 0,
                "next_price": 1000,
                "overnight_price": 2000,
                "price": 5000,
                "stay_time": 1,
                "type": "PROGRESSIVE",
                "overstay_type": "PROGRESSIVE",
                "count_type": "INCREMENT",
                "vehicle_code": "MT1",
                "vehicle_name": "Motor",
                "overstay_parameter": "DURATION",
                "overstay_duration": 6,
                "overstay_affected_user": "ALL",
                "overstay_product_member": [],
                "overstay_start": "",
                "overstay_end": "",
                "overstay_progressive_time_start": 1,
                "overstay_progressive_time_next": 1,
                "overstay_start_price": 5000,
                "overstay_next_price": 2000,
            }
        ]
    
    @staticmethod
    def get_price_inap_progressive_duration_casual():
        return [
            {
                "fine": 0,
                "fine_type": "",
                "grace_period": 5,
                "initial_time": 1,
                "max_hour": 0,
                "min_hour": 0,
                "discount": 0,
                "max_price": 0,
                "next_price": 1000,
                "overnight_price": 2000,
                "price": 5000,
                "stay_time": 1,
                "type": "PROGRESSIVE",
                "overstay_type": "PROGRESSIVE",
                "count_type": "INCREMENT",
                "vehicle_code": "MT1",
                "vehicle_name": "Motor",
                "overstay_parameter": "DURATION",
                "overstay_duration": 6,
                "overstay_affected_user": "ALL",
                "overstay_product_member": [],
                "overstay_start": "",
                "overstay_end": "",
                "overstay_progressive_time_start": 1,
                "overstay_progressive_time_next": 1,
                "overstay_start_price": 5000,
                "overstay_next_price": 2000,
            }
        ]
    
    @staticmethod
    def get_price_progressive_duration():
        return [
            {
                "fine": 0,
                "grace_period": 5,
                "initial_time": 1,
                "max_hour": 24,
                "min_hour": 0,
                "discount": 0,
                "max_price": 0,
                "next_price": 3000,
                "overnight_price": 10000,
                "price": 5000,
                "stay_time": 0,
                "type": "PROGRESSIVE",
                "count_type": "INCREMENT",
                "vehicle_code": "MB1",
                "vehicle_name": "Mobil",
                "overstay_parameter": "DURATION",
                "overstay_duration": 10,
                "overstay_affected_user": "ALL",
                "overstay_product_member": [],
                "overstay_start": "",
                "overstay_end": ""
            },
            {
                "fine": 0,
                "grace_period": 5,
                "initial_time": 1,
                "max_hour": 24,
                "min_hour": 0,
                "discount": 0,
                "max_price": 0,
                "next_price": 1000,
                "overnight_price": 7000,
                "price": 2000,
                "stay_time": 0,
                "type": "PROGRESSIVE",
                "count_type": "INCREMENT",
                "vehicle_code": "MT1",
                "vehicle_name": "Motor",
                "overstay_parameter": "DURATION",
                "overstay_duration": 10,
                "overstay_affected_user": "ALL",
                "overstay_product_member": [],
                "overstay_start": "",
                "overstay_end": ""
            }
        ]
    
    @staticmethod
    def get_price_progressive_range():
        return [
            {
                "fine": 0,
                "grace_period": 5,
                "initial_time": 1,
                "max_hour": 24,
                "min_hour": 0,
                "discount": 0,
                "max_price": 0,
                "next_price": 3000,
                "overnight_price": 10000,
                "price": 5000,
                "stay_time": 0,
                "type": "PROGRESSIVE",
                "count_type": "INCREMENT",
                "vehicle_code": "MB1",
                "vehicle_name": "Mobil",
                "overstay_parameter": "TIME",
                "overstay_duration": None,
                "overstay_affected_user": "ALL",
                "overstay_product_member": [],
                "overstay_start": "07:00",
                "overstay_end": "12:00"
            },
            {
                "fine": 0,
                "grace_period": 5,
                "initial_time": 1,
                "max_hour": 24,
                "min_hour": 0,
                "discount": 0,
                "max_price": 0,
                "next_price": 1000,
                "overnight_price": 7000,
                "price": 2000,
                "stay_time": 0,
                "type": "PROGRESSIVE",
                "count_type": "INCREMENT",
                "vehicle_code": "MT1",
                "vehicle_name": "Motor",
                "overstay_parameter": "TIME",
                "overstay_duration": None,
                "overstay_affected_user": "ALL",
                "overstay_product_member": [],
                "overstay_start": "07:00",
                "overstay_end": "12:00"
            }
        ]
    
    @staticmethod
    def get_price_progressive_range_start_more_than_end():
        return [
            {
                "fine": 0,
                "grace_period": 5,
                "initial_time": 1,
                "max_hour": 24,
                "min_hour": 0,
                "discount": 0,
                "max_price": 0,
                "next_price": 3000,
                "overnight_price": 10000,
                "price": 5000,
                "stay_time": 0,
                "type": "PROGRESSIVE",
                "count_type": "INCREMENT",
                "vehicle_code": "MB1",
                "vehicle_name": "Mobil",
                "overstay_parameter": "TIME",
                "overstay_duration": None,
                "overstay_affected_user": "ALL",
                "overstay_product_member": [],
                "overstay_start": "21:00",
                "overstay_end": "02:00"
            }
        ]

    @staticmethod
    def get_price_limited_progressive_range_start_more_than_end():
        return [
            {
                "fine": 0,
                "grace_period": 5,
                "initial_time": 1,
                "max_hour": 12,
                "min_hour": 0,
                "discount": 0,
                "max_price": 10000,
                "next_price": 1000,
                "overnight_price": 4000,
                "price": 2000,
                "stay_time": 1,
                "type": "LIMITED_PROGRESSIVE",
                "count_type": "INCREMENT",
                "vehicle_code": "MT1",
                "vehicle_name": "Motor",
                "overstay_parameter": "TIME",
                "overstay_duration": None,
                "overstay_affected_user": "ALL",
                "overstay_product_member": [],
                "overstay_start": "21: 00",
                "overstay_end": "03: 00"
            }
        ]
    
    @staticmethod
    def get_price_flat_range_start_more_than_end():
        return [
            {
                "fine": 0,
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
                "overstay_parameter": "TIME",
                "overstay_duration": None,
                "overstay_affected_user": "ALL",
                "overstay_product_member": [],
                "overstay_start": "21: 00",
                "overstay_end": "03: 00"
            }
        ]
    
    @staticmethod
    def get_price_flat_range_start_minutes_overstay():
        return [
            {
                "fine": 0,
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
                "overstay_parameter": "TIME",
                "overstay_duration": None,
                "overstay_affected_user": "ALL",
                "overstay_product_member": [],
                "overstay_start": "00: 00",
                "overstay_end": "06: 00"
            },
            {
                "fine": 0,
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
                "overstay_parameter": "TIME",
                "overstay_duration": None,
                "overstay_affected_user": "ALL",
                "overstay_product_member": [],
                "overstay_start": "00: 00",
                "overstay_end": "06: 00"
            }
        ]
    
    @staticmethod
    def get_price_dynamic_pricing():
        return [
            {
                "fine": 0,
                "fine_type": "",
                "grace_period": 0,
                "initial_time": 5,
                "max_hour": 0,
                "min_hour": 0,
                "discount": 0,
                "max_price": 0,
                "next_price": 0,
                "overnight_price": 0,
                "price": 5,
                "stay_time": 0,
                "type": "PERIOD",
                "count_type": "INCREMENT",
                "vehicle_code": "MT1",
                "vehicle_name": "Motor",
                "overstay_parameter": None,
                "overstay_duration": None,
                "overstay_affected_user": None,
                "overstay_start": None,
                "overstay_end": None,
                "period_data": [
                    {
                        "end": 10,
                        "price": 10000,
                        "start": 6
                    },
                    {
                        "end": 15,
                        "price": 30000,
                        "start": 10
                    },
                    {
                        "end": 18,
                        "price": 50000,
                        "start": 15
                    },
                    {
                        "end": 30,
                        "price": 60000,
                        "start": 18,
                    }
                ]
            }
        ]