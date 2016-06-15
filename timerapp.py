import time

class TimeApp:

    def __init__(self):
        self.initial_time = time.time()

    def get_time_now(self):
        time_now = time.localtime(time.time())
        return time_now

    def get_time_delta(self):
        return time.time() - self.initial_time

    def set_initial_time(self):
        self.initial_time = time.time()

    def get_initial_time(self):
        return self.initial_time
