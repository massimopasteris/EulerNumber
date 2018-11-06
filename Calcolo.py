'''
Created on 06 nov 2018

@author: mpasteri

Versine 3
'''

#--------------------------------------------------------
# #1 - Compute the Euler's number using Newton Expansion.
# sum(1/(n!) n=0...N
#--------------------------------------------------------

EulerNumber=1
for n in range(1,20):  
    print('----------------------------------------')  
    print(n)
    fat=1
    for ind in range(1,n+1):
        fat=fat*ind
    print('fat=',fat)
    errorE = EulerNumber  
    EulerNumber=EulerNumber+1/fat
    errorE=errorE-EulerNumber
    print(EulerNumber)    
    print('Error=',errorE)
    print('----------------------------------------')  
        
        
#--------------------------------------------------------
# #2 - Brothers' Formulae 
# EulerNumber= sum( (2*n +2)/(2*n+1)!  ) n=0...N
# n=0 EulerNumber=2
#--------------------------------------------------------
print('---****************************---')  


EulerNumber=2
for n in range(1,6):  
    print('----------------------------------------')  
    print(n)
    fat=1
    for ind in range(1,(2*n+1)+1 ):
        fat=fat*ind
    print('fat=',fat)    
    EulerNumber=EulerNumber+ 2*(n+1)/fat    
    print(EulerNumber)    
    print('----------------------------------------')  
          

