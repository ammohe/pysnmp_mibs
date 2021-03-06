# PySNMP SMI module. Autogenerated from smidump -f python WLSX-USER-MIB
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
( wlanESSID, ) = mibBuilder.importSymbols("WLSX-WLAN-MIB", "wlanESSID")

# Objects

wlsxUserMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4)).setRevisions(("1910-01-26 18:06",))
if mibBuilder.loadTexts: wlsxUserMIB.setOrganization("Aruba Wireless Networks")
if mibBuilder.loadTexts: wlsxUserMIB.setContactInfo("Postal:    1322 Crossman Avenue\nSunnyvale, CA 94089\nE-mail:     dl-support@arubanetworks.com\nPhone:      +1 408 227 4500")
if mibBuilder.loadTexts: wlsxUserMIB.setDescription("This MIB module defines MIB objects which provide\ninformation about the users in an Aruba controller.")
wlsxUserAllInfoGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1))
wlsxTotalNumOfUsers = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxTotalNumOfUsers.setDescription("\nTotal Number of the users.")
wlsxUserTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2))
if mibBuilder.loadTexts: wlsxUserTable.setDescription("\nThis Table lists all the users (both wired and wireless) currently\nconnected to the controller. Users are identified by their MAC \naddress and IP address.")
wlsxUserEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1)).setIndexNames((0, "WLSX-USER-MIB", "nUserPhyAddress"), (0, "WLSX-USER-MIB", "nUserIpAddress"))
if mibBuilder.loadTexts: wlsxUserEntry.setDescription("User Entry")
nUserPhyAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 1), MacAddress()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: nUserPhyAddress.setDescription("\nMAC address of the station from which the user connected to\nthe controller.")
nUserIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 2), IpAddress()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: nUserIpAddress.setDescription("\nIP Address of the user.")
nUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUserName.setDescription("\nName of the User.")
nUserRole = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUserRole.setDescription("\nThe Role configured for this user.")
nUserUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUserUpTime.setDescription("\nTime since the user connected to the controller.	")
nUserAuthenticationMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 6), ArubaAuthenticationMethods()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUserAuthenticationMethod.setDescription("\nAuthentication mechanism used by the user to connect to the \ncontroller.")
nUserSubAuthenticationMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 7), ArubaSubAuthenticationMethods()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUserSubAuthenticationMethod.setDescription("\nSub Authentication Method")
nUserAuthServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUserAuthServerName.setDescription("\nName of the authentication server used to authenticate \nthe user.")
nUserExtVPNAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 9), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUserExtVPNAddress.setDescription("\nExternal VPN IP Address, if this is a VPN user or 0.0.0.0 if not.")
nUserApLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUserApLocation.setDescription("\nLocation of the access point to \nwhich the user is associated.")
nUserApBSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 11), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUserApBSSID.setDescription("\nBSSID of the access point, which \nthe user used to connect to the controller.")
nUserIsOnHomeAgent = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 12), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUserIsOnHomeAgent.setDescription("\nThe Object will indicate if the controller is the home controller \n for the user or not.")
nUserHomeAgentIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 13), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUserHomeAgentIpAddress.setDescription("\nThe Home agent IP Address of the user. If this user is already on \nthe home controller, then this IP is the controller IP else it \nis the home controller IP address.")
nUserMobilityStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 14), Integer().subtype(subtypeSpec=SingleValueConstraint(3,1,2,5,4,)).subtype(namedValues=NamedValues(("visitor", 1), ("away", 2), ("associated", 3), ("wired", 4), ("wireless", 5), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUserMobilityStatus.setDescription("\nThe Mobility Status of the User.")
nUserHomeVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUserHomeVlan.setDescription("\nHome VLAN of the User. If the user is on the home controller \n then this VLAN will be same as userDefaultVlan.")
nUserDefaultVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUserDefaultVlan.setDescription("\nDefault VLAN of the User based on the AP configuration.")
nUserAssignedVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUserAssignedVlan.setDescription("\nThis Vlan will be different from the Default VLAN if the user has \na derived VLAN Configuration.")
nUserBWContractName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 18), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUserBWContractName.setDescription("\nName of the Bandwidth Contract applied to this user.")
nUserBWContractUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 19), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("user", 1), ("shared", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUserBWContractUsage.setDescription("\nIndicates how the Bandwidth Contract is used.")
nUserBWContractId = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUserBWContractId.setDescription("\nBandwidth Contract Id Assigned to the User")
nUserIsProxyArpEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 21), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUserIsProxyArpEnabled.setDescription("\nThis object will indicate if the controller is proxy ARPing for the\nuser.")
nUserCurrentVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUserCurrentVlan.setDescription("\nThe VLAN to which the user is currently bound.")
nUserIsWired = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 23), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUserIsWired.setDescription("\nIndicates whether this is a wired or wireless user.")
nUserConnectedSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUserConnectedSlot.setDescription("\nThe slot to which the user is connected, if wired.")
nUserConnectedPort = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUserConnectedPort.setDescription("\nThe port to which the user is connected, if wired.")
nUserPhyType = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 26), ArubaPhyType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUserPhyType.setDescription("\nThe wireless PHY type to which the user is associated, or 'wired'.")
nUserMobilityDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 27), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUserMobilityDomainName.setDescription("\nThe name of mobility domain mobile user belongs to.")
nUserUPBWContractName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 28), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUserUPBWContractName.setDescription("\nName of the Upstream Bandwidth Contract applied to this user.")
nUserUPBWContractUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 29), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("user", 1), ("shared", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUserUPBWContractUsage.setDescription("\nIndicates how the Upstream Bandwidth Contract is used.")
nUserUPBWContractId = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 30), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUserUPBWContractId.setDescription("\nUpstream Bandwidth Contract Id Assigned to the User")
nUserDNBWContractName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 31), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUserDNBWContractName.setDescription("\nName of the Downstream Bandwidth Contract applied to this user.")
nUserDNBWContractUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 32), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("user", 1), ("shared", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUserDNBWContractUsage.setDescription("\nIndicates how the Downstream Bandwidth Contract is used.")
nUserDNBWContractId = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 33), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUserDNBWContractId.setDescription("\nDownstream Bandwidth Contract Id Assigned to the User")
nUserHTMode = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 34), ArubaHTMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUserHTMode.setDescription("\nThe HT mode of this user, if any.")
nUserEncryptionMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 35), ArubaEncryptionType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUserEncryptionMethod.setDescription("\nEncryption method.")
nUserForwardMode = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 36), ArubaUserForwardMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUserForwardMode.setDescription("\nUser mode.")
nUserDeviceID = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 37), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUserDeviceID.setDescription("\nDevice ID")
nUserConnectedModule = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 38), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUserConnectedModule.setDescription("\nThe module to which the user is connected, if wired.")
nUserDeviceType = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 39), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUserDeviceType.setDescription("\nDevice type")
nUserRxDataPkts64 = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 40), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUserRxDataPkts64.setDescription("\nThis object specifies number of packets received by this IP\nfor which this user is connected to the controller.")
nUserTxDataPkts64 = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 41), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUserTxDataPkts64.setDescription("\nThis object specifies number of packets transmitted by this IP\nfor which this user is connected to the controller.")
nUserRxDataOctets64 = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 42), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUserRxDataOctets64.setDescription("\nThis object specifies number of octets received by this IP\nfor which this user is connected to the controller.")
nUserTxDataOctets64 = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 43), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nUserTxDataOctets64.setDescription("\nThis object specifies number of octets transmitted by this IP\nfor which this user is connected to the controller.")
nVIAUserDeviceID = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 2, 1, 44), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nVIAUserDeviceID.setDescription("\nMAC address of the station from which the user connected to\nthe controller using VIA.")
wlsxUserSessionTimeTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 3))
if mibBuilder.loadTexts: wlsxUserSessionTimeTable.setDescription("\nThis table lists the user session time counts on an ESSID.\nssid. The session times  are separated into predefined time length \nbuckets, with sessions lasting longer than 240 minutes falling into \nthe 240min bucket. ")
wlsxUserSessionTimeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 3, 1)).setIndexNames((0, "WLSX-WLAN-MIB", "wlanESSID"), (0, "WLSX-USER-MIB", "wlsxUserSessionTimeLength"))
if mibBuilder.loadTexts: wlsxUserSessionTimeEntry.setDescription("\nUser session time data, divided into buckets of different\ntime length.         ")
wlsxUserSessionTimeLength = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 3, 1, 1), Integer32()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: wlsxUserSessionTimeLength.setDescription("\nPre-defined user session time length.")
wlsxUserSessionTimeCount = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxUserSessionTimeCount.setDescription("\nNumber of users that are connected to the essid whose sessions expired in this time interval.")
wlsxUserStatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 4))
wlsxNumOfUsers8021x = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 4, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxNumOfUsers8021x.setDescription("\nNumber of 802.1x users.")
wlsxNumOfUsersVPN = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 4, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxNumOfUsersVPN.setDescription("\nNumber of VPN users.")
wlsxNumOfUsersCP = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 4, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxNumOfUsersCP.setDescription("\nNumber of Captive Portal  users.")
wlsxNumOfUsersMAC = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 4, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxNumOfUsersMAC.setDescription("\nNumber of MAC users.")
wlsxNumOfUsersStateful8021x = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 4, 1, 4, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxNumOfUsersStateful8021x.setDescription("\nNumber of stateful 802.1x users.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("WLSX-USER-MIB", PYSNMP_MODULE_ID=wlsxUserMIB)

# Objects
mibBuilder.exportSymbols("WLSX-USER-MIB", wlsxUserMIB=wlsxUserMIB, wlsxUserAllInfoGroup=wlsxUserAllInfoGroup, wlsxTotalNumOfUsers=wlsxTotalNumOfUsers, wlsxUserTable=wlsxUserTable, wlsxUserEntry=wlsxUserEntry, nUserPhyAddress=nUserPhyAddress, nUserIpAddress=nUserIpAddress, nUserName=nUserName, nUserRole=nUserRole, nUserUpTime=nUserUpTime, nUserAuthenticationMethod=nUserAuthenticationMethod, nUserSubAuthenticationMethod=nUserSubAuthenticationMethod, nUserAuthServerName=nUserAuthServerName, nUserExtVPNAddress=nUserExtVPNAddress, nUserApLocation=nUserApLocation, nUserApBSSID=nUserApBSSID, nUserIsOnHomeAgent=nUserIsOnHomeAgent, nUserHomeAgentIpAddress=nUserHomeAgentIpAddress, nUserMobilityStatus=nUserMobilityStatus, nUserHomeVlan=nUserHomeVlan, nUserDefaultVlan=nUserDefaultVlan, nUserAssignedVlan=nUserAssignedVlan, nUserBWContractName=nUserBWContractName, nUserBWContractUsage=nUserBWContractUsage, nUserBWContractId=nUserBWContractId, nUserIsProxyArpEnabled=nUserIsProxyArpEnabled, nUserCurrentVlan=nUserCurrentVlan, nUserIsWired=nUserIsWired, nUserConnectedSlot=nUserConnectedSlot, nUserConnectedPort=nUserConnectedPort, nUserPhyType=nUserPhyType, nUserMobilityDomainName=nUserMobilityDomainName, nUserUPBWContractName=nUserUPBWContractName, nUserUPBWContractUsage=nUserUPBWContractUsage, nUserUPBWContractId=nUserUPBWContractId, nUserDNBWContractName=nUserDNBWContractName, nUserDNBWContractUsage=nUserDNBWContractUsage, nUserDNBWContractId=nUserDNBWContractId, nUserHTMode=nUserHTMode, nUserEncryptionMethod=nUserEncryptionMethod, nUserForwardMode=nUserForwardMode, nUserDeviceID=nUserDeviceID, nUserConnectedModule=nUserConnectedModule, nUserDeviceType=nUserDeviceType, nUserRxDataPkts64=nUserRxDataPkts64, nUserTxDataPkts64=nUserTxDataPkts64, nUserRxDataOctets64=nUserRxDataOctets64, nUserTxDataOctets64=nUserTxDataOctets64, nVIAUserDeviceID=nVIAUserDeviceID, wlsxUserSessionTimeTable=wlsxUserSessionTimeTable, wlsxUserSessionTimeEntry=wlsxUserSessionTimeEntry, wlsxUserSessionTimeLength=wlsxUserSessionTimeLength, wlsxUserSessionTimeCount=wlsxUserSessionTimeCount, wlsxUserStatsGroup=wlsxUserStatsGroup, wlsxNumOfUsers8021x=wlsxNumOfUsers8021x, wlsxNumOfUsersVPN=wlsxNumOfUsersVPN, wlsxNumOfUsersCP=wlsxNumOfUsersCP, wlsxNumOfUsersMAC=wlsxNumOfUsersMAC, wlsxNumOfUsersStateful8021x=wlsxNumOfUsersStateful8021x)

