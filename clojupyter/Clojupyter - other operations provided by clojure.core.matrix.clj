
(use 'clojure.core.matrix)
(use 'clojure.core.matrix.operators)

(def M (matrix [[1 2 3] [4 5 6] [7 8 9]]))
(pm M)
 
(transpose M)
(pm *1)

(def M1 (matrix [[1 2][3 4]]))
 
(def M2 (matrix [[5 6][7 8]]))
 
(pm (+ M1 M2))
(pm (- M1 M2))
(pm (* M1 M2))
(pm (* M1 100))

; zde se nejdříve vypočte inverzní matice k M1
(pm (/ M2 M1))
 
(pm (inverse M1))

(pm (inverse M2))

; vektor
(def v (matrix [1 2 3 4 5 6]))
(pm v)

; 2D matice
(def M (matrix [[1 2] [3 4]]))
(pm M)

; trojrozměrná matice
(def MD (matrix [[ [1 2] [3 4] ] [ [5 6] [7 8] ] ]))
(pm MD)

(dimensionality v)

(dimensionality M)

(dimensionality MD)

(dimensionality 1)

(shape M)

(shape v)

(shape MD)

(def v (matrix [1 2 3 4 5 6]))
(pm v)

; velmi užitečná funkce převzatá z APL: vektor převeden na matici
(reshape v [2 3])
(pm *1)

; jiný tvar matice
(reshape v [3 2])
(pm *1)

(reshape v [1 6])
(pm *1)

(reshape v [6 1])
(pm *1)

; jedná se o oneliner rozepsaný kvůli větší čitelnosti na čtyři řádky
(-> (matrix (range 1 101))
    (reshape [10 10])
    transpose
    pm)

; sekvence operací aplikovaných na matici M1
(-> M1
    transpose
    inverse
    (* 10000)
    transpose
    (* M2)
    (+ M1)
    pm)
