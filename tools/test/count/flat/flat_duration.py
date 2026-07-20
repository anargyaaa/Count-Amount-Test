import csv
import os
from datetime import datetime

from model.price import ParkingPriceModel
from utility.count_price import CountPrice
from utility.time import TimeUtility


class FlatDurationTest:
    INPUT_PATH = os.path.join("data", "manual_test_data.csv")
    OUTPUT_PATH = os.path.join("data", "manual_test_result.csv")

    VEHICLE_CODE_ALIASES = {
        "MT": "MT1",
        "MB": "MB1",
    }

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

            requirement = (
                expectation["parking_price"] == response.parking_price
                and expectation["total_price"] == response.total_amount
                and expectation["overstay_price"] == response.overnight_price
            )

            masuk = datetime.fromtimestamp(time_in / 1000).strftime("%H:%M:%S")
            keluar = datetime.fromtimestamp(time_out / 1000).strftime("%H:%M:%S")

            lama_jam = round((time_out - time_in) / (1000 * 60 * 60), 2)

            overstay = "TRUE" if response.overnight_price > 0 else "FALSE"

            status = "PASSED" if requirement else "FAILED"

            print("=" * 60)
            print("                    RESULT TEST")
            print("=" * 60)

            print(f"Test Name          : {get_test.__name__}")
            print(f"Vehicle            : {price_payload['vehicle_name']} ({current_vehicle})")
            print(f"Grace Time         : {price_payload['grace_period']} Menit")

            print()
            print(f"Jam Masuk          : {masuk}")
            print(f"Jam Keluar         : {keluar}")
            print(f"Lama Parkir        : {lama_jam} Jam")
            print(f"Is Overstay        : {overstay}")

            print("\nParking Price")
            print(f"    Expected       : {expectation['parking_price']}")
            print(f"    Calculated     : {response.parking_price}")

            print("\nOverstay Price")
            print(f"    Expected       : {expectation['overstay_price']}")
            print(f"    Calculated     : {response.overnight_price}")

            print("\nTotal Price")
            print(f"    Expected       : {expectation['total_price']}")
            print(f"    Calculated     : {response.total_amount}")

            print(f"\nStatus             : {status}")
            print("=" * 60)
            print()

            if not requirement:
                raise Exception(f"Test {get_test.__name__} failed")

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

    def execute_manual(self):
        rows = self._read_manual_input(self.INPUT_PATH)
        if not rows:
            print(f"Tidak ada data pada {self.INPUT_PATH}")
            return

        results = [self._process_manual_row(index, row) for index, row in enumerate(rows, start=1)]

        for r in results:
            self._print_manual_result(r)

        self._write_manual_output(results)

        total = len(results)
        total_passed = sum(1 for r in results if r["hasil"] == "PASSED")
        print(f"{total_passed}/{total} baris data PASSED.")
        print(f"Hasil lengkap disimpan di: {self.OUTPUT_PATH}")

    def execute_interactive(self):
        print("=" * 60)
        print("           INPUT DATA MANUAL (INTERAKTIF)")
        print("=" * 60)
        print("Ketik data satu per satu. Tekan Ctrl+C kapan saja untuk keluar.\n")

        results = []
        index = 1

        while True:
            row = self._prompt_manual_row()
            if row is None:
                continue

            result = self._process_manual_row(index, row)
            self._print_manual_result(result)
            results.append(result)
            index += 1

            lanjut = input("Input data lagi? (y/n): ").strip().lower()
            print()
            if lanjut != "y":
                break

        if results:
            self._write_manual_output(results)
            total = len(results)
            total_passed = sum(1 for r in results if r["hasil"] == "PASSED")
            print(f"{total_passed}/{total} baris data PASSED.")
            print(f"Hasil lengkap disimpan di: {self.OUTPUT_PATH}")
        else:
            print("Tidak ada data yang diinput.")

    def _prompt_manual_row(self):
        """Tanyakan satu baris data (vehicle, jam_masuk, jam_keluar,
        expected_total opsional) lewat terminal. Validasi format dasar
        di sini supaya user langsung tahu kalau salah ketik, sebelum
        masuk ke perhitungan harga."""
        known_vehicles = ", ".join(sorted(set(
            [item["vehicle_code"] for item in self._base_data] +
            list(self.VEHICLE_CODE_ALIASES.keys())
        )))

        while True:
            vehicle = input(f"Vehicle ({known_vehicles}): ").strip()
            try:
                self._get_price_payload(vehicle)
                break
            except ValueError as e:
                print(f"  ! {e}. Coba lagi.\n")

        while True:
            jam_masuk = input("Jam Masuk  (YYYY-MM-DD HH:MM:SS): ").strip()
            try:
                self._parse_datetime_to_epoch_ms(jam_masuk)
                break
            except ValueError as e:
                print(f"  ! {e}\n")

        while True:
            jam_keluar = input("Jam Keluar (YYYY-MM-DD HH:MM:SS): ").strip()
            try:
                self._parse_datetime_to_epoch_ms(jam_keluar)
                break
            except ValueError as e:
                print(f"  ! {e}\n")

        expected_total = input(
            "Expected Total (kosongkan jika ingin otomatis): "
        ).strip()

        print()

        return {
            "vehicle": vehicle,
            "jam_masuk": jam_masuk,
            "jam_keluar": jam_keluar,
            "expected_total": expected_total,
        }

    def _resolve_vehicle_code(self, vehicle_input: str) -> str:
        vehicle_input = (vehicle_input or "").strip().upper()
        return self.VEHICLE_CODE_ALIASES.get(vehicle_input, vehicle_input)

    def _get_price_payload(self, vehicle_input: str) -> dict:
        vehicle_code = self._resolve_vehicle_code(vehicle_input)
        payload = next(
            (item for item in self._base_data if item["vehicle_code"] == vehicle_code),
            None,
        )
        if payload is None:
            known = ", ".join(sorted(set(
                [item["vehicle_code"] for item in self._base_data] +
                list(self.VEHICLE_CODE_ALIASES.keys())
            )))
            raise ValueError(
                f"Vehicle '{vehicle_input}' tidak dikenali. Kode yang tersedia: {known}"
            )
        return payload

    def _parse_datetime_to_epoch_ms(self, value: str) -> int:
        """Format yang didukung:
        - "YYYY-MM-DD HH:MM:SS"  (contoh: "2026-07-20 07:00:00")
        - "YYYY-MM-DD HH:MM"     (detik dianggap 0)
        """
        value = (value or "").strip()
        for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M"):
            try:
                dt = datetime.strptime(value, fmt)
                return int(dt.timestamp() * 1000)
            except ValueError:
                continue
        raise ValueError(
            f"Format tanggal/jam '{value}' tidak valid. "
            "Gunakan format 'YYYY-MM-DD HH:MM:SS', contoh: 2026-07-20 07:00:00"
        )

    def _read_manual_input(self, path):
        if not os.path.exists(path):
            print(f"File input tidak ditemukan: {path}")
            print("Buat file CSV dengan kolom: vehicle,jam_masuk,jam_keluar,expected_total")
            return []

        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return [row for row in reader]

    def _process_manual_row(self, index, row):
        vehicle_input = row.get("vehicle", "")
        jam_masuk_str = row.get("jam_masuk", "")
        jam_keluar_str = row.get("jam_keluar", "")
        expected_total_str = (row.get("expected_total") or "").strip()

        try:
            price_payload = self._get_price_payload(vehicle_input)
            time_in = self._parse_datetime_to_epoch_ms(jam_masuk_str)
            time_out = self._parse_datetime_to_epoch_ms(jam_keluar_str)

            count_price = CountPrice(
                time_in=time_in,
                time_out=time_out,
                price_payload=price_payload,
                current_vehicle=price_payload["vehicle_code"],
            )
            response: ParkingPriceModel = count_price.execute()

            parking_price = response.parking_price
            overstay_price = response.overnight_price
            total_amount = response.total_amount
            is_overstay = "TRUE" if overstay_price > 0 else "FALSE"
            lama_jam = round((time_out - time_in) / (1000 * 60 * 60), 2)
            grace_menit = price_payload.get("grace_period", 0)

            if expected_total_str != "":
                try:
                    expected_total = int(expected_total_str)
                except ValueError:
                    return self._failed_row(
                        index, vehicle_input, jam_masuk_str, jam_keluar_str,
                        f"expected_total '{expected_total_str}' bukan angka yang valid"
                    )
                konsisten = total_amount == expected_total
                keterangan = "" if konsisten else f"Expected={expected_total}, Calculated={total_amount}"
            else:
                konsisten = (parking_price + overstay_price) == total_amount
                keterangan = "" if konsisten else "Total tidak konsisten dengan parking + overstay"

            hasil = "PASSED" if konsisten else "FAILED"

            return {
                "no": index,
                "vehicle": f"{price_payload['vehicle_name']} ({price_payload['vehicle_code']})",
                "grace": f"{grace_menit} Menit",
                "jam_masuk": jam_masuk_str,
                "jam_keluar": jam_keluar_str,
                "lama_jam": lama_jam,
                "is_overstay": is_overstay,
                "parking_price": parking_price,
                "overstay_price": overstay_price,
                "total_amount": total_amount,
                "hasil": hasil,
                "keterangan": keterangan,
            }

        except Exception as e:
            return self._failed_row(index, vehicle_input, jam_masuk_str, jam_keluar_str, str(e))

    def _failed_row(self, index, vehicle_input, jam_masuk_str, jam_keluar_str, keterangan):
        return {
            "no": index,
            "vehicle": vehicle_input,
            "grace": "-",
            "jam_masuk": jam_masuk_str,
            "jam_keluar": jam_keluar_str,
            "lama_jam": "-",
            "is_overstay": "-",
            "parking_price": "-",
            "overstay_price": "-",
            "total_amount": "-",
            "hasil": "FAILED",
            "keterangan": keterangan,
        }

    def _print_manual_result(self, r):
        print("=" * 60)
        print("                    RESULT TEST (MANUAL)")
        print("=" * 60)
        print(f"No                 : {r['no']}")
        print(f"Vehicle            : {r['vehicle']}")
        print(f"Grace Time         : {r['grace']}")
        print()
        print(f"Jam Masuk          : {r['jam_masuk']}")
        print(f"Jam Keluar         : {r['jam_keluar']}")
        print(f"Lama Parkir        : {r['lama_jam']} Jam")
        print(f"Is Overstay        : {r['is_overstay']}")
        print()
        print(f"Parking Price      : {r['parking_price']}")
        print(f"Overstay Price     : {r['overstay_price']}")
        print(f"Total Price        : {r['total_amount']}")
        print(f"\nStatus             : {r['hasil']}")
        if r["keterangan"]:
            print(f"Keterangan         : {r['keterangan']}")
        print("=" * 60)
        print()

    def _write_manual_output(self, results):
        os.makedirs(os.path.dirname(self.OUTPUT_PATH), exist_ok=True)
        fieldnames = [
            "no", "vehicle", "grace", "jam_masuk", "jam_keluar",
            "lama_jam", "is_overstay", "parking_price",
            "overstay_price", "total_amount", "hasil", "keterangan",
        ]
        with open(self.OUTPUT_PATH, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for r in results:
                writer.writerow({k: r[k] for k in fieldnames})