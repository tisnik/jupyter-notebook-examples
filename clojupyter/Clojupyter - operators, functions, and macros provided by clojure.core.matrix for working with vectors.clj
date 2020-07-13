
(use 'clojure.core.matrix)
(use 'clojure.core.matrix.operators)

(defmacro print-vector
    "Makro, které na standardní výstup vypíše výraz a následně i
     hodnotu tohoto výrazu s použitím funkce pm (pretty print matrix).
     Předpokládá se, že se výraz vyhodnotí na vektor."
    [expression]
    `(do (printf "    %-32s =  " '~expression)
         (pm ~expression)))

(defmacro print-matrix
    "Makro, které na standardní výstup vypíše výraz a následně i
     hodnotu tohoto výrazu s použitím funkce pm (pretty print matrix).
     Předpokládá se, že se výraz vyhodnotí na matici"
    [expression]
    `(do (println "   " '~expression "=")
         (pm ~expression)
         (println)))

(defn immutable-vector-operators
    "Test chování operátorů předefinovaných ve jmenném prostoru
     clojure.core.matrix.operators."
    [vector1 vector2]
    (println "*** Test základních operátorů aplikovaných na vektory ***")
    (println "Vstupní data (vektory):")
    (print-vector vector1)
    (print-vector vector2)
    (println "Vyhodnocení:")
    ; operace provedené mezi vektorem a skalární hodnotou
    (print-vector (+ vector1 10))
    (print-vector (- vector1 10))
    (print-vector (* vector1 10))
    (print-vector (/ vector1 10))
    ; operace provedené mezi skalární hodnotou a vektorem
    (print-vector (+ 10 vector1))
    (print-vector (- 10 vector1))
    (print-vector (* 10 vector1))
    (print-vector (/ 10 vector1))
    ; operace provedené mezi dvěma vektory (zde stejné délky)
    (print-vector (+ vector1 vector2))
    (print-vector (- vector1 vector2))
    (print-vector (* vector1 vector2))
    (print-vector (/ vector1 vector2))
    (println))

(defn immutable-vector-special-operators
    "Test chování speciálních operátorů předefinovaných
     ve jmenném prostoru clojure.core.matrix.operators."
    [vector1 vector2]
    (println "*** Test speciálních operátorů aplikovaných na vektory ***")
    (println "Vstupní data (vektory):")
    (print-vector vector1)
    (print-vector vector2)
    (println "Vyhodnocení:")
    ; operace provedené mezi vektorem a skalární hodnotou
    (print-vector (** vector1 10))
    ; operace provedené mezi skalární hodnotou a vektorem
    (print-vector (** 10 vector1))
    ; operace provedené mezi dvěma vektory (zde stejné délky)
    (print-vector (** vector1 vector2))
    ; operátor ekvivalence
    (print-vector (== vector1 vector2))
    (print-vector (== vector1 vector1))
    (print-vector (== vector1 (array [1 2 3])))
    (print-vector (== vector1 [1 2 3]))
    (print-vector (== vector1 '(1 2 3)))
    (println))

(let [v1 (array [1 2 3])
      v2 (array [2 3 4])]
      (immutable-vector-operators v1 v2)
      (immutable-vector-special-operators v1 v2))

(defn immutable-vector-functions
    "Test chování vybraných funkcí, které lze nalézt ve jmenných prostorech
     clojure.core.matrix a clojure.core.matrix.operators."
    [vector1 vector2 vector3]
    (println "*** Test funkcí aplikovaných na vektory ***")
    (println "Vstupní data (vektory):")
    (print-vector vector1)
    (print-vector vector2)
    (print-vector vector3)
    (println "Vyhodnocení:")
    (print-vector (emin vector1))
    (print-vector (emin vector2))
    (print-vector (emin vector3))
    (print-vector (emax vector1))
    (print-vector (emax vector2))
    (print-vector (emax vector3))
    (print-vector (normalise vector1))
    (print-vector (normalise vector2))
    (print-vector (normalise vector3))
    (print-vector (length vector1))
    (print-vector (length vector2))
    (print-vector (length vector3))
    (print-vector (length-squared vector1))
    (print-vector (length-squared vector2))
    (print-vector (length-squared vector3))
    (print-vector (distance vector1 vector2))
    (print-vector (distance vector1 vector3))
    (print-vector (distance vector2 vector3))
    (print-vector (join vector1 vector2))
    (print-vector (join vector1 vector2 vector3))
    (println))

(let [v0 (zero-vector 3)
      v1 (array [1 2 3])
      v2 (array [2 3 4])]
      (immutable-vector-functions v0 v1 v2))

(defn immutable-vector-products
    "Skalární a vektorový součin dvou trojsložkových vektorů."
    [vector1 vector2]
    (println "*** Skalární a vektorový součin dvou trojsložkových vektorů ***")
    (println "Vstupní data (vektory):")
    (print-vector vector1)
    (print-vector vector2)
    (println "Vyhodnocení:")
    (print-vector (dot vector1 vector1))
    (print-vector (dot vector1 vector2))
    (print-vector (dot vector2 vector1))
    (print-vector (dot vector2 vector2))
    (print-vector (inner-product vector1 vector1))
    (print-vector (inner-product vector1 vector2))
    (print-vector (inner-product vector2 vector1))
    (print-vector (inner-product vector2 vector2))
    (print-vector (cross vector1 vector1))
    (print-vector (cross vector1 vector2))
    (print-vector (cross vector2 vector1))
    (print-vector (cross vector2 vector2))
    (println))

(let [v0 (zero-vector 3)
      v1 (array [1 2 3])
      v2 (array [2 3 4])
      v3 (array [1 1])]
      (immutable-vector-products v1 v2)
      (immutable-vector-products v0 v1))

(defn mutable-vector-operators
    "Test chování operátorů předefinovaných ve jmenném prostoru
     clojure.core.matrix.operators na měnitelné vektory."
    [vector1 vector2]
    (println "*** Test základních operátorů aplikovaných na měnitelné vektory ***")
    (println "Vstupní data (vektory):")
    (print-vector vector1)
    (print-vector vector2)
    (println "Vyhodnocení:")
    ; operace provedené mezi dvěma vektory (zde stejné délky)
    (print-vector (+= vector1 vector2))
    (print-vector (-= vector1 vector2))
    (print-vector (*= vector1 vector2))
    (print-vector (div= vector1 vector2))
    (println))

(defn mutable-vector-functions
    "Test chování vybraných funkcí, které lze nalézt ve jmenných prostorech
     clojure.core.matrix a clojure.core.matrix.operators na měnitelné vektory."
    [vector1 vector2 vector3]
    (println "*** Test funkcí aplikovaných na měnitelné vektory ***")
    (println "Vstupní data (vektory):")
    (print-vector vector1)
    (print-vector vector2)
    (print-vector vector3)
    (println "Vyhodnocení:")
    (print-vector (sin! vector1))
    (print-vector (sin! vector2))
    (print-vector (sin! vector3))
    (print-vector (fill! vector1 1))
    (print-vector (fill! vector2 2))
    (print-vector (fill! vector3 3))
    (println))

(defn mutable-vector-tests
    []
    (let [v0 (mutable (zero-vector 3))
          v1 (mutable (array [1 2 3]))
          v2 (mutable (array [2 3 4]))]
          (mutable-vector-operators v1 v2)
          (mutable-vector-functions v0 v1 v2)))

(mutable-vector-tests)
