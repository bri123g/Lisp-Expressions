from SupplierNode import *
from SupplyNode import *

class Suppliers:

  def __init__(self):
    self.head = SupplierNode("","",None,None)
    self.size = 0

  def find(self,sno):
    s = self.head
    found = False
    while s.get_next() != None and not found:
      if s.get_next().get_no() >= sno:
        found = True
      else:
        s = s.get_next()
    if found and s.get_next().get_no() == sno:
      return (True, s)
    else:
      return (False, s)
    
  def insert(self,sno,sname):
    (found,position) = self.find(sno)
    if found:
      return False
    else:
      s = SupplierNode(sno,sname,position.get_next(), None)
      position.set_next(s)
      self.size += 1
      return True 

  def delete(self,sno):
    (found, position) = self.find(sno)
    if not found:
      return False
    else:
        if position.get_next().num_supply == 0:
          position.set_next(position.get_next().get_next())
          self.size -= 1
          return True

  def update(self,sno,sname):
    (found,position) = self.find(sno)
    if not found:
      return False
    else:
      position.get_next().set_no(sno)
      position.get_next().set_name(sname)
      return True

  def __str__(self):
    s = self.head
    result = "\n"
    if s.get_next() != None:
      s = s.get_next()
      while s != None:
        result = result + str(s) + ' ' + 'Supplies: '
        sup = s.get_supply()
        if sup != None:
          if sup.get_snext() != None:
            sup = sup.get_snext()
            while sup != None:
              result = result + '(' + str(sup.get_powner().get_no()) + ',' + str(sup.get_price()) + ')' + ' '
              sup = sup.get_snext()
            result = result + "\n"
          else:
            result = result + 'None' + "\n"
          s = s.get_next()
        else:
          result = result + 'None' + "\n"
          s = s.get_next()
      return result + "\n"
    else:
      return 'None'