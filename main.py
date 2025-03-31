import os
import random
import time
import uuid

SHOULD_BE_SILENT = os.environ.get("SILENT_OUTPUT", "false")
SHOULD_GENERATE_UUID = os.environ.get("OUTPUT_UUID", "false")
BASE_DELAY = os.environ.get("BASE_DELAY", 30)
RAND_DELAY_RANGE = os.environ.get("RAND_DELAY_RANGE", 30)

def main():

    randWait = random.randint(0, int( RAND_DELAY_RANGE) )
    time.sleep( int(BASE_DELAY) + randWait)

    if SHOULD_BE_SILENT == "false":
        print("Waited", str( int(BASE_DELAY) + randWait ), "seconds.")

    if SHOULD_GENERATE_UUID == "true":
        print(uuid.uuid4())

if __name__ == '__main__':
    main()