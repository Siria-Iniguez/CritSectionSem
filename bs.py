#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 11:04:31 2022

@author: cati
"""
from multiprocessing import Process,BoundedSemaphore
from multiprocessing import current_process
from multiprocessing import Value, Array
N = 8
def is_anybody_inside(critical, tid):
     found = False
     i = 0
     while i<len(critical) and not found:
         found = tid!=i and critical[i]==1
         i += 1
     return found
 
def task(tid,common, b):
     a = 0
     for i in range(100):
         print(f'{tid}−{i}: Non−critical Section')
         a += 1
         
         print(f'{tid}−{i}: End of non−critical Section')
         b.acquire()
         print(f'{tid}−{i}: Critical section')
         try:
             v = common.value + 1
             print(f'{tid}−{i}: Inside critical section')
             common.value = v
             print(f'{tid}−{i}: End of critical section')
         finally:
             b.release()
def main():
     lp = []
     common = Value('i', 0)
     b= BoundedSemaphore(1)
     for tid in range(N):
         lp.append(Process(target=task, args= (tid,common ,b)))
     print (f"Valor inicial del contador {common.value}")
     for p in lp:
         p.start()
     for p in lp:
         p.join()
     print (f"Valor final del contador {common.value}")
     print ("fin")

     
if __name__ == "__main__":
    main()