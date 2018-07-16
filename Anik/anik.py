import sys
import csv
import json
import argparse
import logging as log
#import addQAndA


               
'''The output files are hard coded for this version
   and in the next version, it will take optional parameters.
   To test the code, use the error.log provided to parse the log.
   The parsed log is then sorted and written to analyse.out. Analyse.out
   is analyzed to understand the correctnes of TCP Loadbalancing.
   The final output is is result.out
'''
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()

    parser.add_argument('-d', '--debug',
             help="print debugging statements",
             action="store_const", dest="loglevel", const=log.DEBUG,
             default=log.WARNING,
    )
    parser.add_argument('-v', '--verbose',
             help="verbose",
             action="store_const", dest="loglevel", const=log.INFO,
    )

    parser.add_argument("-o", "--knowledgefile", type=str, required=True)
    parser.add_argument
    args = parser.parse_args()
    log.debug(args)
    knowFile = args.knowledgefile
    log.debug("main: knowfile " + knowFile)

    # set up logging
    log.basicConfig(level=args.loglevel, format='%(asctime)s - %(levelname)s - %(message)s')
    log.debug("main:argument file = " + str(args))

    knowledgeBae = { }

    def revieKnowlege():
        kf = open(knowFile, "r")
        lines = kf.readlines()
        kf.close()
        i = 0
        for line in lines:
            kl = line.split(':')
            


    def writeQA(text):
        rfile = open(knowFile,"a")
        rfile.write(text)
       
    i = 0
    while 1:
        response = input("Q for Question, R for review, X or any character for Exit " )
        if response == 'Q' or response == 'q':
            question = input("Please input Question ")
            question = "Q" + str(i) + ": " + question + '\n'
            writeQA(question)
            answer = input("Please input Answer ")
            answer = 'A' + str(i) + ': ' + answer + '\n' 
            writeQA(answer)
            i = i + 1
        elif response == 'R' or response == 'r':
            reviewQA()
        else:
            exit()


