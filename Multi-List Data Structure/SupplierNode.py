class SupplierNode:

  def __init__(self, no, name, nxt, supply):
    self.sno = no
    self.sname = name
    self.next = nxt
    self.first_supply = supply
    self.num_supply = 0
  # write setters and getters and __str__ methods
  def get_name(self):
    return self.sname
  def get_no(self):
    return self.sno
  def get_next(self):
    return self.next
  def get_supply(self):
    return self.first_supply
  def get_n_supply(self):
    return self.num_supply
  def set_name(self, name):
    self.sname = name
  def set_no(self, no):
    self.sno = no
  def set_next(self, nxt):
    self.next = nxt
  def set_supply(self, supply):
    self.first_supply = supply
  def set_n_supply(self, n_supply):
    self.num_supply = n_supply
  def __str__(self):
    return (f"({self.sno},{self.sname})")