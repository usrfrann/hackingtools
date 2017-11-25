#!/bin/bash
#date :20171107

echo HI! 
echo What is your name? 
STR="Francois" 
echo Hi $STR

LOCA=LA
function whereAreYouFrom {
	local LOCA="NY"
       	echo I am from $LOCA
}
echo I am a global here using LOCA in $LOCA
echo Where are you from instance function LOCA?
whereAreYouFrom
echo $LOCA

echo Do you like NY?
ANS="yes"
if [ $ANS="yes" ]; then
       	echo "Oh Me too NY is great and the pizza is tasty"
else 
	echo "Yeah I hate NY too it smells bad!" 
fi

echo Can you count too three going the for way and the while way too?
echo I can do better I can count by twos all the way to ten with for 
for i in `seq 2 10`;
do 
	echo $i
done

echo but I can only count two three using while
COUNTER=0
echo SEE!
while [ $COUNTER -lt 3 ]; do
	echo $COUNTER  
        let COUNTER=COUNTER+1 
done

echo How do you pass paramaters using functions 

function e { 
	echo $1
}
e Hello
e Jasper

echo Are you sure you are Jasper?
OPTIONS="JASPER CHUCK" 
select opt in $OPTIONS; do
	if [ "$opt" = "JASPER" ]; then 
		echo Hi Jasper DONT Bite
	elif [ "$opt" = "CHUCK" ]; then 
		echo Rest in Peace Chuck and live forever in this code if it touches the web
	else
		echo Whoe are you
	        break 
	fi
done

echo Please tell me that you will be doing cyber stuff one day 
read $ANS
if [ "$ANS" = "yes" ]; then
       echo Just hang in there and youll get there 
else 
 echo Dont give	up you will be waking up and doing something you love every day
fi

