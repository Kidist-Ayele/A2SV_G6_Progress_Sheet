class Solution:
    def countVowels(self, word: str) -> int:
        vov={'a':0,'e':0,'i':0,'o':0,'u':0}
        x=len(word)
        for i in range(x):
            if word[i] in vov:
                vov[word[i]]+=(i+1)*(x-i) 
        summ=0  
        for i,j in vov.items():
            summ+=j  
        return summ

            
