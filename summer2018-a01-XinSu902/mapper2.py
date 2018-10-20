#!/usr/bin/env python
#
# This file has been provided as a starting point. You need to modify this file.
# Reads whole lines stdin; writes key/value pairs to stdout
# --- DO NOT MODIFY ANYTHING ABOVE THIS LINE ---


import sys
import datetime

if __name__ == "__main__":
      for line in sys.stdin:
            line = line.strip().split()[3][1:]
            for yyyymm in line:
                  yyyymm = f"{datetime.datetime.strptime(line,'%d/%b/%Y:%H:%M:%S').year}-{datetime.datetime.strptime(line,'%d/%b/%Y:%H:%M:%S').month}"
                  sys.stdout.write("{}\t1\n".format(yyyymm))

