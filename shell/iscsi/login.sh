
#!/bin/bash
iqn=$1

echo "=====================Check sessions======================"
iscsiadm -m session

echo "=====================Session Login======================="
iscsiadm -m node -T $iqn --login

