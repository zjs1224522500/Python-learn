#!/usr/bin/env bash
path="D:\zjs1224522500.github.io"
remote_branch_name="coding"
remote_branch_url="https://git.coding.net/qcloud_3562257030/Blog.git"
echo ${path}
cd ${path}
dirs
git status
git pull --rebase
check_remote_branch=`git remote show ${remote_branch_name}`
echo -e "command show remote: ${check_remote_branch}"

if [[ ! -n "${check_remote_branch}" ]]
then
    echo -e "Not contained.\n"
    echo "Add new branch with name ${remote_branch_name} and url ${remote_branch_url}"
    git remote add ${remote_branch_name} ${remote_branch_url}
else
    echo "Contained."
fi
git push ${remote_branch_name}
read -n 1 -p "Press any key to continue..."