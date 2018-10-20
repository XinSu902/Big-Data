#!/usr/bin/env python
#
# This file has been provided as a starting point. You need to modify this file.
# Reads whole lines stdin; writes key/value pairs to stdout
# --- DO NOT MODIFY ANYTHING ABOVE THIS LINE ---

import sys

if __name__ == "__main__":
	for line in sys.stdin:
		for word in line.split():
			sys.stdout.write("{}\t1\n".format(word))

