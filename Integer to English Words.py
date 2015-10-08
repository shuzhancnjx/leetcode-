# -*- coding: utf-8 -*-
"""
Created on Tue Oct 06 14:40:48 2015

@author: ZSHU
"""
"""
recursive + dictionary
"""

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        dic={1:'One', 2:'Two', 3:'Three', 4:'Four',5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 10: 'Ten', 11:'Eleven', 12:'Twelve',\
            13: 'Thirteen', 14: 'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen',18:'Eighteen',19:'Nineteen',20:'Twenty',30:'Thirty',\
            40:'Forty', 50:'Fifty', 60:'Sixty', 70:'Seventy', 80:'Eighty', 90:'Ninety', 100: 'Hundred',1000:'Thousand',1000000:'Million',\
            1000000000:'Billion'}
       
        
        def expression(num, prime, expre):
            if num==0:
                return 
            elif num<100 and num%prime[0]<20: 
                expre.append(dic[num%prime[0]])
                return 
            else:
                for i in range(len(prime)):
                    temp=num/prime[i]
                    if temp>0:
                        if prime[i]>=100: 
                           
                            if temp<100 and dic.get(temp, None):
                                expre+= [dic[temp]]+ [dic[prime[i]]]
                            else:
                                res=[]
                                expression(temp, prime[i:],res)
                                expre+= res + [dic[prime[i]]]
                        else:
                            expre.append( dic[prime[i]])
                        expression(num%prime[i], prime[i:],expre)
                        break
            
        if num==0:
            return 'Zero'
        result=[]
        expression(num, [1000000000, 1000000, 1000, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10], result)
        return " ".join(result)
         
            