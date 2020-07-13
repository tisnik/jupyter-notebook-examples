for file in *.ipynb
do
    jupyter nbconvert --to script "$file"
done
