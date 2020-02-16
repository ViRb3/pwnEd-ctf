#!/bin/bash

for i in {1..64}
do
   base64 -d flag$i.txt > flag$(($i+1)).txt
done