
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ACCESS_MODIFIER COMMA ID LPAREN RETURN_TYPE RPAREN SEMICOLON\n    function_declaration :  ACCESS_MODIFIER RETURN_TYPE ID LPAREN RPAREN SEMICOLON\n    '
    
_lr_action_items = {'ACCESS_MODIFIER':([0,],[2,]),'$end':([1,7,],[0,-1,]),'RETURN_TYPE':([2,],[3,]),'ID':([3,],[4,]),'LPAREN':([4,],[5,]),'RPAREN':([5,],[6,]),'SEMICOLON':([6,],[7,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'function_declaration':([0,],[1,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> function_declaration","S'",1,None,None,None),
  ('function_declaration -> ACCESS_MODIFIER RETURN_TYPE ID LPAREN RPAREN SEMICOLON','function_declaration',6,'p_function_declaration','yacc.py',5),
]