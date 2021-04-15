#!/usr/bin/env bash
echo "--------------------Begin-----------------"
host=""
remotePort=22832
serviceNames=("ems-admi-service" "ems-flp-odat-service" "ems-configuration-service")
localPort=30515
i=0
step=1
failureCommandResult="FAILED"
staticCommandString="cf ssh -N -L "${localPort}":"${host}":"${remotePort}" "
commandString=${staticCommandString}${serviceNames[i]}
echo ${commandString}
commandResult=`${commandString}`
echo ${commandResult}
while [[ ${commandResult} == *${failureCommandResult}* ]]
do
    i=`expr ${i} + ${step}`
    commandString=${staticCommandString}${serviceNames[i]}
    echo ${commandString}
    commandResult=`${commandString}`
    echo ${commandResult}
done
echo "--------------------End-----------------"
read -n 1 -p "Press any key to continue..."