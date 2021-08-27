import string
from random import *
class Password:
  def generatePassword(self) -> str:
    len = int(input("Enter the length of the password: "))
    if len < 8: 
      return self.generatePassword()
    else:
      characters = string.ascii_letters + string.punctuation  + string.digits + '*-/+'
      password = "".join(choice(characters) for x in range(len))
      return password

a = Password()
print(a.generatePassword())