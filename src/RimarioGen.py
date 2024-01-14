import sys


class RimarioGen:
    '''RimarioGen handles a console application interface to run functionalities offered by RimarioGen application'''

    def __init__(self):
        '''Create a new instance of RimarioGen'''
        if len(sys.argv) > 1:
            self.args = sys.argv[1:]
        else:
            self.args = []

    def run(self):
        '''Run console application considering arguments passed to application during creation of instance'''
        # TBD
        print("RimarioGen hasn't been implemented yet.")


def main():
    # Start application
    app = RimarioGen()
    # Run application
    app.run()


if __name__ == "__main__":
    main()
