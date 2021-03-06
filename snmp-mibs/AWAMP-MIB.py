# PySNMP SMI module. Autogenerated from smidump -f python AWAMP-MIB
# by libsmi2pysnmp-0.1.3 at Tue Jun  3 12:38:40 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Integer32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, enterprises, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "enterprises")
( DisplayString, MacAddress, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TruthValue")

# Objects

airwave = MibIdentifier((1, 3, 6, 1, 4, 1, 12028))
awamp = ModuleIdentity((1, 3, 6, 1, 4, 1, 12028, 4)).setRevisions(("2011-12-20 00:00","2011-06-21 00:00","2008-02-28 00:00","2003-04-17 00:01","2003-04-17 00:00",))
if mibBuilder.loadTexts: awamp.setOrganization("Aruba Networks, Inc.")
if mibBuilder.loadTexts: awamp.setContactInfo("Primary Author: Paul Gray\n\npostal:    Aruba Networks, Inc.\n           1344 Crossman Ave\n           Sunnyvale, CA 94402\nphone:     +1 408-227-4500\nemail:     paul@arubanetworks.com\n  web:     http://www.arubanetworks.com/")
if mibBuilder.loadTexts: awamp.setDescription("The MIB module for AirWave entities .\niso(1).org(3).dod(6).internet(1).private(4).\nenterprises(1).airwave(12028).awamp(4)")
awampConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12028, 4, 2))
awampCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 12028, 4, 2, 1))
awampGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 12028, 4, 2, 2))
awampSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 12028, 4, 10))
awamp802dot11 = MibIdentifier((1, 3, 6, 1, 4, 1, 12028, 4, 11))
awampEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 12028, 4, 15))
awampEventPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0))
awampEventObject = MibIdentifier((1, 3, 6, 1, 4, 1, 12028, 4, 15, 1))
awampEventID = MibScalar((1, 3, 6, 1, 4, 1, 12028, 4, 15, 1, 101), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: awampEventID.setDescription("Random number AMP assigns to the event.")
awampEventSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 12028, 4, 15, 1, 102), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: awampEventSeverityCode.setDescription("Level 1-6")
awampEventDescription = MibScalar((1, 3, 6, 1, 4, 1, 12028, 4, 15, 1, 103), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: awampEventDescription.setDescription("Concatenated String produced from AMP.")
awampEventAPIPOld = MibScalar((1, 3, 6, 1, 4, 1, 12028, 4, 15, 1, 104), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: awampEventAPIPOld.setDescription("Old IP of the AP when AMP changes and\nsends trap to HPOV.")
awampEventAPMngURL = MibScalar((1, 3, 6, 1, 4, 1, 12028, 4, 15, 1, 105), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: awampEventAPMngURL.setDescription("URL to manage AP on AMP from HPOV.")
awampEventAPMonURL = MibScalar((1, 3, 6, 1, 4, 1, 12028, 4, 15, 1, 106), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: awampEventAPMonURL.setDescription("URL to monitor AP on AMP from HPOV.")
awampEventGroupMngURL = MibScalar((1, 3, 6, 1, 4, 1, 12028, 4, 15, 1, 107), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: awampEventGroupMngURL.setDescription("URL to manage Group on AMP from HPOV.")
awampEventGroupMonURL = MibScalar((1, 3, 6, 1, 4, 1, 12028, 4, 15, 1, 108), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: awampEventGroupMonURL.setDescription("URL to monitor Group on AMP from HPOV.")
awampEventAPICON = MibScalar((1, 3, 6, 1, 4, 1, 12028, 4, 15, 1, 109), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: awampEventAPICON.setDescription("Name of ICON to display on HPOV screen")
awampEventRogueSSID = MibScalar((1, 3, 6, 1, 4, 1, 12028, 4, 15, 1, 110), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: awampEventRogueSSID.setDescription("SSID of detected Rogue AP.")
awampEventRogueLANManufacturer = MibScalar((1, 3, 6, 1, 4, 1, 12028, 4, 15, 1, 111), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: awampEventRogueLANManufacturer.setDescription("Manufacturer of LAN of detected Rogue AP.")
awampEventRogueRadioManufacturer = MibScalar((1, 3, 6, 1, 4, 1, 12028, 4, 15, 1, 112), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: awampEventRogueRadioManufacturer.setDescription("Manufacturer of radio detected Rogue AP.")
awampEventRogueIsWired = MibScalar((1, 3, 6, 1, 4, 1, 12028, 4, 15, 1, 113), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: awampEventRogueIsWired.setDescription("Detected Rogue AP was discovered on the wired network.")
awampEventRogueIsWireless = MibScalar((1, 3, 6, 1, 4, 1, 12028, 4, 15, 1, 114), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: awampEventRogueIsWireless.setDescription("Detected Rogue AP was discovered on the wireless network.")
awampEventRogueClassifyingRule = MibScalar((1, 3, 6, 1, 4, 1, 12028, 4, 15, 1, 115), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: awampEventRogueClassifyingRule.setDescription("Rule used to classify detected rogue AP.")
awampEventRogueDiscoveringAgent = MibScalar((1, 3, 6, 1, 4, 1, 12028, 4, 15, 1, 116), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: awampEventRogueDiscoveringAgent.setDescription("The discovering agent that last detected the rogue AP.")
awampEventRogueDiscoveringAgentFolder = MibScalar((1, 3, 6, 1, 4, 1, 12028, 4, 15, 1, 117), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: awampEventRogueDiscoveringAgentFolder.setDescription("The folder name of the discovering agent that last detected the rogue AP.")
awampEventRogueClientMac = MibScalar((1, 3, 6, 1, 4, 1, 12028, 4, 15, 1, 118), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: awampEventRogueClientMac.setDescription("MAC Address of client connected to rogue ap.")
awampEventRogueName = MibScalar((1, 3, 6, 1, 4, 1, 12028, 4, 15, 1, 119), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: awampEventRogueName.setDescription("SSID to which the client is connected on rogue ap.")
awampApName = MibScalar((1, 3, 6, 1, 4, 1, 12028, 4, 101), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: awampApName.setDescription("The AP Name")
awampGroupName = MibScalar((1, 3, 6, 1, 4, 1, 12028, 4, 102), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: awampGroupName.setDescription("The Group Name")
awampAPEthMAC = MibScalar((1, 3, 6, 1, 4, 1, 12028, 4, 103), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: awampAPEthMAC.setDescription("IEEE Unique Identifier")
awampAPIP = MibScalar((1, 3, 6, 1, 4, 1, 12028, 4, 104), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: awampAPIP.setDescription("IP Address of the AP (Eth0)")
awampAPMFG = MibScalar((1, 3, 6, 1, 4, 1, 12028, 4, 105), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: awampAPMFG.setDescription("AP MFG")
awampAPModel = MibScalar((1, 3, 6, 1, 4, 1, 12028, 4, 106), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: awampAPModel.setDescription("AP Model")
awampAPFirmware = MibScalar((1, 3, 6, 1, 4, 1, 12028, 4, 107), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: awampAPFirmware.setDescription("AP Firmware")
awampROCommString = MibScalar((1, 3, 6, 1, 4, 1, 12028, 4, 108), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: awampROCommString.setDescription("Read Only Community String (not currently used)")
awampHPOVHostName = MibScalar((1, 3, 6, 1, 4, 1, 12028, 4, 109), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: awampHPOVHostName.setDescription("Hostname of the AP")
awampHPOVSYSID = MibScalar((1, 3, 6, 1, 4, 1, 12028, 4, 110), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: awampHPOVSYSID.setDescription("Hp OpenView Object Id")
awampHPOVMAC1 = MibScalar((1, 3, 6, 1, 4, 1, 12028, 4, 111), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: awampHPOVMAC1.setDescription("First Radio MAC on AP")
awampHPOVIP1 = MibScalar((1, 3, 6, 1, 4, 1, 12028, 4, 112), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: awampHPOVIP1.setDescription("First Radio IP AP")
awampHPOVMAC2 = MibScalar((1, 3, 6, 1, 4, 1, 12028, 4, 113), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: awampHPOVMAC2.setDescription("Second Radio MAC on AP")
awampHPOVIP2 = MibScalar((1, 3, 6, 1, 4, 1, 12028, 4, 114), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: awampHPOVIP2.setDescription("Second Radio IP AP")
awampHPOVsysName = MibScalar((1, 3, 6, 1, 4, 1, 12028, 4, 115), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: awampHPOVsysName.setDescription("Hostname of the AP")
awampHPOVsysDescr = MibScalar((1, 3, 6, 1, 4, 1, 12028, 4, 116), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: awampHPOVsysDescr.setDescription("Hostname of the AP")

# Augmentions

# Notifications

tooManyDevAssocAMP = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 1)).setObjects(*(("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: tooManyDevAssocAMP.setDescription("This trap is sent when too many devices are\nsimultaneously associated with AMP for a period of time.")
tooManyDevAssocGroup = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 2)).setObjects(*(("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: tooManyDevAssocGroup.setDescription("This trap is sent when too many devices are \nsimultaneously associated with a Group for a period of time.")
tooManyDevAssocAp = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 3)).setObjects(*(("AWAMP-MIB", "awampAPIP"), ("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: tooManyDevAssocAp.setDescription("This trap is sent when too many devices are associated \nsimultaneously associated with an AP for a period of time. ")
toomuchBWAMP = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 4)).setObjects(*(("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: toomuchBWAMP.setDescription("This trap is sent when there is too much BW being \nused on the WLAN for a period of time.")
toomuchBWGroup = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 5)).setObjects(*(("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: toomuchBWGroup.setDescription("This trap is sent when there is too much BW being \nused by a Group for a period of time.")
toomuchBWAP = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 6)).setObjects(*(("AWAMP-MIB", "awampAPIP"), ("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: toomuchBWAP.setDescription("This trap is sent when there is too much BW being \nused on an AP for a period of time.")
toomuchBWClient = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 7)).setObjects(*(("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: toomuchBWClient.setDescription("This trap is sent when there is too much BW being \nused by a Client for a period of time.")
toomanyRoamsClient = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 8)).setObjects(*(("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: toomanyRoamsClient.setDescription("This trap is sent when Client roams too frequently   \nfor a period of time.")
poorSignalAP = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 9)).setObjects(*(("AWAMP-MIB", "awampAPIP"), ("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: poorSignalAP.setDescription("This trap is sent when an AP has poor Signal\nquality for a period of time.")
nonAMPAPChange = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 10)).setObjects(*(("AWAMP-MIB", "awampAPIP"), ("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: nonAMPAPChange.setDescription("This trap is sent when an AP Changes configuration\nwithout the AMP's knowledge")
unauthenticatedClient = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 11)).setObjects(*(("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: unauthenticatedClient.setDescription("This trap is sent when Client is associated with\nWLAN for a period of time without authenticating.")
rogueAPDetected = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 12)).setObjects(*(("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: rogueAPDetected.setDescription("This trap is sent when the AMP classifies a\nRogue AP.")
downAP = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 13)).setObjects(*(("AWAMP-MIB", "awampAPIP"), ("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: downAP.setDescription("This trap is sent when the AP is down\n(for instance, a missed SNMP Ping or SNMP Get).")
discoveredAP = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 14)).setObjects(*(("AWAMP-MIB", "awampAPIP"), ("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: discoveredAP.setDescription("This trap is sent when AP is discovered by AMP.\nNote that this only applies to AP discovery,\nnot authorization. (A Config trap is sent when\nthe AP is authorized.")
upAP = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 15)).setObjects(*(("AWAMP-MIB", "awampAPIP"), ("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: upAP.setDescription("This trap is sent when AP is detected as UP after being\nmarked DOWN by the AMP.")
downRadio = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 16)).setObjects(*(("AWAMP-MIB", "awampAPIP"), ("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: downRadio.setDescription("This trap is sent when the radio of an AP is not operating.")
clientAssociate = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 17)).setObjects(*(("AWAMP-MIB", "awampAPIP"), ("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: clientAssociate.setDescription("This trap is sent when a watched client mac address\nassociates to an AP.")
authIssueClient = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 18)).setObjects(*(("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: authIssueClient.setDescription("This trap is sent when a client experiences too many \nauthentication failures.")
authIssueAP = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 19)).setObjects(*(("AWAMP-MIB", "awampAPIP"), ("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: authIssueAP.setDescription("This trap is sent when an AP experiences too many\nauthentication failures.")
authIssueAMP = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 20)).setObjects(*(("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: authIssueAMP.setDescription("This trap is sent when AMP detects too many\nauthentication failures.")
idsEventAP = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 21)).setObjects(*(("AWAMP-MIB", "awampAPIP"), ("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: idsEventAP.setDescription("This trap is sent when AMP receives too many IDS\nevents from an AP.")
rfidTagNotHeard = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 22)).setObjects(*(("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: rfidTagNotHeard.setDescription("This trap is sent when an RFID tag is not heard for\na certain period of time.")
dot11Counters = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 23)).setObjects(*(("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: dot11Counters.setDescription("This trap is sent when a Dot11 counter trigger fires.")
qosCounters = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 24)).setObjects(*(("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: qosCounters.setDescription("This trap is sent when a QOS counter trigger fires.")
deviceResources = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 25)).setObjects(*(("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: deviceResources.setDescription("This trap is sent when a Device Resources trigger fires.")
diskUsage = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 26)).setObjects(*(("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: diskUsage.setDescription("This trap is sent when a Disk Usage trigger fires.")
managedAmpDown = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 27)).setObjects(*(("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: managedAmpDown.setDescription("This trap is sent when a Managed AMP Down trigger fires.")
watchedAmpDown = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 28)).setObjects(*(("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: watchedAmpDown.setDescription("This trap is sent when a Watched AMP Down trigger fires.")
interfaceBandwidth = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 29)).setObjects(*(("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: interfaceBandwidth.setDescription("This trap is sent when an Interface Bandwidth trigger fires.")
radioUtilization = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 30)).setObjects(*(("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: radioUtilization.setDescription("This trap is sent when a Radio Utilization trigger fires.")
deviceEvent = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 31)).setObjects(*(("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: deviceEvent.setDescription("This trap is sent when a Device Event trigger fires.")
rogueAPDetectedDetail = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 32)).setObjects(*(("AWAMP-MIB", "awampEventRogueIsWireless"), ("AWAMP-MIB", "awampEventRogueDiscoveringAgentFolder"), ("AWAMP-MIB", "awampEventRogueDiscoveringAgent"), ("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventRogueRadioManufacturer"), ("AWAMP-MIB", "awampEventRogueIsWired"), ("AWAMP-MIB", "awampEventRogueSSID"), ("AWAMP-MIB", "awampEventDescription"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventRogueClassifyingRule"), ) )
if mibBuilder.loadTexts: rogueAPDetectedDetail.setDescription("This trap is sent when the AMP classifies a\nRogue AP. It includes more details: SSID, Manufacturer,\nWired (boolean), Wireless (boolean), Classifying Rule Name,\nLast Discovering Agent, and AP Folder Name.")
ipv4LinkLocalAddresses = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 33)).setObjects(*(("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: ipv4LinkLocalAddresses.setDescription("This trap is sent when a IPv4 Link-Local Addresses trigger fires.")
vpnUserConnect = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 34)).setObjects(*(("AWAMP-MIB", "awampAPIP"), ("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: vpnUserConnect.setDescription("This trap is sent when a new VPN user \nconnects to a controller.")
clientOnRogueAP = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 35)).setObjects(*(("AWAMP-MIB", "awampAPIP"), ("AWAMP-MIB", "awampEventRogueName"), ("AWAMP-MIB", "awampEventDescription"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventRogueClientMac"), ("AWAMP-MIB", "awampEventRogueSSID"), ) )
if mibBuilder.loadTexts: clientOnRogueAP.setDescription("This trap is sent when a new client is discovered\non Rogue AP. It includes more details: Client MAC,\nRogue SSID and Rogue Device Name.")
vpnUserAssociate = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 36)).setObjects(*(("AWAMP-MIB", "awampAPIP"), ("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: vpnUserAssociate.setDescription("This trap is sent when a watched VPN username \nassociates to a controller.")
toomuchBWVPNUser = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 37)).setObjects(*(("AWAMP-MIB", "awampAPIP"), ("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: toomuchBWVPNUser.setDescription("This trap is sent when a new VPN user\nconnects to a controller.")
toomuchGoodputClient = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 38)).setObjects(*(("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: toomuchGoodputClient.setDescription("This trap is sent when there is too much Goodput being\nused by a Client for a period of time.")
speedClient = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 39)).setObjects(*(("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: speedClient.setDescription("This trap is sent when speed of a Client is\nbelow (or above) a threshold for a period of time.")
noisefloorRadio = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 40)).setObjects(*(("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: noisefloorRadio.setDescription("This trap is sent when noise floor of AP is\nbelow (or above) a threshold for a period of time.")
genericTrap = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 50)).setObjects(*(("AWAMP-MIB", "awampAPIP"), ("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: genericTrap.setDescription("This trap will catch things not defined.")
internalAMLUnknown = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 51)).setObjects(*(("AWAMP-MIB", "awampAPIP"), ("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: internalAMLUnknown.setDescription("This is an internal trap designed for AML\nrunning on the NNM.  It allows the AML to \ndynamically accept severity codes from the AMP.\nBecause HP OpenView statically defines these in\ntrapd.conf per trap, we are creating an internal\nfor each severity level to work around issue.\nRepresents Blue and level 1")
internalAMLNormal = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 52)).setObjects(*(("AWAMP-MIB", "awampAPIP"), ("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: internalAMLNormal.setDescription("This is an internal trap designed for AML\nrunning on the NNM.  It allows the AML to \ndynamically accept severity codes from the AMP.\nBecause HP OpenView statically defines these in\ntrapd.conf per trap, we are creating an internal\nfor each severity level to work around issue.\nRepresents Green and level 2")
internalAMLMinor = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 53)).setObjects(*(("AWAMP-MIB", "awampAPIP"), ("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: internalAMLMinor.setDescription("This is an internal trap designed for AML\nrunning on the NNM.  It allows the AML to \ndynamically accept severity codes from the AMP.\nBecause HP OpenView statically defines these in\ntrapd.conf per trap, we are creating an internal\nfor each severity level to work around issue.\nRepresents yellow and level 3")
internalAMLCritcal = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 54)).setObjects(*(("AWAMP-MIB", "awampAPIP"), ("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: internalAMLCritcal.setDescription("This is an internal trap designed for AML\nrunning on the NNM.  It allows the AML to \ndynamically accept severity codes from the AMP.\nBecause HP OpenView statically defines these in\ntrapd.conf per trap, we are creating an internal\nfor each severity level to work around issue.\nRepresents Red and level 4")
internalAMLWarning = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 56)).setObjects(*(("AWAMP-MIB", "awampAPIP"), ("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: internalAMLWarning.setDescription("This is an internal trap designed for AML\nrunning on the NNM.  It allows the AML to \ndynamically accept severity codes from the AMP.\nBecause HP OpenView statically defines these in\ntrapd.conf per trap, we are creating an internal\nfor each severity level to work around issue.\nRepresents Cyan and level 6")
internalAMLMajor = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 57)).setObjects(*(("AWAMP-MIB", "awampAPIP"), ("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: internalAMLMajor.setDescription("This is an internal trap designed for AML\nrunning on the NNM.  It allows the AML to \ndynamically accept severity codes from the AMP.\nBecause HP OpenView statically defines these in\ntrapd.conf per trap, we are creating an internal\nfor each severity level to work around issue.\nRepresents Orange and level 7")
uplinkDevice = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 58)).setObjects(*(("AWAMP-MIB", "awampAPIP"), ("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventDescription"), ) )
if mibBuilder.loadTexts: uplinkDevice.setDescription("This trap is sent when the device uplink status is changed.")
configAlert = NotificationType((1, 3, 6, 1, 4, 1, 12028, 4, 15, 0, 200)).setObjects(*(("AWAMP-MIB", "awampEventAPIPOld"), ("AWAMP-MIB", "awampAPIP"), ("AWAMP-MIB", "awampEventGroupMngURL"), ("AWAMP-MIB", "awampEventAPMonURL"), ("AWAMP-MIB", "awampAPModel"), ("AWAMP-MIB", "awampEventGroupMonURL"), ("AWAMP-MIB", "awampGroupName"), ("AWAMP-MIB", "awampAPEthMAC"), ("AWAMP-MIB", "awampEventAPICON"), ("AWAMP-MIB", "awampEventAPMngURL"), ("AWAMP-MIB", "awampAPFirmware"), ("AWAMP-MIB", "awampApName"), ("AWAMP-MIB", "awampAPMFG"), ) )
if mibBuilder.loadTexts: configAlert.setDescription("This trap is sent every time a new device is discovered\nand authenticated on the AMP.  Also sent upon change to\n	IP, Name, Firmware, Group Association.")

# Groups

awampInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12028, 4, 2, 2, 1)).setObjects(*(("AWAMP-MIB", "awampHPOVIP2"), ("AWAMP-MIB", "awampAPIP"), ("AWAMP-MIB", "awampAPMFG"), ("AWAMP-MIB", "awampHPOVsysDescr"), ("AWAMP-MIB", "awampHPOVIP1"), ("AWAMP-MIB", "awampAPModel"), ("AWAMP-MIB", "awampHPOVMAC2"), ("AWAMP-MIB", "awampHPOVsysName"), ("AWAMP-MIB", "awampApName"), ("AWAMP-MIB", "awampGroupName"), ("AWAMP-MIB", "awampAPEthMAC"), ("AWAMP-MIB", "awampAPFirmware"), ("AWAMP-MIB", "awampHPOVSYSID"), ("AWAMP-MIB", "awampHPOVMAC1"), ("AWAMP-MIB", "awampHPOVHostName"), ("AWAMP-MIB", "awampROCommString"), ) )
if mibBuilder.loadTexts: awampInfoGroup.setDescription("The group of objects providing AMP information.")
awampEventGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12028, 4, 2, 2, 2)).setObjects(*(("AWAMP-MIB", "awampEventAPIPOld"), ("AWAMP-MIB", "awampEventRogueDiscoveringAgent"), ("AWAMP-MIB", "awampEventRogueDiscoveringAgentFolder"), ("AWAMP-MIB", "awampEventRogueRadioManufacturer"), ("AWAMP-MIB", "awampEventRogueLANManufacturer"), ("AWAMP-MIB", "awampEventGroupMngURL"), ("AWAMP-MIB", "awampEventAPMonURL"), ("AWAMP-MIB", "awampEventDescription"), ("AWAMP-MIB", "awampEventSeverityCode"), ("AWAMP-MIB", "awampEventGroupMonURL"), ("AWAMP-MIB", "awampEventAPMngURL"), ("AWAMP-MIB", "awampEventRogueIsWireless"), ("AWAMP-MIB", "awampEventRogueName"), ("AWAMP-MIB", "awampEventID"), ("AWAMP-MIB", "awampEventRogueClientMac"), ("AWAMP-MIB", "awampEventRogueIsWired"), ("AWAMP-MIB", "awampEventAPICON"), ("AWAMP-MIB", "awampEventRogueSSID"), ("AWAMP-MIB", "awampEventRogueClassifyingRule"), ) )
if mibBuilder.loadTexts: awampEventGroup.setDescription("The group of objects providing AMP events.")
awampNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 12028, 4, 2, 2, 3)).setObjects(*(("AWAMP-MIB", "toomuchBWGroup"), ("AWAMP-MIB", "poorSignalAP"), ("AWAMP-MIB", "nonAMPAPChange"), ("AWAMP-MIB", "toomuchBWClient"), ("AWAMP-MIB", "managedAmpDown"), ("AWAMP-MIB", "noisefloorRadio"), ("AWAMP-MIB", "clientAssociate"), ("AWAMP-MIB", "toomuchBWAMP"), ("AWAMP-MIB", "discoveredAP"), ("AWAMP-MIB", "internalAMLMajor"), ("AWAMP-MIB", "downRadio"), ("AWAMP-MIB", "diskUsage"), ("AWAMP-MIB", "vpnUserAssociate"), ("AWAMP-MIB", "authIssueAMP"), ("AWAMP-MIB", "clientOnRogueAP"), ("AWAMP-MIB", "toomuchBWAP"), ("AWAMP-MIB", "toomuchBWVPNUser"), ("AWAMP-MIB", "toomuchGoodputClient"), ("AWAMP-MIB", "watchedAmpDown"), ("AWAMP-MIB", "internalAMLNormal"), ("AWAMP-MIB", "configAlert"), ("AWAMP-MIB", "uplinkDevice"), ("AWAMP-MIB", "unauthenticatedClient"), ("AWAMP-MIB", "authIssueAP"), ("AWAMP-MIB", "deviceEvent"), ("AWAMP-MIB", "radioUtilization"), ("AWAMP-MIB", "ipv4LinkLocalAddresses"), ("AWAMP-MIB", "tooManyDevAssocGroup"), ("AWAMP-MIB", "internalAMLMinor"), ("AWAMP-MIB", "rfidTagNotHeard"), ("AWAMP-MIB", "vpnUserConnect"), ("AWAMP-MIB", "internalAMLCritcal"), ("AWAMP-MIB", "genericTrap"), ("AWAMP-MIB", "dot11Counters"), ("AWAMP-MIB", "idsEventAP"), ("AWAMP-MIB", "upAP"), ("AWAMP-MIB", "authIssueClient"), ("AWAMP-MIB", "tooManyDevAssocAp"), ("AWAMP-MIB", "deviceResources"), ("AWAMP-MIB", "rogueAPDetected"), ("AWAMP-MIB", "rogueAPDetectedDetail"), ("AWAMP-MIB", "tooManyDevAssocAMP"), ("AWAMP-MIB", "qosCounters"), ("AWAMP-MIB", "downAP"), ("AWAMP-MIB", "interfaceBandwidth"), ("AWAMP-MIB", "toomanyRoamsClient"), ("AWAMP-MIB", "internalAMLWarning"), ("AWAMP-MIB", "internalAMLUnknown"), ("AWAMP-MIB", "speedClient"), ) )
if mibBuilder.loadTexts: awampNotificationGroup.setDescription("The group of objects providing AMP notifications.")

# Compliances

awampCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 12028, 4, 2, 1, 1)).setObjects(*(("AWAMP-MIB", "awampInfoGroup"), ("AWAMP-MIB", "awampEventGroup"), ("AWAMP-MIB", "awampNotificationGroup"), ) )
if mibBuilder.loadTexts: awampCompliance.setDescription("The compliance statement for the AirWave AMP.")

# Exports

# Module identity
mibBuilder.exportSymbols("AWAMP-MIB", PYSNMP_MODULE_ID=awamp)

# Objects
mibBuilder.exportSymbols("AWAMP-MIB", airwave=airwave, awamp=awamp, awampConformance=awampConformance, awampCompliances=awampCompliances, awampGroups=awampGroups, awampSystem=awampSystem, awamp802dot11=awamp802dot11, awampEvent=awampEvent, awampEventPrefix=awampEventPrefix, awampEventObject=awampEventObject, awampEventID=awampEventID, awampEventSeverityCode=awampEventSeverityCode, awampEventDescription=awampEventDescription, awampEventAPIPOld=awampEventAPIPOld, awampEventAPMngURL=awampEventAPMngURL, awampEventAPMonURL=awampEventAPMonURL, awampEventGroupMngURL=awampEventGroupMngURL, awampEventGroupMonURL=awampEventGroupMonURL, awampEventAPICON=awampEventAPICON, awampEventRogueSSID=awampEventRogueSSID, awampEventRogueLANManufacturer=awampEventRogueLANManufacturer, awampEventRogueRadioManufacturer=awampEventRogueRadioManufacturer, awampEventRogueIsWired=awampEventRogueIsWired, awampEventRogueIsWireless=awampEventRogueIsWireless, awampEventRogueClassifyingRule=awampEventRogueClassifyingRule, awampEventRogueDiscoveringAgent=awampEventRogueDiscoveringAgent, awampEventRogueDiscoveringAgentFolder=awampEventRogueDiscoveringAgentFolder, awampEventRogueClientMac=awampEventRogueClientMac, awampEventRogueName=awampEventRogueName, awampApName=awampApName, awampGroupName=awampGroupName, awampAPEthMAC=awampAPEthMAC, awampAPIP=awampAPIP, awampAPMFG=awampAPMFG, awampAPModel=awampAPModel, awampAPFirmware=awampAPFirmware, awampROCommString=awampROCommString, awampHPOVHostName=awampHPOVHostName, awampHPOVSYSID=awampHPOVSYSID, awampHPOVMAC1=awampHPOVMAC1, awampHPOVIP1=awampHPOVIP1, awampHPOVMAC2=awampHPOVMAC2, awampHPOVIP2=awampHPOVIP2, awampHPOVsysName=awampHPOVsysName, awampHPOVsysDescr=awampHPOVsysDescr)

# Notifications
mibBuilder.exportSymbols("AWAMP-MIB", tooManyDevAssocAMP=tooManyDevAssocAMP, tooManyDevAssocGroup=tooManyDevAssocGroup, tooManyDevAssocAp=tooManyDevAssocAp, toomuchBWAMP=toomuchBWAMP, toomuchBWGroup=toomuchBWGroup, toomuchBWAP=toomuchBWAP, toomuchBWClient=toomuchBWClient, toomanyRoamsClient=toomanyRoamsClient, poorSignalAP=poorSignalAP, nonAMPAPChange=nonAMPAPChange, unauthenticatedClient=unauthenticatedClient, rogueAPDetected=rogueAPDetected, downAP=downAP, discoveredAP=discoveredAP, upAP=upAP, downRadio=downRadio, clientAssociate=clientAssociate, authIssueClient=authIssueClient, authIssueAP=authIssueAP, authIssueAMP=authIssueAMP, idsEventAP=idsEventAP, rfidTagNotHeard=rfidTagNotHeard, dot11Counters=dot11Counters, qosCounters=qosCounters, deviceResources=deviceResources, diskUsage=diskUsage, managedAmpDown=managedAmpDown, watchedAmpDown=watchedAmpDown, interfaceBandwidth=interfaceBandwidth, radioUtilization=radioUtilization, deviceEvent=deviceEvent, rogueAPDetectedDetail=rogueAPDetectedDetail, ipv4LinkLocalAddresses=ipv4LinkLocalAddresses, vpnUserConnect=vpnUserConnect, clientOnRogueAP=clientOnRogueAP, vpnUserAssociate=vpnUserAssociate, toomuchBWVPNUser=toomuchBWVPNUser, toomuchGoodputClient=toomuchGoodputClient, speedClient=speedClient, noisefloorRadio=noisefloorRadio, genericTrap=genericTrap, internalAMLUnknown=internalAMLUnknown, internalAMLNormal=internalAMLNormal, internalAMLMinor=internalAMLMinor, internalAMLCritcal=internalAMLCritcal, internalAMLWarning=internalAMLWarning, internalAMLMajor=internalAMLMajor, uplinkDevice=uplinkDevice, configAlert=configAlert)

# Groups
mibBuilder.exportSymbols("AWAMP-MIB", awampInfoGroup=awampInfoGroup, awampEventGroup=awampEventGroup, awampNotificationGroup=awampNotificationGroup)

# Compliances
mibBuilder.exportSymbols("AWAMP-MIB", awampCompliance=awampCompliance)
