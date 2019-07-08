#!/usr/bin/env bash
git status
git add ./
#oldIFS=$IFS
#IFS=\n
read -p "Please input commit message: " -a commitMsgArray
commitMsg=''
for str in commitMsgArray ; do
    commitMsg=${commitMsg} ${str}
done
echo ${commitMsg}
git commit -m ${commitMsg}
read -n 1 -p "Press any key to start to push..."
git push
read -n 1 -p "Press any key to end..."