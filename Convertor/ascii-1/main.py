text = input("enter a string to convert into ascii values:")
ascii_values = []
for character in text:
    ascii_values.append(ord(character))
print(ascii_values)
def decimalToBinary(n):
    return bin(n).replace("0b", "")
choice = int(input("Enter your choice between 2,8,16:"))
bina=[]
octa=[]
hexa=[]
if choice==2:
  for i in ascii_values:
    # print(i)
    bina.append(decimalToBinary(i))
  print(bina)
elif choice==8:
  for i in ascii_values:
      octa.append(oct(i))
  print(octa)
elif choice==16:
  for i in ascii_values:
      hexa.append(hex(i))
  print(hexa)
