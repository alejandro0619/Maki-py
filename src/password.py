import string
from random import *
class Password:
  
  def __init__(self, len) -> None:
      self.len = len
  
  def generatePassword(self) -> str:
    characters = string.ascii_letters + string.punctuation  + string.digits 
    password = "".join(choice(characters) for x in range(self.len))
    return password

a = Password(5)
a.hello()