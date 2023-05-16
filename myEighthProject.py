from abc import ABC,abstractmethod
from collections import defaultdict
#Q1
class FrequencyCalculator(ABC):
    address=""
    def __init__(self,address): self.address=address
    @abstractmethod
    def calculateFreqs(self): pass
#Q2(create ListCount) and Q3
class ListCount(FrequencyCalculator):
    def calculateFreqs(self):
        freqs=defaultdict(int)
        with open(self.address,'r') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        char=char.lower()
                        freqs[char]=freqs[char]+1
        result=[]
        for char,count in freqs.items():
            result.extend([char,count])
        print(result)
#Q2(create DictCount) and Q4
class DictCount(FrequencyCalculator):
    def calculateFreqs(self):
        freqs={}
        with open(self.address,'r') as file:
            data=file.read()
            for char in data:
                if char.isalpha():
                    char=char.lower()
                    freqs[char]=freqs.get(char,0)+1
        print(freqs)
#Q5
listCount=ListCount('weirdWords.txt')
listCount.calculateFreqs()
dictCount=DictCount('weirdWords.txt')
dictCount.calculateFreqs()