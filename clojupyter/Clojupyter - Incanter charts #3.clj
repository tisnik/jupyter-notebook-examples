
(ns simple-plot
  (:use (incanter core stats charts)))

(defn display
    [chart]
    (.createBufferedImage chart 640 480))

(def seasons (mapcat identity (repeat 3 ["jaro" "léto" "podzim" "zima"])))

seasons

(def years (mapcat identity (repeat 4 [2016 2017 2018 2019 2020])))

(def values (sample-uniform 12 :integers true :max 100))

(display (bar-chart years values :group-by seasons :legend true :x-label "Rok" :y-label "Úroda"))
