# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 09:04:58 2015

@author: ZSHU
"""
"""
comments, this one is not hard logically, but a lot of corner cases 
"""

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if len(words)==0:
            return [' '*maxWidth]
            
        i,p,length,res=0,0,0,[]
        while i<len(words) and p<=len(words):
            if p<len(words) and length+len(words[p])<=maxWidth-p+i:
                length+=len(words[p])
                p+=1
            else:
                if p==i:
                    res.append(words[i])
                    p+=1
                elif p-i==1:
                    temp=(maxWidth-length)
                    res.append(words[i]+' '*temp)
                else:
                    word=words[i:p]
                    if p!=len(words):
                        temp=(maxWidth-length)/(p-i-1)
                        if (maxWidth-length)%(p-i-1)>0:
                            for j in range( (maxWidth-length)%(p-i-1)):
                                word[j]+=' '
                        res.append((' '*temp).join(word))
                    else:
                        temp=' '.join(word)
                        res.append(temp+' '*(maxWidth-len(temp)))
                i=p
                length=0
        return res 

        
    