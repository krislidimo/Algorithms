#!/usr/bin/python

import argparse

#   4
#  3  -
#2     2  2
#       1

#       4
#   3  3
#  2  2
# 1 

# profit 
# - accending and new low hasn't been hit
# - only decending => lowest loss

# for every price
	# curr > high
		# set high
	# curr <
def find_max_profit(prices):
	max_profit = 0
	profit = 0
	low = prices[0]
	high = prices[0]

	for i in range(len(prices)):
		current = prices[i]

		# decending
		if current < low:
			low = current
			high = 0 # high set to 0 assures profit only accure when accending
		# accending
		elif current > high:
			high = current
			profit = high - low

			# only set profit if higher then max profits
			if profit > max_profit:
				max_profit = profit

	# if prices only decend, max_profit never gets set
	if max_profit == 0:
		max_profit = prices[-1] - prices[-2]

	print(max_profit)
	return max_profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))