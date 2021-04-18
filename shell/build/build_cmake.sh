#!/usr/bin/env bash

wget https://github.com/Kitware/CMake/releases/download/v3.18.6/cmake-3.18.6-Linux-x86_64.tar.gz
tar -zxvf cmake-3.18.6-Linux-x86_64.tar.gz
cp -rf cmake-3.18.6-Linux-x86_64 /usr/local/cmake
echo 'PATH=/usr/local/cmake/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
cmake -version