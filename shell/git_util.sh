#!/usr/bin/env bash
git status
git add ./
echo "Please input commit message: "
read commitMsg
git commit -m commitMsg
read -n 1 -p "Press any key to start to push..."
git push
read -n 1 -p "Press any key to end..."