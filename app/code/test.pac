function FindProxyForURL(url, host) {

	if (isInNet(myIpAddress(), "192.168.1.0", "255.255.255.0")) {
		return "PROXY 192.168.1.1:3128";
	}

	if (isInNet(myIpAddress(), "10.10.10.0", "255.255.255.0")) {
		return "PROXY 10.10.10.1:3128";
	}

	else {
		return "DIRECT";
	}
	

}
