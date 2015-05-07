import sys
import argparse

# default value is "World"
# Author: Elad Mizrahi (eladmz@gmail.com)
class Greeter:
	def __init__(self, name):
		self.name = name
	
	def greet(self):
		print "Hello,", self.name