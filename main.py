import gc
import os

import psutil as psutil
import requests as requests

# fetch api response and it's data then print it
response = requests.get("https://zenquotes.io/api/quotes/")
# print json data of 'q' key
print("Quote: " + response.json()[0]['q'])
# print json data of author key with by at first then author name
print("by " + response.json()[0]['a'])

# force garbage collection for python
gc.collect()

# print out the memory usage of the current process in MB with MB at the end
print("Memory usage: ", str(psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024) + " MB")
