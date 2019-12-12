#!/usr/bin/env bash
git status
git add ./

read -p "Please input commit message: " -a commitMsgArray
commitMsg=''
echo ${commitMsgArray[@]}
commitMsg="${commitMsg} ${commitMsgArray[@]}"
echo ${commitMsg}
git commit -m "${commitMsg}"
read -n 1 -p "Press any key to start to push..."
git push origin master
read -n 1 -p "Press any key to end..."