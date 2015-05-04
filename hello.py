import sys
import argparse

# default value is "World"
name = "World"
if len(sys.argv) > 1:
	name = sys.argv[1]
print "Hello,", name