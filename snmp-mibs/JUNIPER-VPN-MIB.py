# PySNMP SMI module. Autogenerated from smidump -f python JUNIPER-VPN-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:57:57 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( InterfaceIndexOrZero, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
( InetAddress, InetAddressType, ) = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
( jnxMibs, ) = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( Bits, Counter32, Counter64, Gauge32, Integer32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "TimeTicks", "Unsigned32")
( RowStatus, StorageType, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "StorageType", "TextualConvention")

# Types

class JnxVpnIdentifier(OctetString):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,256)
    
class JnxVpnIdentifierType(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(2,0,5,3,4,7,8,9,11,1,6,10,)
    namedValues = NamedValues(("none", 0), ("other", 1), ("vcId", 10), ("localSwitch", 11), ("routeDistinguisher", 2), ("routeDistinguisher0", 3), ("routeDistinguisher1", 4), ("routeDistinguisher2", 5), ("routeTarget", 6), ("routeTarget0", 7), ("routeTarget1", 8), ("routeTarget2", 9), )
    
class JnxVpnLocalSwitchIdentifier(OctetString):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(1,256)
    
class JnxVpnMultiplexor(Unsigned32):
    pass

class JnxVpnName(OctetString):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(1,128)
    
class JnxVpnRouteDistinguisher(TextualConvention, OctetString):
    displayHint = "1x:1x:1x:1x:1x:1x:1x:1x"
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(8,8)
    fixedLength = 8
    
class JnxVpnRouteDistinguisher0(TextualConvention, OctetString):
    displayHint = "2x-2d:4d"
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(8,8)
    fixedLength = 8
    
class JnxVpnRouteDistinguisher1(TextualConvention, OctetString):
    displayHint = "2x-1d.1d.1d.1d:2d"
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(8,8)
    fixedLength = 8
    
class JnxVpnRouteDistinguisher2(TextualConvention, OctetString):
    displayHint = "2x-4d:2d"
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(8,8)
    fixedLength = 8
    
class JnxVpnRouteTarget(TextualConvention, OctetString):
    displayHint = "1x:1x:1x:1x:1x:1x:1x:1x"
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(8,8)
    fixedLength = 8
    
class JnxVpnRouteTarget0(TextualConvention, OctetString):
    displayHint = "2x-4d:2d"
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(8,8)
    fixedLength = 8
    
class JnxVpnRouteTarget1(TextualConvention, OctetString):
    displayHint = "2x-1d.1d.1d.1d:2d"
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(8,8)
    fixedLength = 8
    
class JnxVpnRouteTarget2(TextualConvention, OctetString):
    displayHint = "2x-2d:4d"
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(8,8)
    fixedLength = 8
    
class JnxVpnType(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(4,5,6,7,3,10,8,2,1,9,)
    namedValues = NamedValues(("other", 1), ("bgpAtmVpn", 10), ("bgpIpVpn", 2), ("bgpL2Vpn", 3), ("bgpVpls", 4), ("l2Circuit", 5), ("ldpVpls", 6), ("opticalVpn", 7), ("vpOxc", 8), ("ccc", 9), )
    
class JnxVpnVCIdentifier(TextualConvention, OctetString):
    displayHint = "1d.1d.1d.1d:4d"
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(8,8)
    fixedLength = 8
    

# Objects

jnxVpnMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 26)).setRevisions(("2010-10-15 00:00","2010-08-27 00:00","2002-04-21 21:28",))
if mibBuilder.loadTexts: jnxVpnMIB.setOrganization("IETF Provider Provisioned VPNs WG")
if mibBuilder.loadTexts: jnxVpnMIB.setContactInfo("        Kireeti Kompella\nPostal: Juniper Networks, Inc.\n        1194 Mathilda Ave\n        Sunnyvale, CA 94089\n   Tel: +1 408 745 2000\nE-mail: kireeti@juniper.net")
if mibBuilder.loadTexts: jnxVpnMIB.setDescription("Extended VPN MIB module to support VPN Identifier for locally switched\nL2 circuits.")
jnxVpnMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 26, 0))
jnxVpnMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1))
jnxVpnInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 1))
jnxVpnConfiguredVpns = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnConfiguredVpns.setDescription("Number of configured VPNs.")
jnxVpnActiveVpns = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnActiveVpns.setDescription("Number of active VPNs.")
jnxVpnNextIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnNextIfIndex.setDescription("Next free VPN interface index.")
jnxVpnNextPwIndex = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnNextPwIndex.setDescription("Next free Pseudo-Wire index.")
jnxVpnNextRTIndex = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnNextRTIndex.setDescription("Next free Route Target index.")
jnxVpnTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2))
if mibBuilder.loadTexts: jnxVpnTable.setDescription("Table of Configured VPNs.")
jnxVpnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1)).setIndexNames((0, "JUNIPER-VPN-MIB", "jnxVpnType"), (0, "JUNIPER-VPN-MIB", "jnxVpnName"))
if mibBuilder.loadTexts: jnxVpnEntry.setDescription("Entry containing information about a particular VPN.")
jnxVpnType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 1), JnxVpnType()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxVpnType.setDescription("Type of the VPN.")
jnxVpnName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 2), JnxVpnName()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxVpnName.setDescription("Name of the VPN.  This should ideally be unique in the\nService Provider's domain; at a minimum, it MUST be\nunique per Provider Edge router.")
jnxVpnRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 3), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnRowStatus.setDescription("This variable is used to create, modify, and/or delete a\nrow in this table.")
jnxVpnStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnStorageType.setDescription("This variable indicates the storage type for this object.")
jnxVpnDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnDescription.setDescription("String describing the VPN.")
jnxVpnIdentifierType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 6), JnxVpnIdentifierType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnIdentifierType.setDescription("Type of the following JnxVpnIdentifier.")
jnxVpnIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 7), JnxVpnIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnIdentifier.setDescription("In the case of BGP VPNs, this is the Route Distinguisher\nfor the VPN.  In the case of LDP VPNs, this is the VC ID\nfor the circuit.  A value of all zeros indicates that the\nneither a Route Distinguisher nor a VC ID is configured\nfor the VPN.")
jnxVpnConfiguredSites = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnConfiguredSites.setDescription("The number of sites configured in the VPN.  Must be set\nto zero if not applicable.")
jnxVpnActiveSites = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnActiveSites.setDescription("The number of active sites (i.e., sites whose state is\nactive) in the VPN.")
jnxVpnLocalAddresses = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnLocalAddresses.setDescription("The number of addresses learned from the CE device.")
jnxVpnTotalAddresses = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnTotalAddresses.setDescription("The total number of addresses in the VPN RIB.")
jnxVpnAge = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 12), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnAge.setDescription("The age (i.e., time from creation till now) of this\nVPN in hundredths of a second.")
jnxVpnIfTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3))
if mibBuilder.loadTexts: jnxVpnIfTable.setDescription("Table of VPN Interfaces.")
jnxVpnIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1)).setIndexNames((0, "JUNIPER-VPN-MIB", "jnxVpnIfVpnType"), (0, "JUNIPER-VPN-MIB", "jnxVpnIfVpnName"), (0, "JUNIPER-VPN-MIB", "jnxVpnIfIndex"))
if mibBuilder.loadTexts: jnxVpnIfEntry.setDescription("Entry containing information about a particular VPN\ninterface.")
jnxVpnIfVpnType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1, 1), JnxVpnType()).setMaxAccess("notifyonly")
if mibBuilder.loadTexts: jnxVpnIfVpnType.setDescription("Type of the VPN to which this interface belongs.")
jnxVpnIfVpnName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1, 2), JnxVpnName()).setMaxAccess("notifyonly")
if mibBuilder.loadTexts: jnxVpnIfVpnName.setDescription("Name of the VPN to which this interface belongs.")
jnxVpnIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1, 3), Unsigned32()).setMaxAccess("notifyonly")
if mibBuilder.loadTexts: jnxVpnIfIndex.setDescription("The index of this interface in the VPN.  Each interface\nin the VPN is given a unique index.  The RowStatus says\nwhether a given interface (i.e., a row in this table)\nis valid or not. Note: this index MUST NOT be zero.")
jnxVpnIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1, 4), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnIfRowStatus.setDescription("This variable is used to create, modify, and/or delete a\nrow in this table.")
jnxVpnIfStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1, 5), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnIfStorageType.setDescription("This variable indicates the storage type for this object.")
jnxVpnIfAssociatedPw = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnIfAssociatedPw.setDescription("Index of associated Pseudo-wire, if any, in which case\nthe index MUST be non-zero.  If none, then this index\nMUST be zero.")
jnxVpnIfProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1, 7), Integer().subtype(subtypeSpec=SingleValueConstraint(26,21,7,20,15,5,2,130,0,13,6,17,24,8,10,25,18,11,129,3,9,12,23,1,4,22,)).subtype(namedValues=NamedValues(("other", 0), ("frameRelay", 1), ("atmVpc", 10), ("vpls", 11), ("ipInterworking", 12), ("atmTrunkNNI", 129), ("snapInterworking", 13), ("atmTrunkUNI", 130), ("frameRelayPort", 15), ("satope1", 17), ("satopt1", 18), ("atmAal5", 2), ("static", 20), ("rip", 21), ("ospf", 22), ("bgp", 23), ("satope3", 24), ("satopt3", 25), ("cesop", 26), ("atmCell", 3), ("ethernetVlan", 4), ("ethernet", 5), ("ciscoHdlc", 6), ("ppp", 7), ("cem", 8), ("atmVcc", 9), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnIfProtocol.setDescription("Protocol running over this VPN interface.  The values up to\n10 are taken from draft-martini-l2circuit-trans-mpls-08.txt;\nthe value for vpls is taken from\ndraft-lasserre-vkompella-ppvpn-vpls-01.txt.  The values\nfrom 20-23 are used when the VPN is a Layer 3 VPN.")
jnxVpnIfInBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnIfInBandwidth.setDescription("Maximum bandwidth that the CE connected over this VPN i/f\ncan send to the PE, in Kilo (i.e., 1000) Bytes per second.\nA value of zero means there is no configured maximum.")
jnxVpnIfOutBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnIfOutBandwidth.setDescription("Maximum bandwidth that the PE can send to the CE over this\nVPN interface, in Kilo (i.e., 1000) Bytes per second.  A\nvalue of zero means there is no configured maximum.")
jnxVpnIfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1, 10), Integer().subtype(subtypeSpec=SingleValueConstraint(4,3,0,5,2,1,)).subtype(namedValues=NamedValues(("unknown", 0), ("noLocalInterface", 1), ("disabled", 2), ("encapsulationMismatch", 3), ("down", 4), ("up", 5), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnIfStatus.setDescription("Status of this interface.")
jnxVpnPwTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4))
if mibBuilder.loadTexts: jnxVpnPwTable.setDescription("Table of Pseudo-Wire Connections.")
jnxVpnPwEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1)).setIndexNames((0, "JUNIPER-VPN-MIB", "jnxVpnPwVpnType"), (0, "JUNIPER-VPN-MIB", "jnxVpnPwVpnName"), (0, "JUNIPER-VPN-MIB", "jnxVpnPwIndex"))
if mibBuilder.loadTexts: jnxVpnPwEntry.setDescription("Entry containing information about a particular VPN.")
jnxVpnPwVpnType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 1), JnxVpnType()).setMaxAccess("notifyonly")
if mibBuilder.loadTexts: jnxVpnPwVpnType.setDescription("The type of the VPN to which this Pseudo-Wire belongs.")
jnxVpnPwVpnName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 2), JnxVpnName()).setMaxAccess("notifyonly")
if mibBuilder.loadTexts: jnxVpnPwVpnName.setDescription("The name of the VPN to which this Pseudo-Wire belongs.")
jnxVpnPwIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 3), Unsigned32()).setMaxAccess("notifyonly")
if mibBuilder.loadTexts: jnxVpnPwIndex.setDescription("The index of this Pseudo-Wire in the VPN.  Each Pseudo\nWire in the VPN is given a unique index.  The RowStatus\nsays whether a given Pseudo Wire (i.e., a row in this\ntable) is valid or not. Note: this index MUST NOT be zero.")
jnxVpnPwRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 4), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwRowStatus.setDescription("This variable is used to create, modify, and/or delete a\nrow in this table.")
jnxVpnPwStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 5), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwStorageType.setDescription("This variable indicates the storage type for this object.")
jnxVpnPwAssociatedInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwAssociatedInterface.setDescription("The VPN index of the interface associated with this Pseudo\nWire, if any.  If there is no interface associated with\nthis Pseudo Wire, a value of zero is to be returned.")
jnxVpnPwLocalSiteId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwLocalSiteId.setDescription("The local site identifier for this Pseudo-Wire.  If there\nis no local site identifier, a value of zero is to be\nreturned.")
jnxVpnPwRemoteSiteId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwRemoteSiteId.setDescription("The remote site (i.e., the site at the other end of this\nPseudo-Wire) identifier.  If there is no remote site\nidentifier, a value of zero is to be returned.")
jnxVpnRemotePeIdAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 9), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnRemotePeIdAddrType.setDescription("The type of address assigned to the remote PE.")
jnxVpnRemotePeIdAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 10), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnRemotePeIdAddress.setDescription("The address of the remote PE, i.e., the router at the\nother end of the Pseudo-Wire.")
jnxVpnPwTunnelType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 11), Integer().subtype(subtypeSpec=SingleValueConstraint(5,2,1,3,7,6,4,)).subtype(namedValues=NamedValues(("static", 1), ("gre", 2), ("l2tpv3", 3), ("ipSec", 4), ("ldp", 5), ("rsvpTe", 6), ("crLdp", 7), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwTunnelType.setDescription("The type of the tunnel over which the Pseudo-Wire is\ncarried.  If several Pseudo-Wires can be carried in one\ntunnel, each Pseudo-Wire is identified by the multiplexor/\ndemultiplexor within this tunnel.")
jnxVpnPwTunnelName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 12), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwTunnelName.setDescription("The name of the Tunnel over which this Pseudo-Wire is\ncarried, if any.")
jnxVpnPwReceiveDemux = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 13), JnxVpnMultiplexor()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwReceiveDemux.setDescription("The value of the demultiplexor that identifies received\npackets as belonging to this Pseudo-Wire, if any.")
jnxVpnPwTransmitDemux = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 14), JnxVpnMultiplexor()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwTransmitDemux.setDescription("The value of the demultiplexor that identifies transmitted\npackets as belonging to this Pseudo-Wire, if any.")
jnxVpnPwStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 15), Integer().subtype(subtypeSpec=SingleValueConstraint(1,0,2,)).subtype(namedValues=NamedValues(("unknown", 0), ("down", 1), ("up", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwStatus.setDescription("Status of the Pseudo-Wire.")
jnxVpnPwTunnelStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 16), Integer().subtype(subtypeSpec=SingleValueConstraint(1,0,2,3,)).subtype(namedValues=NamedValues(("unknown", 0), ("down", 1), ("testing", 2), ("up", 3), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwTunnelStatus.setDescription("Status of the PE-to-PE tunnel over which the Pseudo-\nWire is carried.")
jnxVpnPwRemoteSiteStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 17), Integer().subtype(subtypeSpec=SingleValueConstraint(2,0,1,3,)).subtype(namedValues=NamedValues(("unknown", 0), ("outOfRange", 1), ("down", 2), ("up", 3), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwRemoteSiteStatus.setDescription("Status of the interface at the remote end of the\nPseudo-Wire.")
jnxVpnPwTimeUp = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 18), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwTimeUp.setDescription("The total time in hundredths of a second that this\nPseudo-Wire has been operational.")
jnxVpnPwTransitions = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 19), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwTransitions.setDescription("The number of state transitions (up -> down and\ndown -> up) this Tunnel has undergone.")
jnxVpnPwLastTransition = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 20), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwLastTransition.setDescription("The time in hundredths of a second since the last\ntransition occurred on this Tunnel.")
jnxVpnPwPacketsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 21), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwPacketsSent.setDescription("The number of packets that have been sent over this\nPseudo-Wire.")
jnxVpnPwOctetsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 22), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwOctetsSent.setDescription("The number of octets that have been sent over this\nPseudo-Wire.")
jnxVpnPwPacketsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 23), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwPacketsReceived.setDescription("The number of packets that have been received over this\nPseudo-Wire.")
jnxVpnPwOctetsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 24), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwOctetsReceived.setDescription("The number of octets that have been received over this\nPseudo-Wire.")
jnxVpnPwLRPacketsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwLRPacketsSent.setDescription("The number of packets that have been sent over this\nPseudo-Wire.")
jnxVpnPwLROctetsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwLROctetsSent.setDescription("The number of octets that have been sent over this\nPseudo-Wire.")
jnxVpnPwLRPacketsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwLRPacketsReceived.setDescription("The number of packets that have been received over this\nPseudo-Wire.")
jnxVpnPwLROctetsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwLROctetsReceived.setDescription("The number of octets that have been received over this\nPseudo-Wire.")
jnxVpnRTTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 5))
if mibBuilder.loadTexts: jnxVpnRTTable.setDescription("Table of Route Targets for a VPN.")
jnxVpnRTEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 5, 1)).setIndexNames((0, "JUNIPER-VPN-MIB", "jnxVpnRTVpnType"), (0, "JUNIPER-VPN-MIB", "jnxVpnRTVpnName"), (0, "JUNIPER-VPN-MIB", "jnxVpnRTIndex"))
if mibBuilder.loadTexts: jnxVpnRTEntry.setDescription("Entry containing information about a particular VPN.")
jnxVpnRTVpnType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 5, 1, 1), JnxVpnType()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxVpnRTVpnType.setDescription("The type of the VPN for which this list of Route Targets\nare defined.")
jnxVpnRTVpnName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 5, 1, 2), JnxVpnName()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxVpnRTVpnName.setDescription("The name of the VPN for which this list of Route Targets\nare defined.")
jnxVpnRTIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 5, 1, 3), Unsigned32()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxVpnRTIndex.setDescription("The index within the list of Route Targets that specifies\nindividual Route Targets that define the VPN.  Note: this\nindex MUST NOT be zero.")
jnxVpnRTRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 5, 1, 4), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnRTRowStatus.setDescription("This variable is used to create, modify, and/or delete a\nrow in this table.")
jnxVpnRTStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 5, 1, 5), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnRTStorageType.setDescription("This variable indicates the storage type for this object.")
jnxVpnRTType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 5, 1, 6), JnxVpnIdentifierType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnRTType.setDescription("Type of the following Route Target.  This can one of\n'routeTarget[012]' or 'none'.")
jnxVpnRT = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 5, 1, 7), JnxVpnIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnRT.setDescription("Route Target for the VPN.  If the jnxVpnRTType is\n'none', this value should be all zeros.")
jnxVpnRTFunction = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 5, 1, 8), Integer().subtype(subtypeSpec=SingleValueConstraint(1,3,2,)).subtype(namedValues=NamedValues(("import", 1), ("export", 2), ("both", 3), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnRTFunction.setDescription("The route target export distribution type.")
jnxVpnMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 26, 2))

# Augmentions

# Notifications

jnxVpnIfUp = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 26, 0, 1)).setObjects(*(("JUNIPER-VPN-MIB", "jnxVpnIfVpnType"), ("JUNIPER-VPN-MIB", "jnxVpnIfIndex"), ("JUNIPER-VPN-MIB", "jnxVpnIfVpnName"), ) )
if mibBuilder.loadTexts: jnxVpnIfUp.setDescription("A jnxVpnIfUp notification is generated when the interface\nwith index jnxVpnIfIndex belonging to the VPN named jnxVpnIfVpnName \nof type jnxVpnIfVpnType transitions out of the 'down' state.")
jnxVpnIfDown = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 26, 0, 2)).setObjects(*(("JUNIPER-VPN-MIB", "jnxVpnIfVpnType"), ("JUNIPER-VPN-MIB", "jnxVpnIfIndex"), ("JUNIPER-VPN-MIB", "jnxVpnIfVpnName"), ) )
if mibBuilder.loadTexts: jnxVpnIfDown.setDescription("A jnxVpnIfDown notification is generated when the interface\nwith index jnxVpnIfIndex belonging to the VPN named jnxVpnIfVpnName \nof type jnxVpnIfVpnType transitions to the 'down' state.")
jnxVpnPwUp = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 26, 0, 3)).setObjects(*(("JUNIPER-VPN-MIB", "jnxVpnPwVpnType"), ("JUNIPER-VPN-MIB", "jnxVpnPwVpnName"), ("JUNIPER-VPN-MIB", "jnxVpnPwIndex"), ) )
if mibBuilder.loadTexts: jnxVpnPwUp.setDescription("A jnxVpnPwUp notification is generated when the Pseudo-Wire\nwith index jnxVpnPwIndex belonging to the VPN named jnxVpnPwVpnName \nof type jnxVpnPwVpnType transitions out of the 'down' state.")
jnxVpnPwDown = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 26, 0, 4)).setObjects(*(("JUNIPER-VPN-MIB", "jnxVpnPwVpnType"), ("JUNIPER-VPN-MIB", "jnxVpnPwVpnName"), ("JUNIPER-VPN-MIB", "jnxVpnPwIndex"), ) )
if mibBuilder.loadTexts: jnxVpnPwDown.setDescription("A jnxVpnPwDown notification is generated when the Pseudo-Wire\nwith index jnxVpnPwIndex belonging to the VPN named jnxVpnPwVpnName \nof type jnxVpnPwVpnType transitions to the 'down' state.")

# Exports

# Module identity
mibBuilder.exportSymbols("JUNIPER-VPN-MIB", PYSNMP_MODULE_ID=jnxVpnMIB)

# Types
mibBuilder.exportSymbols("JUNIPER-VPN-MIB", JnxVpnIdentifier=JnxVpnIdentifier, JnxVpnIdentifierType=JnxVpnIdentifierType, JnxVpnLocalSwitchIdentifier=JnxVpnLocalSwitchIdentifier, JnxVpnMultiplexor=JnxVpnMultiplexor, JnxVpnName=JnxVpnName, JnxVpnRouteDistinguisher=JnxVpnRouteDistinguisher, JnxVpnRouteDistinguisher0=JnxVpnRouteDistinguisher0, JnxVpnRouteDistinguisher1=JnxVpnRouteDistinguisher1, JnxVpnRouteDistinguisher2=JnxVpnRouteDistinguisher2, JnxVpnRouteTarget=JnxVpnRouteTarget, JnxVpnRouteTarget0=JnxVpnRouteTarget0, JnxVpnRouteTarget1=JnxVpnRouteTarget1, JnxVpnRouteTarget2=JnxVpnRouteTarget2, JnxVpnType=JnxVpnType, JnxVpnVCIdentifier=JnxVpnVCIdentifier)

# Objects
mibBuilder.exportSymbols("JUNIPER-VPN-MIB", jnxVpnMIB=jnxVpnMIB, jnxVpnMIBNotifications=jnxVpnMIBNotifications, jnxVpnMibObjects=jnxVpnMibObjects, jnxVpnInfo=jnxVpnInfo, jnxVpnConfiguredVpns=jnxVpnConfiguredVpns, jnxVpnActiveVpns=jnxVpnActiveVpns, jnxVpnNextIfIndex=jnxVpnNextIfIndex, jnxVpnNextPwIndex=jnxVpnNextPwIndex, jnxVpnNextRTIndex=jnxVpnNextRTIndex, jnxVpnTable=jnxVpnTable, jnxVpnEntry=jnxVpnEntry, jnxVpnType=jnxVpnType, jnxVpnName=jnxVpnName, jnxVpnRowStatus=jnxVpnRowStatus, jnxVpnStorageType=jnxVpnStorageType, jnxVpnDescription=jnxVpnDescription, jnxVpnIdentifierType=jnxVpnIdentifierType, jnxVpnIdentifier=jnxVpnIdentifier, jnxVpnConfiguredSites=jnxVpnConfiguredSites, jnxVpnActiveSites=jnxVpnActiveSites, jnxVpnLocalAddresses=jnxVpnLocalAddresses, jnxVpnTotalAddresses=jnxVpnTotalAddresses, jnxVpnAge=jnxVpnAge, jnxVpnIfTable=jnxVpnIfTable, jnxVpnIfEntry=jnxVpnIfEntry, jnxVpnIfVpnType=jnxVpnIfVpnType, jnxVpnIfVpnName=jnxVpnIfVpnName, jnxVpnIfIndex=jnxVpnIfIndex, jnxVpnIfRowStatus=jnxVpnIfRowStatus, jnxVpnIfStorageType=jnxVpnIfStorageType, jnxVpnIfAssociatedPw=jnxVpnIfAssociatedPw, jnxVpnIfProtocol=jnxVpnIfProtocol, jnxVpnIfInBandwidth=jnxVpnIfInBandwidth, jnxVpnIfOutBandwidth=jnxVpnIfOutBandwidth, jnxVpnIfStatus=jnxVpnIfStatus, jnxVpnPwTable=jnxVpnPwTable, jnxVpnPwEntry=jnxVpnPwEntry, jnxVpnPwVpnType=jnxVpnPwVpnType, jnxVpnPwVpnName=jnxVpnPwVpnName, jnxVpnPwIndex=jnxVpnPwIndex, jnxVpnPwRowStatus=jnxVpnPwRowStatus, jnxVpnPwStorageType=jnxVpnPwStorageType, jnxVpnPwAssociatedInterface=jnxVpnPwAssociatedInterface, jnxVpnPwLocalSiteId=jnxVpnPwLocalSiteId, jnxVpnPwRemoteSiteId=jnxVpnPwRemoteSiteId, jnxVpnRemotePeIdAddrType=jnxVpnRemotePeIdAddrType, jnxVpnRemotePeIdAddress=jnxVpnRemotePeIdAddress, jnxVpnPwTunnelType=jnxVpnPwTunnelType, jnxVpnPwTunnelName=jnxVpnPwTunnelName, jnxVpnPwReceiveDemux=jnxVpnPwReceiveDemux, jnxVpnPwTransmitDemux=jnxVpnPwTransmitDemux, jnxVpnPwStatus=jnxVpnPwStatus, jnxVpnPwTunnelStatus=jnxVpnPwTunnelStatus, jnxVpnPwRemoteSiteStatus=jnxVpnPwRemoteSiteStatus, jnxVpnPwTimeUp=jnxVpnPwTimeUp, jnxVpnPwTransitions=jnxVpnPwTransitions, jnxVpnPwLastTransition=jnxVpnPwLastTransition, jnxVpnPwPacketsSent=jnxVpnPwPacketsSent, jnxVpnPwOctetsSent=jnxVpnPwOctetsSent, jnxVpnPwPacketsReceived=jnxVpnPwPacketsReceived, jnxVpnPwOctetsReceived=jnxVpnPwOctetsReceived, jnxVpnPwLRPacketsSent=jnxVpnPwLRPacketsSent, jnxVpnPwLROctetsSent=jnxVpnPwLROctetsSent, jnxVpnPwLRPacketsReceived=jnxVpnPwLRPacketsReceived, jnxVpnPwLROctetsReceived=jnxVpnPwLROctetsReceived, jnxVpnRTTable=jnxVpnRTTable, jnxVpnRTEntry=jnxVpnRTEntry, jnxVpnRTVpnType=jnxVpnRTVpnType, jnxVpnRTVpnName=jnxVpnRTVpnName, jnxVpnRTIndex=jnxVpnRTIndex, jnxVpnRTRowStatus=jnxVpnRTRowStatus, jnxVpnRTStorageType=jnxVpnRTStorageType, jnxVpnRTType=jnxVpnRTType, jnxVpnRT=jnxVpnRT, jnxVpnRTFunction=jnxVpnRTFunction, jnxVpnMIBConformance=jnxVpnMIBConformance)

# Notifications
mibBuilder.exportSymbols("JUNIPER-VPN-MIB", jnxVpnIfUp=jnxVpnIfUp, jnxVpnIfDown=jnxVpnIfDown, jnxVpnPwUp=jnxVpnPwUp, jnxVpnPwDown=jnxVpnPwDown)

