
(use '(incanter core stats charts io))

(-> (sample-normal 10000)
    histogram
    (.createBufferedImage 600 400))

(-> (scatter-plot (sample-normal 1000) 
                  (sample-normal 1000)
                  :x-label "x" :y-label "y")
    (.createBufferedImage 600 400))
