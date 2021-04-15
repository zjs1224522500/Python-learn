#!/bin/bash
echo -e "\033[36m=====================Build tcmu-runner. (4 steps)============ \033[0m"

echo -e "\033[36m=====================Step1. Check tcmu-runner.============ \033[0m"
systemctl status tcmu-runner
systemctl stop tcmu-runner

echo -e "\033[36m=====================Step2. Build tcmu-runner.============ \033[0m"

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
# cd $DIR/../extra && ./make_runnerrpms.sh
cd $DIR/../
rm -rf build/*
mkdir build
cd build
cmake ../ -Dwith-glfs=false -Dwith-qcow=false -Dwith-zbc=false -Dwith-fbo=false  -DSUPPORT_SYSTEMD=ON -DCMAKE_INSTALL_PREFIX=/usr
make
make install

echo -e "\033[36m=====================Step3. Run tcmu-runner.============ \033[0m"
cd $DIR/../
cp -rf tcmu-runner.conf /etc/dbus-1/system.d/
cp -rf org.kernel.TCMUService1.service /usr/share/dbus-1/system-services/
cp -rf tcmu-runner.service /lib/systemd/system
cp -rf tcmu.conf /etc/tcmu/

echo -e "\033[36m=====================Step4. Check tcmu-runner status.============ \033[0m"
systemctl daemon-reload
systemctl start tcmu-runner
systemctl status tcmu-runner
