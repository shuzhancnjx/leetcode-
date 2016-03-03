# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 10:57:49 2015

@author: ZSHU
"""
class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if len(prices)<=1:
            return 0
        else:
            profit, starting, point=0,0,1
            
            while point<=len(prices)-1:
                if prices[point]>=prices[point-1]:
                    if point==len(prices)-1:
                        profit+= prices[point]-prices[starting]
                        return profit 
                    point+=1
                else:
                    profit += prices[point-1]-prices[starting]
                    starting=point
                    point+=1
            return profit 
        