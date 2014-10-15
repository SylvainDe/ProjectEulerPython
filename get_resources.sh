#! /bin/bash

for file in p022_names.txt p042_words.txt p054_poker.txt p059_cipher.txt p067_triangle.txt p079_keylog.txt p081_matrix.txt p082_matrix.txt p083_matrix.txt p089_roman.txt p096_sudoku.txt p098_words.txt p099_base_exp.txt p102_triangles.txt p105_sets.txt p107_network.txt p424_kakuro200.txt; do
    echo $file;
    [ -f $file ] || wget "https://projecteuler.net/project/resources/$file" --no-check-certificate -O "$file"
done

