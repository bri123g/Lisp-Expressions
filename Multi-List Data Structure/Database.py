import sys
from SupplierNode import *
from Suppliers import *
from PartNode import *
from Parts import *
from SupplyNode import *
from Supply import *

def loadSuppliers(fname):
  suppliers = Suppliers()
  with open(fname) as f:
    for line in f.readlines():
      line = line.strip("\n")
      s = line.split(",")
      suppliers.insert(s[0],s[1])
  return suppliers

def loadParts(fname):
  parts = Parts()
  with open(fname) as f:
    for line in f.readlines():
      line = line.strip("\n")
      p = line.split(",")
      parts.insert(p[0],p[1])
  return parts

def loadSupply(suppliers,parts,fname):
  with open(fname) as f:
    for line in f.readlines():
      line = line.strip("\n")
      sup = line.split(",")
      insert_supply(suppliers, parts, sup[0], sup[1], sup[2])
      
def storeSuppliers(suppliers,fname):
    with open(fname, "w") as f:
      s = suppliers.head.get_next()
      while s != None:
        line = str(s.get_no()) + ',' + str(s.get_name()) 
        f.write(line)
        f.write('\n')
        s = s.get_next()

def storeParts(parts,fname):
  with open(fname, "w") as f:
    p = parts.head.get_next()
    while p != None:
      line = str(p.get_no()) + ',' + str(p.get_name())
      f.write(line)
      f.write('\n')
      p = p.get_next()

def storeSupply(suppliers,parts,fname):
  with open(fname, "w") as f:
    s = suppliers.head.get_next()
    while s != None:
      sup = s.get_supply()
      if sup != None:
        sup = sup.get_snext()
        while sup != None:
          line = str(sup.get_sowner().get_no()) + ',' + str(sup.get_powner().get_no()) + ',' + str(sup.get_price())
          f.write(line)
          f.write('\n')
          sup = sup.get_snext()
      s = s.get_next()

def menu():
    print()
    print("Menu of Options:\n")
    print("ps (print suppliers)")
    print("pp (print parts)")
    print("fsgp pno (find suppliers given part)")
    print("fpgs sno (find parts given supplier)")
    print("fcsgp pno (find cheapest suppliers given part)\n")
    print("is sno:sname (insert supplier)")
    print("ds sno (delete supplier)")
    print("us sno:sname (update supplier name)\n")
    print("ip pno:pname (insert part)")
    print("dp pno (delete part)")
    print("up pno:pname (update part name)\n")
    print("isp sno:pno:price (insert supply)")
    print("dsp sno:pno (delete supply)")
    print("usp sno:pno:price (update supply price)\n")
    print("q (quit)")
    print()

def main():
  suppliers = loadSuppliers(sys.argv[1]+"/s.dat")
  parts = loadParts(sys.argv[1]+"/p.dat")
  loadSupply(suppliers,parts,sys.argv[1]+"/sp.dat")
  while True:
    menu()
    c = input("Your option: ").strip().split()
    command = c[0].lower()
    if command == "q":
      break

    # suppliers
    elif command == "ps":
      print(str(suppliers),end="")
    elif command == 'is':
      sno,sname = c[1].strip().split(":")
      if suppliers.insert(sno,sname):
        print("Supplier %s has been inserted"%sno)
      else:
        print("Supplier %s already exists"%sno)
    elif command == 'ds':
      sno = c[1].strip()
      if suppliers.delete(sno):
        print("Supplier %s has been deleted"%sno)
      else:
        print("Supplier %s does not exist"%sno)
    elif command == 'us':
      sno,sname = c[1].strip().split(":")
      if suppliers.update(sno,sname):
        print("Supplier %s has been updated"%sno)
      else:
        print("Supplier %s does not exist"%sno)

    # parts
    elif command == "pp":
      print(str(parts),end="")
    elif command == 'ip':
      pno,pname = c[1].strip().split(":")
      #print(pno,pname)
      if parts.insert(pno,pname):
        print("Part %s has been inserted"%pno)
      else:
        print("Part %s already exists"%pno)
    elif command == 'dp':
      pno = c[1].strip()
      if parts.delete(pno):
        print("Part %s has been deleted"%pno)
      else:
        print("Part %s does not exist"%pno)
    elif command == 'up':
      pno,pname = c[1].strip().split(":")
      if parts.update(pno,pname):
        print("Part %s has been updated"%pno)
      else:
        print("Part %s does not exist"%pno)

    # supply
    elif command == 'isp':
      sno,pno,price = c[1].strip().split(":")
      if insert_supply(suppliers,parts,sno,pno,price):
         print("Supply Element %s, %s has been inserted"%(sno,pno))
      else:
         print("Supply Element %s, %s was NOT inserted"%(sno,pno))
    elif command == 'dsp':
      sno,pno = c[1].strip().split(":")
      if delete_supply(suppliers,parts,sno,pno):
         print("Supply Element %s, %s has been deleted"%(sno,pno))
      else:
         print("Supply Element %s, %s was NOT deleted"%(sno,pno))
    elif command == 'usp':
      sno,pno,price = c[1].strip().split(":")
      if update_supply(suppliers,parts,sno,pno,price):
         print("Supply Element %s, %s has been updated"%(sno,pno))
      else:
         print("Supply Element %s, %s was NOT updated"%(sno,pno))

    # Queries
    elif command == "fsgp":
      pno = c[1].strip()
      print_suppliers_given_part(parts,pno)
    elif command == "fpgs":
      sno = c[1].strip()
      print_parts_given_supplier(suppliers,sno)
    elif command == "fcsgp":
      pno = c[1].strip()
      print_cheapest_suppliers_given_part(parts,pno)
    else:
      print("Invalid option; Please enter option again\n")

  storeSuppliers(suppliers,sys.argv[1]+"/s.dat")
  storeParts(parts,sys.argv[1]+"/p.dat")
  storeSupply(suppliers,parts,sys.argv[1]+"/sp.dat")
  print("Bye!")
  print()

main()