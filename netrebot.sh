#!/bin/bash

ifconfig wlan0 down
macchanger -r wlan0
ifconfig wlan0 up
service network-manager restart 

