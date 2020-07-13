
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

(defn immutable-matrix-operators
    "Test chování operátorů předefinovaných ve jmenném prostoru
     clojure.core.matrix.operators."
    [matrix1 matrix2]
    (println "*** Test základních operátorů aplikovaných na matice ***")
    (println "Vstupní data (matice):")
    (print-matrix matrix1)
    (print-matrix matrix2)
    (println "Vyhodnocení:")
    ; operace provedené mezi maticí a skalární hodnotou
    (print-matrix (+ matrix1 10))
    (print-matrix (- matrix1 10))
    (print-matrix (* matrix1 10))
    (print-matrix (/ matrix1 10))
    ; operace provedené mezi skalární hodnotou a maticí
    (print-matrix (+ 10 matrix1))
    (print-matrix (- 10 matrix1))
    (print-matrix (* 10 matrix1))
    (try
        (print-matrix (/ 10 matrix1))
        (catch java.lang.ArithmeticException e
            (println "Exception: " (.toString e))))
    ; operace provedené mezi dvěma maticemi
    (print-matrix (+ matrix1 matrix2))
    (print-matrix (- matrix1 matrix2))
    (print-matrix (* matrix1 matrix2))
    (try
        (print-matrix (/ matrix1 matrix2))
        (catch java.lang.ArithmeticException e
            (println "Exception: " (.toString e))))
    (println))

(defn immutable-matrix-tests
    "Spustí všechny testovací funkce s neměnitelnými maticemi"
    []
    (let [m0 (zero-matrix 3 3)
          m1 (identity-matrix 3 3)
          m2 (array [[1 2 3] [4 5 6] [7 8 9]])
          m3 (array [[0 1] [2 3]])]
          (immutable-matrix-operators m0 m1)
          (immutable-matrix-operators m1 m2)))

(immutable-matrix-tests)

(defn immutable-matrix-special-operators
    "Test chování speciálních operátorů předefinovaných
     ve jmenném prostoru clojure.core.matrix.operators."
    [matrix1 matrix2]
    (println "*** Test speciálních operátorů aplikovaných na matice ***")
    (println "Vstupní data (matice):")
    (print-matrix matrix1)
    (print-matrix matrix2)
    (println "Vyhodnocení:")
    ; operace provedené mezi maticí a skalární hodnotou
    (print-matrix (** matrix1 10))
    ; operace provedené mezi skalární hodnotou a maticí
    (print-matrix (** 10 matrix1))
    ; operace provedené mezi dvěma maticemi
    (print-matrix (** matrix1 matrix2))
    ; operátor ekvivalence aplikovaný na dvojici matic
    (print-vector (== matrix1 matrix2))
    (print-vector (== matrix1 matrix1))
    (print-vector (== matrix1 (identity-matrix 3 3)))
    (print-vector (== matrix2 (array [[1 2 3] [4 5 6] [7 8 9]])))
    (println))

(defn immutable-matrix-tests-2
    "Spustí všechny testovací funkce s neměnitelnými maticemi"
    []
    (let [m1 (identity-matrix 3 3)
          m2 (array [[1 2 3] [4 5 6] [7 8 9]])]
          (immutable-matrix-special-operators m1 m2)))

(immutable-matrix-tests-2)

(defn immutable-matrix-functions
    "Test chování vybraných funkcí, které lze nalézt ve jmenných prostorech
     clojure.core.matrix a clojure.core.matrix.operators."
    [matrix1 matrix2 matrix3]
    (println "*** Test funkcí aplikovaných na matice ***")
    (println "Vstupní data (matice):")
    (print-matrix matrix1)
    (print-matrix matrix2)
    (print-matrix matrix3)
    (println "Vyhodnocení:")
    (print-vector (emin matrix1))
    (print-vector (emin matrix2))
    (print-vector (emin matrix3))
    (print-vector (emax matrix1))
    (print-vector (emax matrix2))
    (print-vector (emax matrix3))
    (print-vector (esum matrix1))
    (print-vector (esum matrix2))
    (print-vector (esum matrix3))
    (print-vector (ecount matrix1))
    (print-vector (ecount matrix2))
    (print-vector (ecount matrix3))
    (print-vector (zero-count matrix1))
    (print-vector (zero-count matrix2))
    (print-vector (zero-count matrix3))
    (print-matrix (inverse matrix1))
    (print-matrix (inverse matrix2))
    (print-matrix (inverse matrix3))
    (print-matrix (non-zero-indices matrix1))
    (print-matrix (non-zero-indices matrix2))
    (print-matrix (non-zero-indices matrix3))
    (print-matrix (outer-product matrix1))
    (print-matrix (outer-product matrix2))
    (print-matrix (outer-product matrix3))
    (print-matrix (join matrix1 matrix2))
    (println))

(defn immutable-matrix-tests-3
    "Spustí všechny testovací funkce s neměnitelnými maticemi"
    []
    (let [m1 (identity-matrix 3 3)
          m2 (array [[1 2 3] [4 5 6] [7 8 9]])
          m3 (array [[0 1] [2 3]])]
          (immutable-matrix-functions m1 m2 m3)))

(immutable-matrix-tests-3)

(def v1 (array (range 1 11)))
 
(pm (outer-product v1 v1))

(defn mutable-matrix-operators
    "Test chování operátorů předefinovaných ve jmenném prostoru
     clojure.core.matrix.operators na měnitelné matice"
    [matrix1 matrix2]
    (println "*** Test základních operátorů aplikovaných na měnitelné matice ***")
    (println "Vstupní data (matice):")
    (print-matrix matrix1)
    (print-matrix matrix2)
    (println "Vyhodnocení:")
    ; operace provedené mezi dvěma maticemi
    (print-matrix (+= matrix1 matrix2))
    (print-matrix (-= matrix1 matrix2))
    (print-matrix (*= matrix1 matrix2))
    (print-matrix (div= matrix1 matrix2))
    (println))

(defn mutable-matrix-functions
    "test chování vybraných funkcí, které lze nalézt ve jmenných prostorech
     clojure.core.matrix a clojure.core.matrix.operators na měnitelné matice."
    [matrix1 matrix2 matrix3]
    (println "*** test funkcí aplikovaných na měnitelné matice ***")
    (println "vstupní data (matice):")
    (print-matrix matrix1)
    (print-matrix matrix2)
    (print-matrix matrix3)
    (println "vyhodnocení:")
    (print-matrix (sin! matrix1))
    (print-matrix (sin! matrix2))
    (print-matrix (sin! matrix3))
    (print-matrix (fill! matrix1 0))
    (print-matrix (fill! matrix2 1))
    (print-matrix (fill! matrix3 2))
    (println))

(defn mutable-matrix-tests
    []
    (let [m0 (mutable (zero-matrix 3 3))
          m1 (mutable (identity-matrix 3 3))
          m2 (mutable (array [[1 2 3] [4 5 6] [7 8 9]]))]
          (mutable-matrix-operators m1 m2)
          (mutable-matrix-functions m0 m1 m2)))

(mutable-matrix-tests)

(defn as-vector-test
    "Test funkce as-vector."
    [matrix]
    (print-vector (as-vector matrix)))

(defn submatrix-test
    "Test funkce submatrix."
    [matrix]
    (print-matrix (submatrix matrix 0 3 0 3))
    (print-matrix (submatrix matrix 1 5 2 4))
    (print-matrix (submatrix matrix 0 5 0 1))
    (print-matrix (submatrix matrix 0 1 0 5))
    (print-matrix (submatrix matrix [[0 10][2 2]])))

(defn select-test
    "Test funkce select."
    [matrix]
    (print-matrix (select matrix 0 0))
    (print-matrix (select matrix 5 5))
    (print-matrix (select matrix 1 :all))
    (print-matrix (select matrix :all 1))
    (print-matrix (select matrix 9 :all))
    (print-matrix (select matrix :all 9)))

(def big-matrix
    (-> (range 0 100) (reshape [10 10])))

(defn views-tests
    "Pohledy na matice."
    []
    (println "*** Test pohledů na matice ***")
    (let [m1 big-matrix]
        (println "Vstupní matice:")
        (print-matrix m1)
        (as-vector-test m1)
        (submatrix-test m1)
        (select-test m1)))

(views-tests)
