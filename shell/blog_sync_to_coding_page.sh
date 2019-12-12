#!/usr/bin/env bash
path="D:\zjs1224522500.github.io"
echo ${path}
cd ${path}
dirs
git status
git pull --rebase
git add ./
git commit -m "SYNC Github Page"
git push coding
read -n 1 -p "Press any key to continue..."