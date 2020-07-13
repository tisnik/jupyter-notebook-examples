
(ns simple-plot
  (:use (incanter core stats charts symbolic)))

(defn display
    [chart]
    (.createBufferedImage chart 640 480))

(defn sinc
    [t]
    (/ (sin t) t))

(display (function-plot sinc -10 10))

(display (function-plot
             (deriv-fn [t] (/ (sin t) t) t)
             -20 20))

(display
    (doto (function-plot sinc -10 10)
          (add-function (deriv-fn [t] (/ (sin t) t) t) -10 10)))
