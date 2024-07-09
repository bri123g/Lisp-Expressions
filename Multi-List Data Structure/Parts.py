from PartNode import *
from SupplyNode import *

class Parts:

  def __init__(self):
    self.head = PartNode("","",None,None)
    self.size = 0

  def find(self,pno):
    p = self.head
    found = False
    while p.get_next() != None and not found:
      if p.get_next().get_no() >= pno:
        found = True
      else:
        p = p.get_next()
    if found and p.get_next().get_no() == pno:
      return (True, p)
    else:
      return (False, p)
    
  def insert(self,pno,pname):
    (found,position) = self.find(pno)
    if found:
      return False
    else:
      p = PartNode(pno, pname, position.get_next(), None)
      position.set_next(p)
      self.size += 1
      return True
 
  def delete(self,pno):
    (found, position) = self.find(pno)
    if not found:
      return False
    else:
        if position.get_next().num_supply == 0:
          position.set_next(position.get_next().get_next())
          self.size -= 1
          return True

  def update(self,pno,pname):
    (found,position) = self.find(pno)
    if not found:
      return False
    else:
      position.get_next().set_no(pno)
      position.get_next().set_name(pname)
      return True

  def __str__(self):
    p = self.head
    result = "\n"
    if p.get_next() != None:
      p = p.get_next()
      while p != None:
        result = result + str(p) + ' ' + 'Supplied by: '
        sup = p.get_supply()
        if sup.get_pnext() != None:
          sup = sup.get_pnext()
          while sup != None:
            result = result + '(' + str(sup.get_sowner().get_no()) + ',' + str(sup.get_price()) + ')' + ' '
            sup = sup.get_pnext()
          result = result + "\n"
        else:
          result = result + 'None' + "\n"
        p = p.get_next()
      return result + "\n"
    else:
      return 'None'