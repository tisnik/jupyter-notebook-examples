
(ns simple-plot
  (:use (incanter core stats charts)))

(defn display
    [chart]
    (.createBufferedImage chart 640 480))

(def x (range 0 100 0.5))
(def y (map #(/ (sin %) (inc %)) x))
(display (line-chart x y))

(display (doto (line-chart x y)
               (set-y-range -1/2 1/2)))

(display (doto (line-chart x y :title "sinc")
               (set-y-range -1/2 1/2)
               (set-x-label "t")
               (set-y-label "sinc")))
