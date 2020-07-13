
(use 'clojure.core.matrix)
(use 'clojure.core.matrix.operators)

(let [M (matrix [[1 2] [3 4]])
      v (matrix [1 2])]
      (pm M)
      (pm v)
      (pm (* v 2))
      (pm (mul M v))
      (pm (* M M))
      (pm (inner-product M v)))

; vektor
(pm (matrix [1 2 3]))

; vektor
(pm (matrix '(1 2 3)))
 
; matice
(pm (matrix [[1 2] [3 4]]))
 
; matice
(pm (matrix (range 1 10)))
 
; matice
(pm (matrix [[1 2 3] [4 5 6] [7 8 9]]))

(zero-matrix 10 1)
(pm *1)

(zero-matrix 1 10)
(pm *1)

(zero-matrix 2 3)
(pm *1)
 
(zero-matrix 4 4)
(pm *1)
 
(identity-matrix 4 4)
(pm *1)

; vektor udává pozice jedniček na jednotlivých řádcích matice
; rozměry matice jsou získány na základě velikosti tohoto vektoru
(permutation-matrix [1 4 2 3 0])
 
(pm *1)
