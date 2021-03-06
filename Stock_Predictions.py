#!/usr/bin/py
# https://www.hackerrank.com/challenges/stockprediction

# Heuristic criteria for evaluating potential stock picks
# Score: 55.2
from collections import defaultdict
class Eval(object):
	fact = 0
	item = 0

	def __init__(self,x,y):
		self.fact = x
		self.item= y
	# overloading print function 
	def __str__(self):
		return "{0} {1}".format(str(self.fact), str(self.item))

	# overloading less than function for sorting 
	def __lt__(self, other):
		return (self.fact) >= (other.fact)

def printTransactions(m, k, d, name, owned, prices):
	avail = m
	output = []
	cand1 = []
	cand2 = []
	dt = defaultdict()
	for i in range(len(name)):
		if owned[i]>0:		
			if prices[i][4]> prices[i][3]:
				output.append(name[i]+" SELL "+str(owned[i]));
		if prices[i][2]>= prices[i][3] and prices[i][3]>= prices[i][4]:	
			cand1.append(Eval((prices[i][2]-prices[i][4])/prices[i][2],i))
		if (prices[i][3]-prices[i][4])/prices[i][4] > 0.04:
			cand2.append(i)
	for it in sorted(cand1):
		buy = int(avail/prices[it.item][4])
		avail -= buy*prices[it.item][4]
		if buy >0:
			output.append(name[it.item]+" BUY "+str(buy));
			dt[it.item] = 1
	for i in cand2:
		if dt.get(i) == None:	
			buy = int(avail/prices[i][4])
			avail -= buy*prices[i][4]
			if buy >0:
				output.append(name[it.item]+" BUY "+str(buy));
	print len(output)
	for i in output:
		print i		
	

if __name__ == '__main__':
    m, k, d = [float(i) for i in raw_input().strip().split()]
    k = int(k)
    d = int(d)
    names = []
    owned = []
    prices = []
    for data in range(k):
        temp = raw_input().strip().split()
        names.append(temp[0])
        owned.append(int(temp[1]))
        prices.append([float(i) for i in temp[2:7]])

    printTransactions(m, k, d, names, owned, prices)

