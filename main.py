import sys

from tools.test.count.runner import RunnerTestCount
from tools.test.count.flat.flat_duration import FlatDurationTest


def main():
    if len(sys.argv) < 2:
        print("main - usage: python main.py <nadeem>")
        return False

    args = sys.argv[1]

    app = get_app(args)
    if not app:
        print("app not found")
        return False
    
    app.execute()

def get_app(app):
    if app == "test_count":
        return RunnerTestCount()

    if app == "manual_test":
        return _ManualApp()

    if app == "manual_input":
        return _ManualInteractiveApp()

    if app == "membership_test":
        return _MembershipApp()

    return False


class _ManualApp:
    """Wrapper kecil supaya `manual_test` bisa dipanggil lewat pola
    `app.execute()` yang sama seperti app lain, tapi menjalankan
    `execute_manual()` milik FlatDurationTest."""

    def execute(self):
        FlatDurationTest().execute_manual()


class _ManualInteractiveApp:
    """Wrapper kecil untuk `manual_input` - mode input data manual
    langsung lewat terminal (bukan dari file CSV)."""

    def execute(self):
        FlatDurationTest().execute_interactive()


class _MembershipApp:
    """Wrapper kecil untuk `membership_test` - test kombinasi
    Affected User & User (Member/Casual) dari file CSV."""

    def execute(self):
        FlatDurationTest().execute_membership()


if __name__ == "__main__":
    main()
