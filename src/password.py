import string
from random import *
from tokenize import Number


def generatePassword(max_len):
   characters = string.ascii_letters + string.punctuation  + string.digits 
   password = "".join(choice(characters) for x in range(max_len))
   print(password)
  
generatePassword(888)

