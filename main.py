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

# Run the file
if __name__ == "__main__":
    main()
import sys

from tools.test.count.runner import RunnerTestCount


def main():
    if len(sys.argv) < 2:
        print("main - usage: python main.py <worker_name>")
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
    
    return False

# Run the file
if __name__ == "__main__":
    main()
