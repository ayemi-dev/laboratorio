#!/bin/bash
set -m
cat servidor
./servidor &
echo $!
jobs
ps -p $! | cut -c1-9
sleep 1
curl -sI -m 2 127.0.0.1:8000 | head -n 1
kill -STOP $!
curl -sI -m 2 127.0.0.1:8000 | head -n 1
jobs
kill -CONT %1
curl -sI -m 2 127.0.0.1:8000 | head -n 1
kill %1
wait $!
echo $?
