
#from pig_util import outputSchema

@outputSchema("as:int")
def square(num):
    if num == None:
        return None
    return ((num) * (num))

@outputSchema("word:chararray")
def concatenar(word1, word2):
    return (word1 + word2)