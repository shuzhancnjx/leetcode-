# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 10:11:52 2015

@author: ZSHU
"""

class Solution:
    # @param {integer[]} gas
    # @param {integer[]} cost
    # @return {integer}
    def canCompleteCircuit(self, gas, cost):
        if sum(gas)<sum(cost):
            return -1
        else:
            diff=[]
            for i in xrange(len(gas)):
                diff+=[gas[i]-cost[i]]
         
            i=0
            starting=0
            while starting<=len(diff)-1:
                if (i+1<=len(diff) and sum(diff[starting:i+1])>=0) \
                  or (i+1>len(diff) and sum(diff[starting:]+diff[:i+1-len(diff)])>=0):
                      if i+1-len(diff)==starting:
                          return starting 
                      i+=1
                else:
                    i+=1
                    starting=i
            return -1
            
                 
         
         
            