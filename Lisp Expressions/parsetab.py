
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CAR CDR CONS LET LPAREN NUMBER OP RPAREN SEMI VARstart : list SEMIstart : num SEMInum : NUMBERnum : VARnum : LPAREN OP num num RPARENnum : LPAREN CAR list RPARENnum : LPAREN LET LPAREN vars RPAREN num RPARENlist : LPAREN seq RPARENlist : LPAREN CDR list RPARENlist : LPAREN CONS num list RPARENseq :seq : num seqvars : LPAREN VAR num RPARENvars : vars LPAREN VAR num RPAREN'
    
_lr_action_items = {'LPAREN':([0,4,5,6,11,12,13,14,15,16,18,20,22,24,28,30,32,33,35,37,39,41,42,],[4,9,-3,-4,18,9,9,9,18,24,9,18,9,29,-6,34,-5,9,9,9,-13,-7,-14,]),'NUMBER':([0,4,5,6,12,13,14,18,22,28,32,33,35,37,41,],[5,5,-3,-4,5,5,5,5,5,-6,-5,5,5,5,-7,]),'VAR':([0,4,5,6,12,13,14,18,22,28,29,32,33,34,35,37,41,],[6,6,-3,-4,6,6,6,6,6,-6,33,-5,6,37,6,6,-7,]),'$end':([1,7,8,],[0,-1,-2,]),'SEMI':([2,3,5,6,17,25,28,31,32,41,],[7,8,-3,-4,-8,-9,-6,-10,-5,-7,]),'CDR':([4,18,],[11,11,]),'CONS':([4,18,],[12,12,]),'OP':([4,9,],[14,14,]),'CAR':([4,9,],[15,15,]),'LET':([4,9,],[16,16,]),'RPAREN':([4,5,6,10,13,17,18,19,21,23,25,26,27,28,30,31,32,36,38,39,40,41,42,],[-11,-3,-4,17,-11,-8,-11,25,-12,28,-9,31,32,-6,35,-10,-5,39,41,-13,42,-7,-14,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'list':([0,11,15,20,],[2,19,23,26,]),'num':([0,4,12,13,14,18,22,33,35,37,],[3,13,20,13,22,13,27,36,38,40,]),'seq':([4,13,18,],[10,21,10,]),'vars':([24,],[30,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> list SEMI','start',2,'p_start_1','LispParser.py',5),
  ('start -> num SEMI','start',2,'p_start_2','LispParser.py',9),
  ('num -> NUMBER','num',1,'p_num_1','LispParser.py',13),
  ('num -> VAR','num',1,'p_num_2','LispParser.py',17),
  ('num -> LPAREN OP num num RPAREN','num',5,'p_num_3','LispParser.py',21),
  ('num -> LPAREN CAR list RPAREN','num',4,'p_num_4','LispParser.py',25),
  ('num -> LPAREN LET LPAREN vars RPAREN num RPAREN','num',7,'p_num_5','LispParser.py',29),
  ('list -> LPAREN seq RPAREN','list',3,'p_list_1','LispParser.py',33),
  ('list -> LPAREN CDR list RPAREN','list',4,'p_list_2','LispParser.py',37),
  ('list -> LPAREN CONS num list RPAREN','list',5,'p_list_3','LispParser.py',41),
  ('seq -> <empty>','seq',0,'p_seq_1','LispParser.py',45),
  ('seq -> num seq','seq',2,'p_seq_2','LispParser.py',49),
  ('vars -> LPAREN VAR num RPAREN','vars',4,'p_vars_1','LispParser.py',53),
  ('vars -> vars LPAREN VAR num RPAREN','vars',5,'p_vars_2','LispParser.py',57),
]
