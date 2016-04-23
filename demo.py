#!/usr/bin/env python

## Must import z3str2 first!
import z3str2
import z3

x = z3.Const('x', z3str2.StringSort())
y = z3.Const('y', z3str2.StringSort())
z = z3.Const('z', z3str2.StringSort())
i = z3.Const('i', z3.IntSort())

e = z3.And(x == z3str2.Concat(y, z),
           i == z3str2.Length(x),
           z3str2.Length(y) == z3str2.Length(z),
           i == 8)
print e

(ok, m) = z3str2.check_and_model(e)

print ok
print m
