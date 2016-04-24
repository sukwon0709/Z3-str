#ifndef __Z3STR_h__
#define __Z3STR_h__

#include "z3.h"

#ifdef __cplusplus
extern "C" {
#endif

Z3_context z3str_mk_context();
Z3_theory z3str_get_theory();
void setAlphabet();

Z3_sort z3str_mk_string_sort();
Z3_ast z3str_string_concat(Z3_ast s1, Z3_ast s2);
Z3_ast z3str_string_length(Z3_ast s);
Z3_ast z3str_string_substr(Z3_ast s, Z3_ast pos, Z3_ast len);
Z3_ast z3str_string_indexof(Z3_ast s1, Z3_ast s2);
Z3_ast z3str_string_indexof2(Z3_ast s1, Z3_ast s2, Z3_ast pos);
Z3_ast z3str_string_contains(Z3_ast s1, Z3_ast s2);
Z3_ast z3str_string_startswith(Z3_ast s1, Z3_ast s2);
Z3_ast z3str_string_endswith(Z3_ast s1, Z3_ast s2);
Z3_ast z3str_string_replace(Z3_ast s1, Z3_ast s2, Z3_ast s3);
Z3_ast z3str_string_lastindexof(Z3_ast s1, Z3_ast s2);
Z3_ast z3str_string_charat(Z3_ast s, Z3_ast pos);
void z3str_register_vars(Z3_ast n);
void z3str_basic_str_var_axioms();

#ifdef __cplusplus
}
#endif

#endif
