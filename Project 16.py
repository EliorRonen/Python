
import os

import argparse

def shutdown(seconds):

    """Shuts down the system after the specified number of seconds."""

    os.system(f"shutdown /s /t {seconds}")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Shutdown the system.")

    parser.add_argument("-t", "--time", type=int, default=0,

                    help="Number of seconds before shutdown (default: 0)")

args = parser.parse_args()

shutdown(args.time)