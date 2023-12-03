#!/bin/bash
if [ $1 ]
then
    mkdir -p input/$1
    curl --cookie $(cat cookie_aoc) https://adventofcode.com/2022/day/$1/input > input/$1/input
else
    echo "Error: no day specified"
fi