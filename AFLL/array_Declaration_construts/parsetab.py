
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COMMA DATATYPE ID LBRACKET RBRACKET\n    array_declaration : DATATYPE LBRACKET  RBRACKET ID\n                     | DATATYPE LBRACKET  RBRACKET array_declaration\n    empty :'
    
_lr_action_items = {'DATATYPE':([0,4,],[2,2,]),'$end':([1,5,6,],[0,-1,-2,]),'LBRACKET':([2,],[3,]),'RBRACKET':([3,],[4,]),'ID':([4,],[5,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'array_declaration':([0,4,],[1,6,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> array_declaration","S'",1,None,None,None),
  ('array_declaration -> DATATYPE LBRACKET RBRACKET ID','array_declaration',4,'p_array_declaration','yacc.py',5),
  ('array_declaration -> DATATYPE LBRACKET RBRACKET array_declaration','array_declaration',4,'p_array_declaration','yacc.py',6),
  ('empty -> <empty>','empty',0,'p_empty','yacc.py',12),
]
