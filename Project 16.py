import os

def shutdown_computer(seconds):

"""Shuts down the computer after a specified number of seconds."""


print("Shutting down the computer in", seconds, "seconds...")

os.system("shutdown /s /t " + str(seconds))

# Ask the user how many seconds to wait before shutdown

seconds_to_wait = int(input("How many seconds before shutdown? "))

# Call the shutdown function with the user's input

shutdown_computer(seconds_to_wait)