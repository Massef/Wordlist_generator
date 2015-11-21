#!/usr/bin/python
# -*- coding: utf-8 -*-
import os 

def main():
    Dict = open('rockyou.txt' , 'r')
    fichier = open("result.txt", "w")
    cle = 'facebook'
    for word in Dict.readlines():
		word =word.strip('\n')
		result = (cle + word +('\n'))
		fichier.write(result)
		
   
if __name__ == '__main__':
    main()
