#! /bin/python3

import random
import sys


class StringLengthExceedLimitException(Exception):
    pass
class MultipleKeywordsException(Exception):
    pass

class AeqB:
    disabledlines:list[int]
    disabledlines=[]
    lines:list[str]
    printProgramLine=True
    printProgress=True
    __completed=False
    def __init__(self,programFile):
        with open(programFile,mode="r") as program:
            self.lines = program.readlines()
            for i in range(self.lines.__len__()):
                self.lines[i]=self.lines[i].removesuffix("\n").replace(" ","")
    def step(self,string:str):
            for i in range(self.lines.__len__()):
                if i not in self.disabledlines:
                    line=self.lines[i]
                    if line.__len__()>0 and not (line.isspace() or line.startswith("#")):
                        string2=self.parse(i,line,string)
                        if string!=string2:
                            if self.printProgramLine:
                                print(line,end="\t" if self.printProgress else "\n")
                            if string2.__len__()>255:
                                raise StringLengthExceedLimitException
                            return string2
            return string

    def parse(self,index:int,code:str,input:str):
        fromstr,tostr=code.split("=")
        key0=0
        key1=0
        if fromstr.find(")(")>=0 or tostr.find(")(")>=0:
            raise MultipleKeywordsException
        if fromstr.startswith("(start)"):
            key0=1
            fromstr=fromstr[7:]
        elif fromstr.startswith("(end)"):
            key0=-1
            fromstr=fromstr[5:]
        if tostr.startswith("(start)"):
            key1=1
            tostr=tostr[7:]
        elif tostr.startswith("(end)"):
            key1=-1
            tostr=tostr[5:]
        elif tostr.startswith("(return)"):
            key1=0
            tostr=tostr[8:]
            self.__completed=True
            return tostr

        if fromstr.startswith("(once)"):
            fromstr=fromstr[6:]
            output=self.replace(input,fromstr,tostr,key0,key1)
            if input!=output:
                self.disabledlines.append(index)
            return output
        return self.replace(input,fromstr,tostr,key0,key1)

    def replace(self,input:str,match:str,replacewith:str,key0=0,key1=0):
        string=input
        if key0==1 or match.__len__()==0:
            if string.startswith(match):
                if key1==-1:
                    string=string.removeprefix(match)+replacewith
                else:
                    string=replacewith+string.removeprefix(match)
        elif key0==-1:
            match=match
            if string.endswith(match):
                if key1==1:
                    string=replacewith+string.removesuffix(match)
                else:
                    string=string.removesuffix(match)+replacewith
        else:
            if string.find(match)>=0:
                if key1==-1:
                    string=string.replace(match,"",1)+replacewith
                elif key1==1:
                    string=replacewith+string.replace(match,"",1)
                else:
                    string=string.replace(match,replacewith,1)
        return string

    def getResult(self,input):
        self.disabledlines=[]
        lastinput=input
        while(not self.__completed):
            input=self.step(input)
            if lastinput==input:
                return input
            if self.printProgress:
                print(input)
            lastinput=input
        return(input)

if __name__=="__main__":
    if sys.argv.__len__()<2:
        programFile="demo.aeqb"
    else:
        programFile=sys.argv[1]
    if sys.argv.__len__()<3:
        input=""
    else:
        input=sys.argv[2]
    output=AeqB(programFile).getResult(input)
    print(input,output)
    aeqb = AeqB(programFile)
