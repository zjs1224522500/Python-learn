#!/usr/bin/env bash
git status
git add ./
git commit -m "Add new script"
read -n 1 -p "Press any key to start to push..."
git push
read -n 1 -p "Press any key to start to push..."