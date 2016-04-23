#ifndef __Z3STR_h__
#define __Z3STR_h__

#include "z3.h"


Z3_context mk_string_context();
Z3_theory mk_string_theory(Z3_context ctx);

Z3_sort mk_string_sort(Z3_theory t);
Z3_ast string_concat(Z3_theory t, Z3_ast s1, Z3_ast s2);
Z3_ast string_length(Z3_theory t, Z3_ast s);
Z3_ast string_substr(Z3_theory t, Z3_ast s, Z3_ast pos, Z3_ast len);
Z3_ast string_indexof(Z3_theory t, Z3_ast s1, Z3_ast s2);
Z3_ast string_indexof2(Z3_theory t, Z3_ast s1, Z3_ast s2, Z3_ast pos);
Z3_ast string_contains(Z3_theory t, Z3_ast s1, Z3_ast s2);
Z3_ast string_startswith(Z3_theory t, Z3_ast s1, Z3_ast s2);
Z3_ast string_endswith(Z3_theory t, Z3_ast s1, Z3_ast s2);
Z3_ast string_replace(Z3_theory t, Z3_ast s1, Z3_ast s2, Z3_ast s3);
Z3_ast string_lastindexof(Z3_theory t, Z3_ast s1, Z3_ast s2);
Z3_ast string_charat(Z3_theory t, Z3_ast s, Z3_ast pos);

#endif
