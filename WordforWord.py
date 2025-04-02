import os
import re

class wordProcessor:

    pass

    def readfile(self, file_path):
        with open(file_path) as file:
            content = file.read()
            file.close()
        return content


    def wc(self, content):
        num_chars = len(content)
        num_words = len(content.split())
        num_lines = content.count('\n')
        t = num_chars, num_words, num_lines
        return t


    def wordFrequency(self, content):
        fcontent = re.sub(r'[^\w\s]', '',content).lower()
        words = fcontent.split()
        result = {}

        for i in words:
            if i in result:
                result[i]+=1
            else:
                result[i] = 1
        return result
        #pass


    def letterFrequency(self):
        pass



text = ("The big red dog. \n "
        "It likes to play. \n "
        "It likes to eat. \n"
        "I likes to go on walks. \n"
        "He is a good dog. \n")
processor = wordProcessor()
result = processor.wc(text)
print(result)

wordfreq = processor.wordFrequency(text)
print(wordfreq)

