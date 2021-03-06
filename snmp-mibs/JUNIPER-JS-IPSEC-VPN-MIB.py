# PySNMP SMI module. Autogenerated from smidump -f python JUNIPER-JS-IPSEC-VPN-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:57:51 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( jnxIpSecTunnelMonEntry, ) = mibBuilder.importSymbols("JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIpSecTunnelMonEntry")
( jnxJsIPSecVpn, ) = mibBuilder.importSymbols("JUNIPER-JS-SMI", "jnxJsIPSecVpn")
( Bits, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")

# Types

class JnxJsIpSecVpnType(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(1,2,)
    namedValues = NamedValues(("policyBased", 1), ("routeBased", 2), )
    

# Objects

jnxJsIpSecVpnMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5, 1)).setRevisions(("2007-05-11 21:53","2007-04-27 00:00",))
if mibBuilder.loadTexts: jnxJsIpSecVpnMib.setOrganization("Juniper Networks, Inc.")
if mibBuilder.loadTexts: jnxJsIpSecVpnMib.setContactInfo("Juniper Technical Assistance Center\nJuniper Networks, Inc.\n1194 N. Mathilda Avenue\nSunnyvale, CA 94089\nE-mail: support@juniper.net")
if mibBuilder.loadTexts: jnxJsIpSecVpnMib.setDescription("This module defines the object used to monitor the\nentries pertaining to IPSec objects and the management\nof the IPSEC VPN functionalities for Juniper security \nproduct lines.  \n\nThis mib module extend Juniper's common IPSEC flow monitoring\nMIB, building on the existing common infrastruature, the  \n security implementation integrates the value-added \n features for the security products")
jnxJsIpSecVpnNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5, 1, 0))
jnxJsIpSecVpnPhaseOne = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5, 1, 1))
jnxJsIpSecVpnPhaseTwo = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5, 1, 2))
jnxJsIpSecTunnelTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5, 1, 2, 1))
if mibBuilder.loadTexts: jnxJsIpSecTunnelTable.setDescription("The IPsec Phase-2 Tunnel Table.\nThere is one entry in this table for each active IPsec Phase-2 \nTunnel.  If the tunnel is terminated, then the entry is no longer \navailable after the table has been refreshed. ")
jnxJsIpSecTunnelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5, 1, 2, 1, 1))
if mibBuilder.loadTexts: jnxJsIpSecTunnelEntry.setDescription("Each entry contains the attributes\nassociated with an active IPsec Phase-2 Tunnel.")
jnxJsIpSecTunPolicyName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5, 1, 2, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsIpSecTunPolicyName.setDescription("The policy name assoicated with this tunnel if the \nthis IPSEC VPN is policy based.  Otherwise, this attribute\nis not applicable.")
jnxJsIpSecVpnTunType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5, 1, 2, 1, 1, 2), JnxJsIpSecVpnType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsIpSecVpnTunType.setDescription("This attribute indicates the IPSEC VPN tunnel is policy\nbased or route based.")
jnxJsIpSecTunCfgMonState = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5, 1, 2, 1, 1, 3), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("disable", 1), ("enable", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsIpSecTunCfgMonState.setDescription("The user configuration states whether to monitor the  \nIPSec tunnel to be alive or not. ")
jnxJsIpSecTunState = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5, 1, 2, 1, 1, 4), Integer().subtype(subtypeSpec=SingleValueConstraint(2,3,1,)).subtype(namedValues=NamedValues(("up", 1), ("down", 2), ("vpnMonitoringDisabled", 3), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsIpSecTunState.setDescription("This attribute indicates whether the IPSec Tunnel is up or\ndown, determined by icmp ping if the jnxJsIpSecTunCfgMonState\nis enable.  \n\nDown: VPN monitor detects the tunnel is down\nUp:   VPN monitor detects the tunnel is up.\nvpnMonitoringDisabled: user has disabled VPN tunnel monitoring.")

# Augmentions
jnxIpSecTunnelMonEntry, = mibBuilder.importSymbols("JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIpSecTunnelMonEntry")
jnxIpSecTunnelMonEntry.registerAugmentions(("JUNIPER-JS-IPSEC-VPN-MIB", "jnxJsIpSecTunnelEntry"))
jnxJsIpSecTunnelEntry.setIndexNames(*jnxIpSecTunnelMonEntry.getIndexNames())

# Exports

# Module identity
mibBuilder.exportSymbols("JUNIPER-JS-IPSEC-VPN-MIB", PYSNMP_MODULE_ID=jnxJsIpSecVpnMib)

# Types
mibBuilder.exportSymbols("JUNIPER-JS-IPSEC-VPN-MIB", JnxJsIpSecVpnType=JnxJsIpSecVpnType)

# Objects
mibBuilder.exportSymbols("JUNIPER-JS-IPSEC-VPN-MIB", jnxJsIpSecVpnMib=jnxJsIpSecVpnMib, jnxJsIpSecVpnNotifications=jnxJsIpSecVpnNotifications, jnxJsIpSecVpnPhaseOne=jnxJsIpSecVpnPhaseOne, jnxJsIpSecVpnPhaseTwo=jnxJsIpSecVpnPhaseTwo, jnxJsIpSecTunnelTable=jnxJsIpSecTunnelTable, jnxJsIpSecTunnelEntry=jnxJsIpSecTunnelEntry, jnxJsIpSecTunPolicyName=jnxJsIpSecTunPolicyName, jnxJsIpSecVpnTunType=jnxJsIpSecVpnTunType, jnxJsIpSecTunCfgMonState=jnxJsIpSecTunCfgMonState, jnxJsIpSecTunState=jnxJsIpSecTunState)

