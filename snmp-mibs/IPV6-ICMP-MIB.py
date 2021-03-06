# PySNMP SMI module. Autogenerated from smidump -f python IPV6-ICMP-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:57:43 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( ipv6IfEntry, ) = mibBuilder.importSymbols("IPV6-MIB", "ipv6IfEntry")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "mib-2")

# Objects

ipv6IcmpMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 56)).setRevisions(("1998-01-08 21:55",))
if mibBuilder.loadTexts: ipv6IcmpMIB.setOrganization("IETF IPv6 Working Group")
if mibBuilder.loadTexts: ipv6IcmpMIB.setContactInfo("           Dimitry Haskin\n\nPostal: Bay Networks, Inc.\n        660 Techology Park Drive.\n        Billerica, MA  01821\n        US\n\n   Tel: +1-978-916-8124\nE-mail: dhaskin@baynetworks.com\n\n        Steve Onishi\n\nPostal: Bay Networks, Inc.\n        3 Federal Street\n        Billerica, MA 01821\n        US\n\n   Tel: +1-978-916-3816\nE-mail: sonishi@baynetworks.com")
if mibBuilder.loadTexts: ipv6IcmpMIB.setDescription("The MIB module for entities implementing\nthe ICMPv6.")
ipv6IcmpMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 56, 1))
ipv6IfIcmpTable = MibTable((1, 3, 6, 1, 2, 1, 56, 1, 1))
if mibBuilder.loadTexts: ipv6IfIcmpTable.setDescription("IPv6 ICMP statistics. This table contains statistics\nof ICMPv6 messages that are received and sourced by\nthe entity.")
ipv6IfIcmpEntry = MibTableRow((1, 3, 6, 1, 2, 1, 56, 1, 1, 1))
if mibBuilder.loadTexts: ipv6IfIcmpEntry.setDescription("An ICMPv6 statistics entry containing\nobjects at a particular IPv6 interface.\n\nNote that a receiving interface is\nthe interface to which a given ICMPv6 message\nis addressed which may not be necessarily\nthe input interface for the message.\n\nSimilarly,  the sending interface is\nthe interface that sources a given\nICMP message which is usually but not\nnecessarily the output interface for the message.")
ipv6IfIcmpInMsgs = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpInMsgs.setDescription("The total number of ICMP messages received\nby the interface which includes all those\ncounted by ipv6IfIcmpInErrors. Note that this\ninterface is the interface to which the\nICMP messages were addressed which may not be\nnecessarily the input interface for the messages.")
ipv6IfIcmpInErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpInErrors.setDescription("The number of ICMP messages which the interface\nreceived but determined as having ICMP-specific\nerrors (bad ICMP checksums, bad length, etc.).")
ipv6IfIcmpInDestUnreachs = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpInDestUnreachs.setDescription("The number of ICMP Destination Unreachable\nmessages received by the interface.")
ipv6IfIcmpInAdminProhibs = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpInAdminProhibs.setDescription("The number of ICMP destination\nunreachable/communication administratively\nprohibited messages received by the interface.")
ipv6IfIcmpInTimeExcds = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpInTimeExcds.setDescription("The number of ICMP Time Exceeded messages\nreceived by the interface.")
ipv6IfIcmpInParmProblems = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpInParmProblems.setDescription("The number of ICMP Parameter Problem messages\nreceived by the interface.")
ipv6IfIcmpInPktTooBigs = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpInPktTooBigs.setDescription("The number of ICMP Packet Too Big messages\nreceived by the interface.")
ipv6IfIcmpInEchos = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpInEchos.setDescription("The number of ICMP Echo (request) messages\nreceived by the interface.")
ipv6IfIcmpInEchoReplies = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpInEchoReplies.setDescription("The number of ICMP Echo Reply messages received\nby the interface.")
ipv6IfIcmpInRouterSolicits = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpInRouterSolicits.setDescription("The number of ICMP Router Solicit messages\nreceived by the interface.")
ipv6IfIcmpInRouterAdvertisements = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpInRouterAdvertisements.setDescription("The number of ICMP Router Advertisement messages\nreceived by the interface.")
ipv6IfIcmpInNeighborSolicits = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpInNeighborSolicits.setDescription("The number of ICMP Neighbor Solicit messages\nreceived by the interface.")
ipv6IfIcmpInNeighborAdvertisements = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpInNeighborAdvertisements.setDescription("The number of ICMP Neighbor Advertisement\nmessages received by the interface.")
ipv6IfIcmpInRedirects = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpInRedirects.setDescription("The number of Redirect messages received\nby the interface.")
ipv6IfIcmpInGroupMembQueries = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpInGroupMembQueries.setDescription("The number of ICMPv6 Group Membership Query\nmessages received by the interface.")
ipv6IfIcmpInGroupMembResponses = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpInGroupMembResponses.setDescription("The number of ICMPv6 Group Membership Response messages\nreceived by the interface.")
ipv6IfIcmpInGroupMembReductions = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpInGroupMembReductions.setDescription("The number of ICMPv6 Group Membership Reduction messages\nreceived by the interface.")
ipv6IfIcmpOutMsgs = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpOutMsgs.setDescription("The total number of ICMP messages which this\ninterface attempted to send.  Note that this counter\nincludes all those counted by icmpOutErrors.")
ipv6IfIcmpOutErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpOutErrors.setDescription("The number of ICMP messages which this interface did\nnot send due to problems discovered within ICMP\nsuch as a lack of buffers.  This value should not\ninclude errors discovered outside the ICMP layer\nsuch as the inability of IPv6 to route the resultant\ndatagram.  In some implementations there may be no\ntypes of error which contribute to this counter's\nvalue.")
ipv6IfIcmpOutDestUnreachs = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpOutDestUnreachs.setDescription("The number of ICMP Destination Unreachable\n\nmessages sent by the interface.")
ipv6IfIcmpOutAdminProhibs = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpOutAdminProhibs.setDescription("Number of ICMP dest unreachable/communication\nadministratively prohibited messages sent.")
ipv6IfIcmpOutTimeExcds = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpOutTimeExcds.setDescription("The number of ICMP Time Exceeded messages sent\nby the interface.")
ipv6IfIcmpOutParmProblems = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpOutParmProblems.setDescription("The number of ICMP Parameter Problem messages\nsent by the interface.")
ipv6IfIcmpOutPktTooBigs = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpOutPktTooBigs.setDescription("The number of ICMP Packet Too Big messages sent\nby the interface.")
ipv6IfIcmpOutEchos = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpOutEchos.setDescription("The number of ICMP Echo (request) messages sent\nby the interface.")
ipv6IfIcmpOutEchoReplies = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpOutEchoReplies.setDescription("The number of ICMP Echo Reply messages sent\nby the interface.")
ipv6IfIcmpOutRouterSolicits = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpOutRouterSolicits.setDescription("The number of ICMP Router Solicitation messages\nsent by the interface.")
ipv6IfIcmpOutRouterAdvertisements = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpOutRouterAdvertisements.setDescription("The number of ICMP Router Advertisement messages\nsent by the interface.")
ipv6IfIcmpOutNeighborSolicits = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpOutNeighborSolicits.setDescription("The number of ICMP Neighbor Solicitation\nmessages sent by the interface.")
ipv6IfIcmpOutNeighborAdvertisements = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpOutNeighborAdvertisements.setDescription("The number of ICMP Neighbor Advertisement\nmessages sent by the interface.")
ipv6IfIcmpOutRedirects = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpOutRedirects.setDescription("The number of Redirect messages sent. For\na host, this object will always be zero,\nsince hosts do not send redirects.")
ipv6IfIcmpOutGroupMembQueries = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 32), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpOutGroupMembQueries.setDescription("The number of ICMPv6 Group Membership Query\nmessages sent.")
ipv6IfIcmpOutGroupMembResponses = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 33), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpOutGroupMembResponses.setDescription("The number of ICMPv6 Group Membership Response\nmessages sent.")
ipv6IfIcmpOutGroupMembReductions = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 34), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpOutGroupMembReductions.setDescription("The number of ICMPv6 Group Membership Reduction\nmessages sent.")
ipv6IcmpConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 56, 2))
ipv6IcmpCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 56, 2, 1))
ipv6IcmpGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 56, 2, 2))

# Augmentions
ipv6IfEntry, = mibBuilder.importSymbols("IPV6-MIB", "ipv6IfEntry")
ipv6IfEntry.registerAugmentions(("IPV6-ICMP-MIB", "ipv6IfIcmpEntry"))
ipv6IfIcmpEntry.setIndexNames(*ipv6IfEntry.getIndexNames())

# Groups

ipv6IcmpGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 56, 2, 2, 1)).setObjects(*(("IPV6-ICMP-MIB", "ipv6IfIcmpInParmProblems"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInEchos"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutEchoReplies"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutAdminProhibs"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutGroupMembReductions"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutGroupMembResponses"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutDestUnreachs"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInGroupMembQueries"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutMsgs"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutErrors"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInMsgs"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutGroupMembQueries"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInTimeExcds"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInGroupMembReductions"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutPktTooBigs"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutRedirects"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutParmProblems"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInDestUnreachs"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInEchoReplies"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutRouterSolicits"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutNeighborAdvertisements"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInAdminProhibs"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInGroupMembResponses"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutEchos"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutNeighborSolicits"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutRouterAdvertisements"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInPktTooBigs"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInNeighborAdvertisements"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutTimeExcds"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInRedirects"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInErrors"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInNeighborSolicits"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInRouterAdvertisements"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInRouterSolicits"), ) )
if mibBuilder.loadTexts: ipv6IcmpGroup.setDescription("The ICMPv6 group of objects providing information\nspecific to ICMPv6.")

# Compliances

ipv6IcmpCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 56, 2, 1, 1)).setObjects(*(("IPV6-ICMP-MIB", "ipv6IcmpGroup"), ) )
if mibBuilder.loadTexts: ipv6IcmpCompliance.setDescription("The compliance statement for SNMPv2 entities which\nimplement ICMPv6.")

# Exports

# Module identity
mibBuilder.exportSymbols("IPV6-ICMP-MIB", PYSNMP_MODULE_ID=ipv6IcmpMIB)

# Objects
mibBuilder.exportSymbols("IPV6-ICMP-MIB", ipv6IcmpMIB=ipv6IcmpMIB, ipv6IcmpMIBObjects=ipv6IcmpMIBObjects, ipv6IfIcmpTable=ipv6IfIcmpTable, ipv6IfIcmpEntry=ipv6IfIcmpEntry, ipv6IfIcmpInMsgs=ipv6IfIcmpInMsgs, ipv6IfIcmpInErrors=ipv6IfIcmpInErrors, ipv6IfIcmpInDestUnreachs=ipv6IfIcmpInDestUnreachs, ipv6IfIcmpInAdminProhibs=ipv6IfIcmpInAdminProhibs, ipv6IfIcmpInTimeExcds=ipv6IfIcmpInTimeExcds, ipv6IfIcmpInParmProblems=ipv6IfIcmpInParmProblems, ipv6IfIcmpInPktTooBigs=ipv6IfIcmpInPktTooBigs, ipv6IfIcmpInEchos=ipv6IfIcmpInEchos, ipv6IfIcmpInEchoReplies=ipv6IfIcmpInEchoReplies, ipv6IfIcmpInRouterSolicits=ipv6IfIcmpInRouterSolicits, ipv6IfIcmpInRouterAdvertisements=ipv6IfIcmpInRouterAdvertisements, ipv6IfIcmpInNeighborSolicits=ipv6IfIcmpInNeighborSolicits, ipv6IfIcmpInNeighborAdvertisements=ipv6IfIcmpInNeighborAdvertisements, ipv6IfIcmpInRedirects=ipv6IfIcmpInRedirects, ipv6IfIcmpInGroupMembQueries=ipv6IfIcmpInGroupMembQueries, ipv6IfIcmpInGroupMembResponses=ipv6IfIcmpInGroupMembResponses, ipv6IfIcmpInGroupMembReductions=ipv6IfIcmpInGroupMembReductions, ipv6IfIcmpOutMsgs=ipv6IfIcmpOutMsgs, ipv6IfIcmpOutErrors=ipv6IfIcmpOutErrors, ipv6IfIcmpOutDestUnreachs=ipv6IfIcmpOutDestUnreachs, ipv6IfIcmpOutAdminProhibs=ipv6IfIcmpOutAdminProhibs, ipv6IfIcmpOutTimeExcds=ipv6IfIcmpOutTimeExcds, ipv6IfIcmpOutParmProblems=ipv6IfIcmpOutParmProblems, ipv6IfIcmpOutPktTooBigs=ipv6IfIcmpOutPktTooBigs, ipv6IfIcmpOutEchos=ipv6IfIcmpOutEchos, ipv6IfIcmpOutEchoReplies=ipv6IfIcmpOutEchoReplies, ipv6IfIcmpOutRouterSolicits=ipv6IfIcmpOutRouterSolicits, ipv6IfIcmpOutRouterAdvertisements=ipv6IfIcmpOutRouterAdvertisements, ipv6IfIcmpOutNeighborSolicits=ipv6IfIcmpOutNeighborSolicits, ipv6IfIcmpOutNeighborAdvertisements=ipv6IfIcmpOutNeighborAdvertisements, ipv6IfIcmpOutRedirects=ipv6IfIcmpOutRedirects, ipv6IfIcmpOutGroupMembQueries=ipv6IfIcmpOutGroupMembQueries, ipv6IfIcmpOutGroupMembResponses=ipv6IfIcmpOutGroupMembResponses, ipv6IfIcmpOutGroupMembReductions=ipv6IfIcmpOutGroupMembReductions, ipv6IcmpConformance=ipv6IcmpConformance, ipv6IcmpCompliances=ipv6IcmpCompliances, ipv6IcmpGroups=ipv6IcmpGroups)

# Groups
mibBuilder.exportSymbols("IPV6-ICMP-MIB", ipv6IcmpGroup=ipv6IcmpGroup)

# Compliances
mibBuilder.exportSymbols("IPV6-ICMP-MIB", ipv6IcmpCompliance=ipv6IcmpCompliance)
