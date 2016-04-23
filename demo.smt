(declare-const x String)
(declare-const y String)
(declare-const z String)
(declare-const i Int)

(assert (= x (Concat y z)))
(assert (= i (Length x)))
(assert (= (Length y) (Length z)))
(assert (= i 8))

(check-sat)
(get-model)
