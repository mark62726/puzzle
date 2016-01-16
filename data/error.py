import traceback

class Error:
    def __init__(self):
        self.test()
        
    def create_report(self):
        print(traceback.print_exc())
