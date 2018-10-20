#!/usr/bin/env python
#
# This file has been provided as a starting point. You need to modify this file.
# Reads whole lines stdin; writes key/value pairs to stdout
# --- DO NOT MODIFY ANYTHING ABOVE THIS LINE ---

import sys
import re
import os

if __name__ == "__main__":
        for line in sys.stdin:
			datetime = line.slice!(/\[.*?\]/)
			date, hour, minute, second = datetime.split(“:”)
			day,month,year = date.split(“/”)

				sys.stdout.write(“{}\”-“\{}\t1\n”.format(year,month)
