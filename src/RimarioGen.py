import sys


class RimarioGen:
    def __init__(self):
        if len(sys.argv) > 1:
            self.args = sys.argv[1:]
        else:
            self.args = []

    def run(self):
        # TBD
        print("RimarioGen hasn't been implemented yet.")


def main():
    # Start application
    app = RimarioGen()
    # Run application
    app.run()


if __name__ == "__main__":
    main()
