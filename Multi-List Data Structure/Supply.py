from SupplyNode import *
# Note: This is not a Class but just a set of functions related to Supply nodes

def find_supply(suppliers,parts,sno,pno):
    (found,position) = suppliers.find(sno)
    (f,pos) = parts.find(pno)
    if found == True and f == True:
      s = position.get_next().get_supply()
      p = pos.get_next().get_supply()
      if s != None and p != None:
        while s.get_snext() != None and p.get_pnext() != None:
          if s.get_snext().get_sowner().get_no() == sno and p.get_pnext().get_sowner().get_no() == sno:
            return (True, s, p)
          elif p.get_pnext().get_sowner().get_no() > sno:
            return (False, s, p)
          elif s.get_snext().get_powner().get_no() > pno:
            return (False, s, p)
          else:
            s = s.get_snext()
            p = p.get_pnext()
        return (False, s, p)
      elif s != None and p == None:
        while s.get_snext() != None:
          if s.get_snext().get_powner().get_no() > pno:
            return (False, s, p)
          elif s.get_snext().get_snext() == None:
            return (False, s.get_snext(), p)
          s = s.get_snext()
      elif s == None and p != None:   
        while p.get_pnext() != None:
          if p.get_pnext().get_sowner().get_no() > sno:
            return (False, s, p.get_pnext())
          elif p.get_pnext().get_pnext() == None:
            return (False,s,p.get_pnext())
          p = p.get_pnext()
      elif s == None and p == None:
        return (False, s, p)
    else:
      return (False, None, None)
def insert_supply(suppliers,parts,sno,pno,price):
  (f1,pos1) = suppliers.find(sno)
  (f2,pos2) = parts.find(pno)
  if f1 != True and f2 != True:
    return False
  else:
    (found,s,p) = find_supply(suppliers,parts,sno,pno)
    if found:
      return False
    else:
      if p == None and s == None:
        pos1.get_next().set_supply(SupplyNode(None,None,pos1.get_next(),pos1.get_next(),None))
        pos2.get_next().set_supply(SupplyNode(None,None,pos2.get_next(),pos2.get_next(),None))
        s = pos1.get_next().get_supply()
        p = pos2.get_next().get_supply()
      elif p == None and s != None:
        pos2.get_next().set_supply(SupplyNode(None,None,pos2.get_next(),pos2.get_next(),None))
        p = pos2.get_next().get_supply()
      elif p != None and s == None:
        pos1.get_next().set_supply(SupplyNode(None,None,pos1.get_next(),pos1.get_next(),None))
        s = pos1.get_next().get_supply()
      supply = SupplyNode(s.get_snext(), p.get_pnext(), s.get_sowner(), p.get_powner(), price)
      s.set_snext(supply)
      p.set_pnext(supply)
      s.get_sowner().num_supply += 1
      p.get_powner().num_supply += 1
      return True

def delete_supply(suppliers,parts,sno,pno):
  (found,s,p) = find_supply(suppliers,parts,sno,pno)
  if not found:
    return False
  else:
    s.get_snext().get_sowner().num_supply -= 1
    p.get_pnext().get_powner().num_supply -= 1
    s.set_snext(s.get_snext().get_snext())
    p.set_pnext(p.get_pnext().get_pnext())
    return True

def update_supply(suppliers,parts,sno,pno,price):
  (found,s,p) = find_supply(suppliers,parts,sno,pno)
  if not found:
    return False
  else:
    s.get_snext().set_price(price)
    return True

def print_suppliers_given_part(parts,pno):
  (found,position) = parts.find(pno)
  if not found:
    print('The part does not exist.')
  else:
      p = position.get_next().get_supply()
      if p != None:
        if p.get_pnext() != None:
          p = p.get_pnext()
          while p != None:
            sno = p.get_sowner()
            no = sno.get_no()
            name = sno.get_name()
            price = p.get_price()
            print(f"({no},{name},{price})")
            p = p.get_pnext()
        else:
          print("None")
      else:
        print("None")

def print_parts_given_supplier(suppliers,sno):
  (found,position) = suppliers.find(sno)
  if not found:
    print('The supplier does not exist.')
  else:
      s = position.get_next().get_supply()
      if s != None:
        if s.get_snext() != None:
          s = s.get_snext()
          while s != None:
            pno = s.get_powner()
            no = pno.get_no()
            name = pno.get_name()
            price = s.get_price()
            print(f"({no},{name},{price})")
            s = s.get_snext()
        else:
          print("None")
      else:
        print("None")

def print_cheapest_suppliers_given_part(parts,pno):
  (found,position) = parts.find(pno)
  if not found:
    print('The part does not exist.')
  else:
      sup = []
      p = position.get_next().get_supply()
      if p !=  None:
        p = p.get_pnext()
        min_price = p.get_price()
        min_sup = p.get_sowner().get_no()
        min_name = p.get_sowner().get_name()
        sup.append([min_price, min_sup, min_name])
        if p.get_pnext() != None:
          p = p.get_pnext()
          while p != None:
            if p.get_price() < min_price:
              sup = []
              min_price = p.get_price()
              min_sup = p.get_sowner().get_no()
              min_name = p.get_sowner().get_name()
              sup.append([min_price, min_sup, min_name])
            elif p.get_price == min_price:
              min_price = p.get_price()
              min_sup = p.get_sowner().get_no()
              min_name = p.get_sowner().get_name()
              sup.append([min_price, min_sup, min_name])
            p = p.get_pnext()
        for i in sup:
          print(f'({i[1]}, {i[2]}, {i[0]})')
      else:
        print('Cheapest suppliers: None')