#!/bin/bash
if [ $1 ]
then
    mkdir -p input/$1
    echo  $(cat cookie_aoc)
    curl --cookie $(cat cookie_aoc) https://adventofcode.com/2023/day/$1/input > input/$1/input
else
    echo "Error: no day specified"
fi