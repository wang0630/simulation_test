import resource
from time import sleep


class MemoryMonitor:
    def __init__(self):
        self.should_continue_measuring = True

    def memory_usage(self):
        max_usage = 0
        while self.should_continue_measuring:
            max_usage = max(
                max_usage,
                resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            )
            sleep(0.1)

        return max_usage
