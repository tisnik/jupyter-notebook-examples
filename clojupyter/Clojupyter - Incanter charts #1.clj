
(ns simple-plot
  (:use (incanter core stats charts)))

(def hody-kostkou (take 10 (repeatedly #(inc (rand-int 6)))))

(->
    (bar-chart (range 1 (inc (count hody-kostkou)))
               hody-kostkou)
    (.createBufferedImage 640 480))

(->
    (bar-chart (range 1 11)
               hody-kostkou)
    (.createBufferedImage 640 480))

(->
    (bar-chart (range 1 (inc (count hody-kostkou)))
               hody-kostkou
               :x-label "Pokusy"
               :y-label "Výsledek hodu")
    (.createBufferedImage 640 480))
