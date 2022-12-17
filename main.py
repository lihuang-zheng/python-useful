import gc
import os

import psutil as psutil
import requests as requests

# print out current user's name
print("Hello, " + os.getlogin() + "!")


# print out current day with time
print("Today is: " + os.popen('date').read())


# create line divider def
def line_divider():
    print("--------------------------------------------------")


# fetch api response
response = requests.get("https://zenquotes.io/api/quotes/")

line_divider()
# print json data of 'q' key
print("Quote: " + response.json()[0]['q'])
# print json data of author key with by at first then author name
print("by " + response.json()[0]['a'])
line_divider()

# force garbage collection for python
gc.collect()

# print out the memory usage of the current process in MB with MB at the end
print("Memory usage: ", str(psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024) + " MB")
