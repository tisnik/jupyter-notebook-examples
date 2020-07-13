
(import java.awt.image.BufferedImage)

(defn create
  "Create new bitmap."
  [width height]
  (new BufferedImage width height BufferedImage/TYPE_INT_RGB))

(defn ->rgb
  [r g b]
  (bit-or b
          (bit-shift-left g 8)
          (bit-shift-left r 16)))

(defn putpixel
  "Change pixel color."
  ( [bitmap x y rgb]
    (.setRGB bitmap x y rgb))
  ( [bitmap x y r g b]
    (.setRGB bitmap x y (->rgb r g b))))

(create 256 256)

(let [bitmap (create 256 256)]
    (doseq [y (range 256)]
        (doseq [x (range 256)]
            (putpixel bitmap x y x 255 y)))
    bitmap)
