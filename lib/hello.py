import sys
import argparse

# default value is "World"
# Author: Elad Mizrahi (eladmz@gmail.com)
name = "World"
if len(sys.argv) > 1:
	name = sys.argv[1]
print "Hello,", name