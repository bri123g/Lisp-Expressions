class SupplyNode:

  def __init__(self, snxt, pnxt, sown, pown, p):
    self.snext = snxt
    self.pnext = pnxt
    self.sowner = sown
    self.powner = pown
    self.price = p
  # Write getters and setters and __str__ method
  def get_snext(self):
    return self.snext
  def get_pnext(self):
    return self.pnext
  def get_sowner(self):
    return self.sowner
  def get_powner(self):
    return self.powner
  def get_price(self):
    return self.price
  def set_snext(self, snxt):
    self.snext = snxt
  def set_pnext(self, pnxt):
    self.pnext = pnxt
  def set_sown(self, sown):
    self.sowner = sown
  def set_pown(self, pown):
    self.powner = pown
  def set_price(self, p):
    self.price = p
  def __str__(self):
    return "("+ str(self.get_sowner().get_no())+","+ str(self.get_powner().get_no())+")"