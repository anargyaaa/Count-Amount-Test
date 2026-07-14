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
