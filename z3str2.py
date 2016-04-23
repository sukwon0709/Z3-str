#!/usr/bin/env python

## Figure out where the top-level checkout of the "z3str" repo lives
import os
z3strdir = os.path.dirname(os.path.abspath(__file__))

## Change the python path to load the Z3 python bindings from z3str
import sys
sys.path = [z3strdir + '/z3/python'] + sys.path

## Force Z3's python bindings to load the libz3str.so library
import z3
def find_lib_stub():
  return z3strdir + '/libz3str.so'
z3.z3core._find_lib = find_lib_stub

## Enable ctypes for the z3str_*() functions in libz3str2.so
import ctypes
z3strlib = z3.z3core.lib()
z3strlib.z3str_mk_context.restype = z3.ContextObj
z3strlib.z3str_mk_context.argtypes = []
#z3strlib.z3str_mk_theory.restype = Theory
#z3strlib.z3str_mk_theory.argtypes = [z3.ContextObj]
z3strlib.z3str_mk_string_sort.restype = z3.Sort
z3strlib.z3str_mk_string_sort.argtypes = []
#z3strlib.z3str_mk_regex_sort.restype = z3.Sort
#z3strlib.z3str_mk_regex_sort.argtypes = []
z3strlib.z3str_concat_decl.restype = z3.FuncDecl
z3strlib.z3str_concat_decl.argtypes = []
z3strlib.z3str_length_decl.restype = z3.FuncDecl
z3strlib.z3str_length_decl.argtypes = []
z3strlib.z3str_substring_decl.restype = z3.FuncDecl
z3strlib.z3str_substring_decl.argtypes = []
z3strlib.z3str_indexof_decl.restype = z3.FuncDecl
z3strlib.z3str_indexof_decl.argtypes = []
z3strlib.z3str_indexof2_decl.restype = z3.FuncDecl
z3strlib.z3str_indexof2_decl.argtypes = []
z3strlib.z3str_contains_decl.restype = z3.FuncDecl
z3strlib.z3str_contains_decl.argtypes = []
z3strlib.z3str_startswith_decl.restype = z3.FuncDecl
z3strlib.z3str_startswith_decl.argtypes = []
z3strlib.z3str_endswith_decl.restype = z3.FuncDecl
z3strlib.z3str_endswith_decl.argtypes = []
z3strlib.z3str_replace_decl.restype = z3.FuncDecl
z3strlib.z3str_replace_decl.argtypes = []
z3strlib.z3str_lastindexof_decl.restype = z3.FuncDecl
z3strlib.z3str_lastindexof_decl.argtypes = []
z3strlib.z3str_charat_decl.restype = z3.FuncDecl
z3strlib.z3str_charat_decl.argtypes = []
#z3strlib.z3str_str2reg_decl.restype = z3.FuncDecl
#z3strlib.z3str_str2reg_decl.argtypes = []
#z3strlib.z3str_regexstar_decl.restype = z3.FuncDecl
#z3strlib.z3str_regexstar_decl.argtypes = []
#z3strlib.z3str_regexin_decl.restype = z3.FuncDecl
#z3strlib.z3str_regexin_decl.argtypes = []
#z3strlib.z3str_regexunion_decl.restype = z3.FuncDecl
#z3strlib.z3str_regexunion_decl.argtypes = []
#z3strlib.z3str_regexconcat_decl.restype = z3.FuncDecl
#z3strlib.z3str_regexconcat_decl.argtypes = []
#z3strlib.z3str_unroll_decl.restype = z3.FuncDecl
#z3strlib.z3str_unroll_decl.argtypes = []
#z3strlib.z3str_regexdigit_decl.restype = z3.FuncDecl
#z3strlib.z3str_regexdigit_decl.argtypes = []
z3strlib.z3str_register_vars.restype = None
z3strlib.z3str_register_vars.argtypes = [z3.Ast]
z3strlib.setAlphabet.restype = None
z3strlib.setAlphabet.argtypes = []
z3strlib.setAlphabet7bit.restype = None
z3strlib.setAlphabet7bit.argtypes = []
z3strlib.z3str_basic_str_var_axioms.restype = None
z3strlib.z3str_basic_str_var_axioms.argtypes = []

## Set the default Z3py context to use z3str
ctx = z3.main_ctx()
ctx.ctx = z3strlib.z3str_mk_context()
z3strlib.setAlphabet7bit()

## Wrappers around the various z3str_*() functions in libz3str2.so
def StringSort():
  ctx = z3.main_ctx()
  sort = z3strlib.z3str_mk_string_sort()
  return z3.SortRef(sort, ctx)

"""
def RegexSort():
  ctx = z3.main_ctx()
  sort = z3strlib.z3str_mk_regex_sort()
  return z3.SortRef(sort, ctx)
"""

def string_concat():
  ctx = z3.main_ctx()
  decl = z3strlib.z3str_concat_decl()
  return z3.FuncDeclRef(decl, ctx)

def string_length():
  ctx = z3.main_ctx()
  decl = z3strlib.z3str_length_decl()
  return z3.FuncDeclRef(decl, ctx)

def string_substring():
  ctx = z3.main_ctx()
  decl = z3strlib.z3str_substring_decl()
  return z3.FuncDeclRef(decl, ctx)

def string_indexof():
  ctx = z3.main_ctx()
  decl = z3strlib.z3str_indexof_decl()
  return z3.FuncDeclRef(decl, ctx)

def string_indexof2():
  ctx = z3.main_ctx()
  decl = z3strlib.z3str_indexof2_decl()
  return z3.FuncDeclRef(decl, ctx)

def string_contains():
  ctx = z3.main_ctx()
  decl = z3strlib.z3str_contains_decl()
  return z3.FuncDeclRef(decl, ctx)

def string_startswith():
  ctx = z3.main_ctx()
  decl = z3strlib.z3str_startswith_decl()
  return z3.FuncDeclRef(decl, ctx)

def string_endswith():
  ctx = z3.main_ctx()
  decl = z3strlib.z3str_endswith_decl()
  return z3.FuncDeclRef(decl, ctx)

def string_replace():
  ctx = z3.main_ctx()
  decl = z3strlib.z3str_replace_decl()
  return z3.FuncDeclRef(decl, ctx)

def string_lastindexof():
  ctx = z3.main_ctx()
  decl = z3strlib.z3str_lastindexof_decl()
  return z3.FuncDeclRef(decl, ctx)

def string_charat():
  ctx = z3.main_ctx()
  decl = z3strlib.z3str_charat_decl()
  return z3.FuncDeclRef(decl, ctx)

"""
def string_str2reg():
  ctx = z3.main_ctx()
  decl = z3strlib.z3str_str2reg_decl()
  return z3.FuncDeclRef(decl, ctx)

def string_regexstar():
  ctx = z3.main_ctx()
  decl = z3strlib.z3str_regexstar_decl()
  return z3.FuncDeclRef(decl, ctx)

def string_regexin():
  ctx = z3.main_ctx()
  decl = z3strlib.z3str_regexin_decl()
  return z3.FuncDeclRef(decl, ctx)

def string_regexunion():
  ctx = z3.main_ctx()
  decl = z3strlib.z3str_regexunion_decl()
  return z3.FuncDeclRef(decl, ctx)

def string_regexconcat():
  ctx = z3.main_ctx()
  decl = z3strlib.z3str_regexconcat_decl()
  return z3.FuncDeclRef(decl, ctx)

def string_unroll():
  ctx = z3.main_ctx()
  decl = z3strlib.z3str_unroll_decl()
  return z3.FuncDeclRef(decl, ctx)

def string_regexdigit():
  ctx = z3.main_ctx()
  decl = z3strlib.z3str_regexdigit_decl()
  return z3.FuncDeclRef(decl, ctx)
"""

def z3str_register(expr):
  z3strlib.z3str_register_vars(expr.as_ast())

def z3str_basic_str_var_axioms():
  z3strlib.z3str_basic_str_var_axioms()

## Wrapper around Z3's old solver API; unfortunately, z3str seems
## to work only with the old solver API, and not with the new one.
##
## WARNING: z3str does not seem to clean up in-memory state after
## solving, so it's probably best to fork off a separate process
## to invoke z3str_check_and_model(), and then send the results
## to the parent process using a non-Z3 representation like JSON.
def check_and_model(expr):
  z3str_register(expr)
  z3str_basic_str_var_axioms()
  z3.z3core.Z3_assert_cnstr(ctx.ctx, expr.as_ast())

  _m = z3.Model(None)
  _ok = z3.z3core.Z3_check_and_get_model(ctx.ctx, ctypes.byref(_m))
  ok = z3.CheckSatResult(_ok)
  if ok == z3.sat:
    m = z3.ModelRef(_m, ctx)
    return (ok, m)
  else:
    return (ok, None)

Concat = string_concat()
Length = string_length()
SubString = string_substring()
Indexof = string_indexof()
Indexof2 = string_indexof2()
Contains = string_contains()
StartsWith = string_startswith()
EndsWith = string_endswith()
Replace = string_replace()
LastIndexof =  string_lastindexof()
CharAt = string_charat()
"""
Str2Reg = string_str2reg()
RegexStar = string_regexstar()
RegexIn = string_regexin()
RegexUnion = string_regexunion()
RegexConcat = string_regexconcat()
Unroll = string_unroll()
RegexDigit = string_regexdigit()
"""

def encode_string(v):
  enc = "__cOnStStR_" + "".join(["_x%02x" % ord(c) for c in v])
  return z3.Const(enc, StringSort())

