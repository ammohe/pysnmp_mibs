# PySNMP SMI module. Autogenerated from smidump -f python WLSX-USER6-MIB
# by libsmi2pysnmp-0.1.3 at Tue Jun  3 12:42:18 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( wlsxEnterpriseMibModules, ) = mibBuilder.importSymbols("ARUBA-MIB", "wlsxEnterpriseMibModules")
( ArubaAuthenticationMethods, ArubaEncryptionType, ArubaHTMode, ArubaPhyType, ArubaSubAuthenticationMethods, ArubaUserForwardMode, ) = mibBuilder.importSymbols("ARUBA-TC", "ArubaAuthenticationMethods", "ArubaEncryptionType", "ArubaHTMode", "ArubaPhyType", "ArubaSubAuthenticationMethods", "ArubaUserForwardMode")
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup")
( Bits, Counter32, Counter64, Integer32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, snmpModules, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Integer32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "snmpModules")
( DisplayString, MacAddress, PhysAddress, RowStatus, StorageType, TAddress, TDomain, TextualConvention, TestAndIncr, TimeInterval, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "PhysAddress", "RowStatus", "StorageType", "TAddress", "TDomain", "TextualConvention", "TestAndIncr", "TimeInterval", "TruthValue")
( wlsxSwitchMIB, ) = mibBuilder.importSymbols("WLSX-SWITCH-MIB", "wlsxSwitchMIB")
( wlanESSID, ) = mibBuilder.importSymbols("WLSX-WLAN-MIB", "wlanESSID")

# Objects

wlsxUser6InfoGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 4))
wlsxSwitchUser6Table = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 4, 1))
if mibBuilder.loadTexts: wlsxSwitchUser6Table.setDescription("\nThis Table lists all the users (both wired and wireless) currently\nconnected to the switch. Users are identified by their IP address.")
wlsxSwitchUser6Entry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 4, 1, 1)).setIndexNames((0, "WLSX-USER6-MIB", "user6IpAddress"))
if mibBuilder.loadTexts: wlsxSwitchUser6Entry.setDescription("User Entry")
user6IpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 4, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: user6IpAddress.setDescription("\nIPv6 Address from which the user connected to the switch.")
user6PhyAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 4, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: user6PhyAddress.setDescription("\nPhysical Address of the station from which the user connected to \nthe switch.")
user6Name = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 4, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: user6Name.setDescription("\nName of the User.")
user6Role = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 4, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: user6Role.setDescription("\nThe Role configured for this user.")
user6UpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 4, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: user6UpTime.setDescription("\nTime since the user is connected to the switch.	")
user6AuthenticationMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 4, 1, 1, 6), Integer().subtype(subtypeSpec=SingleValueConstraint(3,1,4,6,2,5,)).subtype(namedValues=NamedValues(("none", 1), ("other", 2), ("web", 3), ("dot1x", 4), ("vpn", 5), ("mac", 6), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: user6AuthenticationMethod.setDescription("\nAuthentication mechanism used by the user to connect to the switch.")
user6Location = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 4, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: user6Location.setDescription("\nLocation of the access point (in Building.Floor.... format), which\nthe user used to connect to the switch.")
user6ServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 4, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: user6ServerName.setDescription("\nName of the Back-end authentication server, used to authenticate\nthe user.")
user6ConnectedVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 4, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: user6ConnectedVlan.setDescription("\nVlan on which the user is connected to the switch.")
user6ConnectedSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 4, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: user6ConnectedSlot.setDescription("\nSlot on switch, where the user connection terminates.")
user6ConnectedPort = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 4, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: user6ConnectedPort.setDescription("\nPort on switch, where the user connection terminates.")
user6BWContractName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 4, 1, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: user6BWContractName.setDescription("\nName of the Bandwidth Contract applied to this user.")
user6BWContractUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 4, 1, 1, 13), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("user", 1), ("shared", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: user6BWContractUsage.setDescription("\nIndicates how the Bandwidth Contract is used.")
user6ConnectedModule = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 4, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: user6ConnectedModule.setDescription("\nModule on switch, where the user connection terminates.")
wlsxUser6MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14)).setRevisions(("1910-01-26 18:06",))
if mibBuilder.loadTexts: wlsxUser6MIB.setOrganization("Aruba Wireless Networks")
if mibBuilder.loadTexts: wlsxUser6MIB.setContactInfo("Postal:    1322 Crossman Avenue\nSunnyvale, CA 94089\nE-mail:     dl-support@arubanetworks.com\nPhone:      +1 408 227 4500")
if mibBuilder.loadTexts: wlsxUser6MIB.setDescription("This MIB module defines MIB objects which provide\ninformation about the IPv6 users in an Aruba controller.")
wlsxUser6AllInfoGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1))
wlsxTotalNumOfUsers6 = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxTotalNumOfUsers6.setDescription("\nTotal Number of the users.")
wlsxUser6Table = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2))
if mibBuilder.loadTexts: wlsxUser6Table.setDescription("\nThis Table lists all the users (both wired and wireless) currently\nconnected to the controller. Users are identified by their MAC \naddress and IP address.")
wlsxUser6Entry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1)).setIndexNames((0, "WLSX-USER6-MIB", "nUser6PhyAddress"), (0, "WLSX-USER6-MIB", "nUser6IpAddress"))
if mibBuilder.loadTexts: wlsxUser6Entry.setDescription("User Entry")
nUser6PhyAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 1), MacAddress()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: nUser6PhyAddress.setDescription("\nMAC address of the station from which the user connected to\nthe controller.")
nUser6IpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: nUser6IpAddress.setDescription("\nIPv6 Address of the user.")
nUser6Name = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUser6Name.setDescription("\nName of the User.")
nUser6Role = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUser6Role.setDescription("\nThe Role configured for this user.")
nUser6UpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUser6UpTime.setDescription("\nTime since the user connected to the controller.	")
nUser6AuthenticationMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 6), ArubaAuthenticationMethods()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUser6AuthenticationMethod.setDescription("\nAuthentication mechanism used by the user to connect to the \ncontroller.")
nUser6SubAuthenticationMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 7), ArubaSubAuthenticationMethods()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUser6SubAuthenticationMethod.setDescription("\nSub Authentication Method")
nUser6AuthServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUser6AuthServerName.setDescription("\nName of the authentication server used to authenticate \nthe user.")
nUser6ExtVPNAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 9), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUser6ExtVPNAddress.setDescription("\nExternal VPN IP Address, if this is a VPN user or 0.0.0.0 if not.")
nUser6ApLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUser6ApLocation.setDescription("\nLocation of the access point to \nwhich the user is associated.")
nUser6ApBSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 11), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUser6ApBSSID.setDescription("\nBSSID of the access point, which \nthe user used to connect to the controller.")
nUser6IsOnHomeAgent = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 12), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUser6IsOnHomeAgent.setDescription("\nThe Object will indicate if the controller is the home controller \n for the user or not.")
nUser6HomeAgentIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 13), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUser6HomeAgentIpAddress.setDescription("\nThe Home agent IP Address of the user. If this user is already on \nthe home controller, then this IP is the controller IP else it \nis the home controller IP address.")
nUser6MobilityStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 14), Integer().subtype(subtypeSpec=SingleValueConstraint(3,1,2,5,4,)).subtype(namedValues=NamedValues(("visitor", 1), ("away", 2), ("associated", 3), ("wired", 4), ("wireless", 5), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUser6MobilityStatus.setDescription("\nThe Mobility Status of the User.")
nUser6HomeVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUser6HomeVlan.setDescription("\nHome VLAN of the User. If the user is on the home controller \n then this VLAN will be same as userDefaultVlan.")
nUser6DefaultVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUser6DefaultVlan.setDescription("\nDefault VLAN of the User based on the AP configuration.")
nUser6AssignedVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUser6AssignedVlan.setDescription("\nThis Vlan will be different from the Default VLAN if the user has \na derived VLAN Configuration.")
nUser6BWContractName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 18), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUser6BWContractName.setDescription("\nName of the Bandwidth Contract applied to this user.")
nUser6BWContractUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 19), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("user", 1), ("shared", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUser6BWContractUsage.setDescription("\nIndicates how the Bandwidth Contract is used.")
nUser6BWContractId = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUser6BWContractId.setDescription("\nBandwidth Contract Id Assigned to the User")
nUser6IsProxyArpEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 21), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUser6IsProxyArpEnabled.setDescription("\nThis object will indicate if the controller is proxy ARPing for the\nuser.")
nUser6CurrentVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUser6CurrentVlan.setDescription("\nThe VLAN to which the user is currently bound.")
nUser6IsWired = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 23), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUser6IsWired.setDescription("\nIndicates whether this is a wired or wireless user.")
nUser6ConnectedSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUser6ConnectedSlot.setDescription("\nThe slot to which the user is connected, if wired.")
nUser6ConnectedPort = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUser6ConnectedPort.setDescription("\nThe port to which the user is connected, if wired.")
nUser6PhyType = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 26), ArubaPhyType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUser6PhyType.setDescription("\nThe wireless PHY type to which the user is associated, or 'wired'.")
nUser6MobilityDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 27), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUser6MobilityDomainName.setDescription("\nThe name of mobility domain mobile user belongs to.")
nUser6UPBWContractName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 28), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUser6UPBWContractName.setDescription("\nName of the Upstream Bandwidth Contract applied to this user.")
nUser6UPBWContractUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 29), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("user", 1), ("shared", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUser6UPBWContractUsage.setDescription("\nIndicates how the Upstream Bandwidth Contract is used.")
nUser6UPBWContractId = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 30), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUser6UPBWContractId.setDescription("\nUpstream Bandwidth Contract Id Assigned to the User")
nUser6DNBWContractName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 31), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUser6DNBWContractName.setDescription("\nName of the Downstream Bandwidth Contract applied to this user.")
nUser6DNBWContractUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 32), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("user", 1), ("shared", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUser6DNBWContractUsage.setDescription("\nIndicates how the Downstream Bandwidth Contract is used.")
nUser6DNBWContractId = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 33), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUser6DNBWContractId.setDescription("\nDownstream Bandwidth Contract Id Assigned to the User")
nUser6HTMode = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 34), ArubaHTMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUser6HTMode.setDescription("\nThe HT mode of this user, if any.")
nUser6DeviceID = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 35), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUser6DeviceID.setDescription("\nDevice ID")
nUser6DeviceType = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 36), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUser6DeviceType.setDescription("\nDevice Type")
nUser6ConnectedModule = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 37), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUser6ConnectedModule.setDescription("\nThe module to which the user is connected, if wired.")
nUser6RxDataPkts64 = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 38), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUser6RxDataPkts64.setDescription("\nThis object specifies number of packets received by this IP\nfor which this user is connected to the controller.")
nUser6TxDataPkts64 = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 39), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUser6TxDataPkts64.setDescription("\nThis object specifies number of packets transmitted by this IP\nfor which this user is connected to the controller.")
nUser6RxDataOctets64 = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 40), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUser6RxDataOctets64.setDescription("\nThis object specifies number of octets received by this IP\nfor which this user is connected to the controller.")
nUser6TxDataOctets64 = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 41), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUser6TxDataOctets64.setDescription("\nThis object specifies number of octets transmitted by this IP\nfor which this user is connected to the controller.")
nUser6ForwardMode = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 42), ArubaUserForwardMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUser6ForwardMode.setDescription("\nForward mode.")
nUser6EncryptionMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 43), ArubaEncryptionType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUser6EncryptionMethod.setDescription("\nEncryption method.")
nVIAUser6DeviceID = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 2, 1, 44), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nVIAUser6DeviceID.setDescription("\nMAC address of the station from which the user connected to\nthe controller using VIA.")
wlsxUser6SessionTimeTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 3))
if mibBuilder.loadTexts: wlsxUser6SessionTimeTable.setDescription("\nThis table lists the user session time counts on an ESSID.\nssid. The session times  are separated into predefined time length \nbuckets, with sessions lasting longer than 240 minutes falling into \nthe 240min bucket. ")
wlsxUser6SessionTimeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 3, 1)).setIndexNames((0, "WLSX-WLAN-MIB", "wlanESSID"), (0, "WLSX-USER6-MIB", "wlsxUser6SessionTimeLength"))
if mibBuilder.loadTexts: wlsxUser6SessionTimeEntry.setDescription("\nUser session time data, divided into buckets of different\ntime length.         ")
wlsxUser6SessionTimeLength = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 3, 1, 1), Integer32()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: wlsxUser6SessionTimeLength.setDescription("\nPre-defined user session time length.")
wlsxUser6SessionTimeCount = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 14, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxUser6SessionTimeCount.setDescription("\nNumber of users that are connected to the essid whose sessions expired in this time interval.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("WLSX-USER6-MIB", PYSNMP_MODULE_ID=wlsxUser6MIB)

# Objects
mibBuilder.exportSymbols("WLSX-USER6-MIB", wlsxUser6InfoGroup=wlsxUser6InfoGroup, wlsxSwitchUser6Table=wlsxSwitchUser6Table, wlsxSwitchUser6Entry=wlsxSwitchUser6Entry, user6IpAddress=user6IpAddress, user6PhyAddress=user6PhyAddress, user6Name=user6Name, user6Role=user6Role, user6UpTime=user6UpTime, user6AuthenticationMethod=user6AuthenticationMethod, user6Location=user6Location, user6ServerName=user6ServerName, user6ConnectedVlan=user6ConnectedVlan, user6ConnectedSlot=user6ConnectedSlot, user6ConnectedPort=user6ConnectedPort, user6BWContractName=user6BWContractName, user6BWContractUsage=user6BWContractUsage, user6ConnectedModule=user6ConnectedModule, wlsxUser6MIB=wlsxUser6MIB, wlsxUser6AllInfoGroup=wlsxUser6AllInfoGroup, wlsxTotalNumOfUsers6=wlsxTotalNumOfUsers6, wlsxUser6Table=wlsxUser6Table, wlsxUser6Entry=wlsxUser6Entry, nUser6PhyAddress=nUser6PhyAddress, nUser6IpAddress=nUser6IpAddress, nUser6Name=nUser6Name, nUser6Role=nUser6Role, nUser6UpTime=nUser6UpTime, nUser6AuthenticationMethod=nUser6AuthenticationMethod, nUser6SubAuthenticationMethod=nUser6SubAuthenticationMethod, nUser6AuthServerName=nUser6AuthServerName, nUser6ExtVPNAddress=nUser6ExtVPNAddress, nUser6ApLocation=nUser6ApLocation, nUser6ApBSSID=nUser6ApBSSID, nUser6IsOnHomeAgent=nUser6IsOnHomeAgent, nUser6HomeAgentIpAddress=nUser6HomeAgentIpAddress, nUser6MobilityStatus=nUser6MobilityStatus, nUser6HomeVlan=nUser6HomeVlan, nUser6DefaultVlan=nUser6DefaultVlan, nUser6AssignedVlan=nUser6AssignedVlan, nUser6BWContractName=nUser6BWContractName, nUser6BWContractUsage=nUser6BWContractUsage, nUser6BWContractId=nUser6BWContractId, nUser6IsProxyArpEnabled=nUser6IsProxyArpEnabled, nUser6CurrentVlan=nUser6CurrentVlan, nUser6IsWired=nUser6IsWired, nUser6ConnectedSlot=nUser6ConnectedSlot, nUser6ConnectedPort=nUser6ConnectedPort, nUser6PhyType=nUser6PhyType, nUser6MobilityDomainName=nUser6MobilityDomainName, nUser6UPBWContractName=nUser6UPBWContractName, nUser6UPBWContractUsage=nUser6UPBWContractUsage, nUser6UPBWContractId=nUser6UPBWContractId, nUser6DNBWContractName=nUser6DNBWContractName, nUser6DNBWContractUsage=nUser6DNBWContractUsage, nUser6DNBWContractId=nUser6DNBWContractId, nUser6HTMode=nUser6HTMode, nUser6DeviceID=nUser6DeviceID, nUser6DeviceType=nUser6DeviceType, nUser6ConnectedModule=nUser6ConnectedModule, nUser6RxDataPkts64=nUser6RxDataPkts64, nUser6TxDataPkts64=nUser6TxDataPkts64, nUser6RxDataOctets64=nUser6RxDataOctets64, nUser6TxDataOctets64=nUser6TxDataOctets64, nUser6ForwardMode=nUser6ForwardMode, nUser6EncryptionMethod=nUser6EncryptionMethod, nVIAUser6DeviceID=nVIAUser6DeviceID, wlsxUser6SessionTimeTable=wlsxUser6SessionTimeTable, wlsxUser6SessionTimeEntry=wlsxUser6SessionTimeEntry, wlsxUser6SessionTimeLength=wlsxUser6SessionTimeLength, wlsxUser6SessionTimeCount=wlsxUser6SessionTimeCount)

