import sys
import argparse
from greeter import *

# default value is "World"
# Author: Elad Mizrahi (eladmz@gmail.com)
name = "World"
if len(sys.argv) > 1:
	name = sys.argv[1]

greeter = Greeter(name)
greeter.greet()