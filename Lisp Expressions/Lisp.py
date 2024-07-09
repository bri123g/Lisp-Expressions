import sys, traceback

from LispParser import parser

def read_input():
  result = ''
  while True:
    data = input('LISP: ').strip() 
    if ';' in data:
      i = data.index(';')
      result += data[0:i+1]
      break
    else:
      result += data + ' '
  return result

def evalNum(tree):
  if tree[0] == 'num':
    return tree[1], "OK"
  elif tree[0] in ['+','-','*','/']:
    num1,msg = evalNum(tree[1])
    if msg != "OK":
      return None, msg
    num2,msg = evalNum(tree[2])
    if msg != "OK":
      return None, msg
    if tree[0] == '+':
      return num1 + num2, msg
    elif tree[0] == '-':
      return num1 - num2, msg
    elif tree[0] == '*':
      return num1 * num2,msg
    elif tree[0] == '/':
      if num2 != 0:
        return num1 / num2, msg
      else:
        return None, "EVALUATION ERROR: Divide by 0!"
  elif tree[0] == 'car':
    num, msg = evalList(tree[1])
    if msg != "OK":
      return None, msg
    if num == []:
      return None, "Cannot evaluate CAR of EMPTY List!"
    else:
      return num[0], "OK"
  else:
    return None, "Something bad happened!"

def evalList(tree):
  if tree == []:
    return  [], "OK"
  elif tree[0] == 'cdr':
    cdr_list, msg = evalList(tree[1])
    if msg != "OK":
      return None, msg
    if cdr_list == []:
      return None, "CDR of empty list Error!"
    return cdr_list[1:], "OK"
  else:
    num1, msg1 = evalNum(tree[0])
    if msg1 != "OK": 
      return None, msg1
    num2, msg2 = evalList(tree[1])
    if msg2 != "OK":
      return None, msg2
    return [num1] + num2, "OK"

def main():
  while True:
    data = read_input() 
    if data == 'exit;':
      break
    try:
      tree = parser.parse(data)
      print(tree)
      if tree[0] == 'NUM':
        answer,msg = evalNum(tree[1])
        if msg == "OK":
          print("\nThe value is "+str(answer)+"\n")
        else:
          print("\n"+msg+"\n")
      elif tree[0] == 'LIST':
        answer,msg = evalList(tree[1])
        if msg == "OK":
          print("\nThe value is "+
                str(answer).replace('[','(').replace(']',')').replace(',','')+"\n")
        else:
          print("\n"+msg+"\n")
      else:
        continue
    except Exception as inst:
      continue

main()
