
nil

42

true

false

(range 10)

(for [i (range 10)]
    (* i i))

(defn even
    [x]
    (zero? (mod x 2)))

(even 0)

(even 1)

(filter even (range 10))

(defn factorial [n]
    (reduce * (range 1 (inc n))))

(factorial 10)

(map factorial (range 10))

(map factorial (filter even (range 10)))

(->> (range 10)
    (filter even)
    (map factorial))
