
(ns simple-plot
  (:use (incanter core stats charts symbolic optimize)))

(defn display
    [chart]
    (.createBufferedImage chart 640 480))

(def pi java.lang.Math/PI)
 
(defn sinc
    [t]
    (/ (sin t) t))
 
(def d0 (/ (* pi 5) 2))

(display
  (doto (function-plot sinc -10 10 :x-label "t" :y-label "sinc + deriv sinc")
        (set-y-range -1/2 3/2)
        (add-function (derivative sinc) -10 10)
        (add-pointer 0 1 :text "deriv=0")
        (add-pointer d0 (sinc d0) :text "deriv=0")
        (add-pointer (- d0) (sinc (- d0)) :text "deriv=0")))
