#!/bin/bash
# display ALL HTTP methods.
curl -sI  "$1" | grep "Allow" | cut -d " " -f 2-
