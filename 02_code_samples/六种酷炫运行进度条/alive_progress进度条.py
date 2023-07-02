import time
from alive_progress import alive_bar
items = range(100)                  # retrieve your set of items
with alive_bar(len(items)) as bar:   # declare your expected total
    for item in items:               # iterate as usual
        # process each item
        bar()
        time.sleep(0.1)