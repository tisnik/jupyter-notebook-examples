
(ns simple-plot
  (:use (incanter core stats charts)))

(defn display
    [chart]
    (.createBufferedImage chart 640 480))

(def hody-kostkou (take 10 (repeatedly #(inc (rand-int 6)))))

(display (bar-chart (range 1 (inc (count hody-kostkou)))
                    hody-kostkou
                    :x-label "Pokusy"
                    :y-label "Výsledek hodu"
                    :legend true))

(def indexy (range 1 (inc (count hody-kostkou))))
(display (bar-chart indexy hody-kostkou :x-label "Pokusy" :y-label "Výsledek hodu" :legend true))

(def indexy (range 1 (inc (count hody-kostkou))))
(display (bar-chart indexy hody-kostkou :x-label "Pokusy" :y-label "Výsledek hodu" :legend true :title "Hody kostkou"))
