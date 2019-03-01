#!/usr/bin/env bash
echo "hello elvis"
a=3
b=5

# + - \* /
val=`expr $a + $b`
echo "Total value : $val"
val=`expr $a - $b`
echo "Total value : $val"
val=`expr $a \* $b`
echo "Total value : $val"
val=`expr $a / $b`
echo "Total value : $val"

# == !=
if [ $a == $b ]
then
   echo "a is equal to b"
fi
if [ $a != $b ]
then
   echo "a is not equal to b"
fi

# -eq -ne -gt -lt -ge -le
if [ $a -eq $b ]
then
   echo "true"
else
   echo "false"
fi

if [ $a -ne $b ]
then
   echo "true"
else
   echo "false"
fi

if [ $a -gt $b ]
then
   echo "true"
else
   echo "false"
fi

if [ $a -lt $b ]
then
   echo "true"
else
   echo "false"
fi

if [ $a -ge $b ]
then
   echo "true"
else
   echo "false"
fi

if [ $a -le $b ]
then
   echo "true"
else
   echo "false"
fi

# string
mText="hello"  # define string
mText2="world"
mText3=$mText" "$mText2  # concat string
echo $mText3  # print string
echo ${#mText3}  # print length of string
echo ${mText3:1:4}  # sub string