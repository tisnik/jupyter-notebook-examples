
(ns simple-plot
  (:use (incanter core stats charts symbolic optimize)))

(defn display
    [chart]
    (.createBufferedImage chart 640 480))

(def pi java.lang.Math/PI)
 
(display (function-plot sin 0 pi))

(display (function-plot (deriv-fn [t] (sin t) t) 0 pi))

(display (doto (function-plot sin 0 pi)
               (add-function (deriv-fn [t] (sin t) t) 0 pi)))

(defn sinc
    [t]
    (/ (sin t) t))
 
(display
  (doto (function-plot sinc -10 10)
        (add-function (derivative sinc) -10 10)))

(display
  (doto (function-plot sinc -10 10 :x-label "t" :y-label "sinc + deriv sinc")
        (add-function (derivative sinc :dx 5) -10 10)))

(display
    (doto (function-plot sinc -10 10 :x-label "t" :y-label "sinc + deriv sinc")
          (add-function (derivative sinc) -10 10)
          (add-function (derivative sinc :dx 1/2) -10 10)
          (add-function (derivative sinc :dx 1) -10 10)
          (add-function (derivative sinc :dx 5) -10 10)))
