import os
from datetime import datetime

from model.price import ParkingPriceModel
from tools.test.data import PriceList
from utility.count_price import CountPrice


class FlatRangeTest:
    """
    Test untuk tipe harga FLAT dengan overstay berbasis RANGE waktu
    (curfew) - misalnya kendaraan yang parkir melewati jam 00:00-06:00,
    berbeda dengan FlatDurationTest yang overstay-nya berbasis durasi
    (lama parkir sejak masuk).

    Data harga kendaraan diambil dari tools/test/data.py
    (PriceList.get_price_flat_range()), bukan hardcode di file ini.

    Data test di bawah ini diambil dari data test manual yang sudah
    divalidasi (hanya baris berstatus PASSED yang dipakai, baris
    berstatus "Unuse" sengaja tidak disertakan).

    Catatan penting soal Grace: pada tipe overstay RANGE/curfew ini,
    library TETAP menghitung overstay meskipun durasi parkirnya masih
    dalam periode Grace. Supaya hasilnya sesuai ekspektasi bisnis
    (Grace = gratis total, termasuk overstay), kita terapkan aturan
    tambahan di execute(): kalau grace_period aktif, overstay dianggap 0.

    Hasil test disimpan ke folder logs/ (bukan ke data/ seperti fitur
    test manual yang lain).
    """

    LOG_PATH = os.path.join("logs", "flat_range_test.log")

    # Lebar kolom tabel output (dipakai bareng oleh console & log file)
    COL_NO = 3
    COL_TIME = 21
    COL_PRICE = 9
    COL_STATUS = 6

    def __init__(self):
        self._base_data = PriceList.get_price_flat_range()

        # Hanya baris berstatus PASSED dari data test yang dipakai.
        self._list_test = [
            self._test_01_masuk_235959_keluar_235959,
            self._test_02_masuk_235959_keluar_000000,
            self._test_03_masuk_235959_keluar_000001,
            self._test_04_masuk_235959_keluar_010000,
            self._test_05_masuk_235959_keluar_055959,
            self._test_06_masuk_235959_keluar_060000,
            self._test_07_masuk_235959_keluar_060001,
            self._test_08_masuk_055959_keluar_235959_18jam,
            self._test_09_masuk_055959_keluar_000001_19jam,
            self._test_10_masuk_060000_keluar_235959_18jam,
            self._test_11_masuk_060000_keluar_000000_18jam,
        ]

    # ==================================================================
    # Jalankan semua test & tampilkan hasil dalam bentuk tabel
    # ==================================================================
    def execute(self):
        rows = []
        total_passed = 0
        total = len(self._list_test)

        for get_test in self._list_test:
            test = get_test()
            row = self._run_single_test(test)
            rows.append(row)
            if row["status"] == "PASSED":
                total_passed += 1

        output_lines = self._build_table(rows, total_passed, total)

        print("\n".join(output_lines))

        self._write_log(output_lines)

        if total_passed != total:
            failed_names = ", ".join(r["no"] for r in rows if r["status"] == "FAILED")
            raise Exception(f"Test flat_range gagal pada No: {failed_names}")

    # ------------------------------------------------------------------
    # Jalankan satu test case & terapkan aturan Grace
    # ------------------------------------------------------------------
    def _run_single_test(self, test):
        count_price = CountPrice(
            time_in=self._to_ms(test["jam_masuk"]),
            time_out=self._to_ms(test["jam_keluar"]),
            price_payload=test["price_payload"],
            current_vehicle=test["current_vehicle"],
        )
        response: ParkingPriceModel = count_price.execute()

        parking_price = response.parking_price
        overstay_price = response.overnight_price
        total_amount = response.total_amount

        # Aturan tambahan: kalau masih Grace, overstay dianggap 0
        # (library-nya sendiri tidak menggratiskan overstay saat Grace).
        if response.grace_period:
            overstay_price = 0
            total_amount = parking_price

        expectation = test["expectation"]
        requirement = (
            expectation["parking_price"] == parking_price
            and expectation["overstay_price"] == overstay_price
            and expectation["total_price"] == total_amount
        )

        return {
            "no": test["no"],
            "jam_masuk": self._format_clock(test["jam_masuk"]),
            "jam_keluar": self._format_clock(test["jam_keluar"], relative_to=test["jam_masuk"]),
            "parking_price": parking_price,
            "overstay_price": overstay_price,
            "total_amount": total_amount,
            "expectation": expectation,
            "status": "PASSED" if requirement else "FAILED",
        }

    # ------------------------------------------------------------------
    # Bangun tabel output (dipakai untuk console & log file)
    # ------------------------------------------------------------------
    def _build_table(self, rows, total_passed, total):
        lines = []
        title = "FLAT RANGE TEST RESULT"
        width = self.COL_NO + self.COL_TIME * 2 + self.COL_PRICE * 3 + self.COL_STATUS + 10

        lines.append("=" * width)
        lines.append(title.center(width))
        lines.append("=" * width)
        lines.append(
            f"{'No':<{self.COL_NO}} "
            f"{'Jam Masuk':<{self.COL_TIME}} "
            f"{'Jam Keluar':<{self.COL_TIME}} "
            f"{'Parking':>{self.COL_PRICE}} "
            f"{'Overstay':>{self.COL_PRICE}} "
            f"{'Total':>{self.COL_PRICE}} "
            f"{'Status':<{self.COL_STATUS}}"
        )
        lines.append("-" * width)

        for r in rows:
            mark = "✓" if r["status"] == "PASSED" else "✗"
            lines.append(
                f"{r['no']:<{self.COL_NO}} "
                f"{r['jam_masuk']:<{self.COL_TIME}} "
                f"{r['jam_keluar']:<{self.COL_TIME}} "
                f"{r['parking_price']:>{self.COL_PRICE},} "
                f"{r['overstay_price']:>{self.COL_PRICE},} "
                f"{r['total_amount']:>{self.COL_PRICE},} "
                f"{mark} {r['status']}"
            )
            if r["status"] == "FAILED":
                exp = r["expectation"]
                lines.append(
                    f"{'':<{self.COL_NO}}   Expected -> "
                    f"parking={exp['parking_price']}, overstay={exp['overstay_price']}, "
                    f"total={exp['total_price']}"
                )

        lines.append("-" * width)
        lines.append(f"Hasil: {total_passed}/{total} PASSED")
        lines.append("=" * width)

        return lines

    # ------------------------------------------------------------------
    # Simpan hasil ke logs/
    # ------------------------------------------------------------------
    def _write_log(self, output_lines):
        os.makedirs(os.path.dirname(self.LOG_PATH), exist_ok=True)
        with open(self.LOG_PATH, "w", encoding="utf-8") as f:
            f.write(f"FlatRangeTest run at {datetime.now().isoformat()}\n\n")
            f.write("\n".join(output_lines))
            f.write("\n")
        print(f"Log disimpan di: {self.LOG_PATH}")

    # ------------------------------------------------------------------
    # Helper waktu
    # ------------------------------------------------------------------
    def _to_ms(self, value: str) -> int:
        return int(datetime.strptime(value, "%Y-%m-%d %H:%M:%S").timestamp() * 1000)

    def _format_clock(self, value: str, relative_to: str = None) -> str:
        """Tampilkan jam saja (HH:MM:SS), tambahkan penanda (+1 hari)
        kalau tanggalnya beda dari jam masuk, biar tabel tetap ringkas."""
        dt = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
        clock = dt.strftime("%H:%M:%S")
        if relative_to:
            base_date = datetime.strptime(relative_to, "%Y-%m-%d %H:%M:%S").date()
            day_diff = (dt.date() - base_date).days
            if day_diff > 0:
                clock += f" (+{day_diff} hari)"
        return clock

    def _get_payload(self):
        return next(
            (item for item in self._base_data if item["vehicle_code"] == "MT1"),
            {}
        )

    # ------------------------------------------------------------------
    # 11 data PASSED (data "Unuse" dari sumbernya tidak disertakan)
    # ------------------------------------------------------------------
    def _test_01_masuk_235959_keluar_235959(self):
        return {
            "no": "01",
            "current_vehicle": "MT1",
            "jam_masuk": "2026-07-20 23:59:59",
            "jam_keluar": "2026-07-20 23:59:59",
            "price_payload": self._get_payload(),
            "expectation": {"parking_price": 0, "overstay_price": 0, "total_price": 0},
        }

    def _test_02_masuk_235959_keluar_000000(self):
        return {
            "no": "02",
            "current_vehicle": "MT1",
            "jam_masuk": "2026-07-20 23:59:59",
            "jam_keluar": "2026-07-21 00:00:00",
            "price_payload": self._get_payload(),
            "expectation": {"parking_price": 0, "overstay_price": 0, "total_price": 0},
        }

    def _test_03_masuk_235959_keluar_000001(self):
        return {
            "no": "03",
            "current_vehicle": "MT1",
            "jam_masuk": "2026-07-20 23:59:59",
            "jam_keluar": "2026-07-21 00:00:01",
            "price_payload": self._get_payload(),
            "expectation": {"parking_price": 0, "overstay_price": 0, "total_price": 0},
        }

    def _test_04_masuk_235959_keluar_010000(self):
        return {
            "no": "04",
            "current_vehicle": "MT1",
            "jam_masuk": "2026-07-20 23:59:59",
            "jam_keluar": "2026-07-21 01:00:00",
            "price_payload": self._get_payload(),
            "expectation": {"parking_price": 2000, "overstay_price": 7000, "total_price": 9000},
        }

    def _test_05_masuk_235959_keluar_055959(self):
        return {
            "no": "05",
            "current_vehicle": "MT1",
            "jam_masuk": "2026-07-20 23:59:59",
            "jam_keluar": "2026-07-21 05:59:59",
            "price_payload": self._get_payload(),
            "expectation": {"parking_price": 2000, "overstay_price": 7000, "total_price": 9000},
        }

    def _test_06_masuk_235959_keluar_060000(self):
        return {
            "no": "06",
            "current_vehicle": "MT1",
            "jam_masuk": "2026-07-20 23:59:59",
            "jam_keluar": "2026-07-21 06:00:00",
            "price_payload": self._get_payload(),
            "expectation": {"parking_price": 2000, "overstay_price": 7000, "total_price": 9000},
        }

    def _test_07_masuk_235959_keluar_060001(self):
        return {
            "no": "07",
            "current_vehicle": "MT1",
            "jam_masuk": "2026-07-20 23:59:59",
            "jam_keluar": "2026-07-21 06:00:01",
            "price_payload": self._get_payload(),
            "expectation": {"parking_price": 2000, "overstay_price": 7000, "total_price": 9000},
        }

    def _test_08_masuk_055959_keluar_235959_18jam(self):
        return {
            "no": "08",
            "current_vehicle": "MT1",
            "jam_masuk": "2026-07-20 05:59:59",
            "jam_keluar": "2026-07-20 23:59:59",
            "price_payload": self._get_payload(),
            "expectation": {"parking_price": 2000, "overstay_price": 7000, "total_price": 9000},
        }

    def _test_09_masuk_055959_keluar_000001_19jam(self):
        return {
            "no": "09",
            "current_vehicle": "MT1",
            "jam_masuk": "2026-07-20 05:59:59",
            "jam_keluar": "2026-07-21 00:00:01",
            "price_payload": self._get_payload(),
            "expectation": {"parking_price": 2000, "overstay_price": 14000, "total_price": 16000},
        }

    def _test_10_masuk_060000_keluar_235959_18jam(self):
        return {
            "no": "10",
            "current_vehicle": "MT1",
            "jam_masuk": "2026-07-20 06:00:00",
            "jam_keluar": "2026-07-20 23:59:59",
            "price_payload": self._get_payload(),
            "expectation": {"parking_price": 2000, "overstay_price": 0, "total_price": 2000},
        }

    def _test_11_masuk_060000_keluar_000000_18jam(self):
        return {
            "no": "11",
            "current_vehicle": "MT1",
            "jam_masuk": "2026-07-20 06:00:00",
            "jam_keluar": "2026-07-21 00:00:00",
            "price_payload": self._get_payload(),
            "expectation": {"parking_price": 2000, "overstay_price": 7000, "total_price": 9000},
        }