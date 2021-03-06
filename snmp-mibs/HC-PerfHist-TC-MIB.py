# PySNMP SMI module. Autogenerated from smidump -f python HC-PerfHist-TC-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:57:40 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( Bits, Counter64, Integer32, Integer32, ModuleIdentity, MibIdentifier, TimeTicks, Unsigned32, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "Unsigned32", "mib-2")
( TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention")

# Types

class HCPerfIntervalThreshold(Unsigned32):
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(0,900)
    
class HCPerfInvalidIntervals(Integer32):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(0,96)
    
class HCPerfTimeElapsed(Integer32):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(0,86399)
    
class HCPerfValidIntervals(Integer32):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(0,96)
    
class HCPerfCurrentCount(Counter64):
    pass

class HCPerfIntervalCount(Counter64):
    pass

class HCPerfTotalCount(Counter64):
    pass


# Objects

hcPerfHistTCMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 107)).setRevisions(("2004-02-03 00:00",))
if mibBuilder.loadTexts: hcPerfHistTCMIB.setOrganization("ADSLMIB Working Group")
if mibBuilder.loadTexts: hcPerfHistTCMIB.setContactInfo("WG-email:  adslmib@ietf.org\nInfo:      https://www1.ietf.org/mailman/listinfo/adslmib\n\nChair:     Mike Sneed\n           Sand Channel Systems\nPostal:    P.O.  Box 37324\n           Raleigh NC 27627-7324\n           USA\nEmail:     sneedmike@hotmail.com\nPhone:     +1 206 600 7022\n\nCo-editor: Bob Ray\n           PESA Switching Systems, Inc.\nPostal:    330-A Wynn Drive\n           Huntsville, AL 35805\n           USA\nEmail:     rray@pesa.com\nPhone:     +1 256 726 9200 ext.  142\n\nCo-editor: Rajesh Abbi\n           Alcatel USA\nPostal:    2301 Sugar Bush Road\n           Raleigh, NC 27612-3339\n           USA\nEmail:     Rajesh.Abbi@alcatel.com\nPhone:     +1 919 850 6194")
if mibBuilder.loadTexts: hcPerfHistTCMIB.setDescription("This MIB Module provides Textual Conventions to be\nused by systems supporting 15 minute based performance\nhistory counts that require high-capacity counts.\n\nCopyright (C) The Internet Society (2004).  This version\nof this MIB module is part of RFC 3705: see the RFC\nitself for full legal notices.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("HC-PerfHist-TC-MIB", PYSNMP_MODULE_ID=hcPerfHistTCMIB)

# Types
mibBuilder.exportSymbols("HC-PerfHist-TC-MIB", HCPerfIntervalThreshold=HCPerfIntervalThreshold, HCPerfInvalidIntervals=HCPerfInvalidIntervals, HCPerfTimeElapsed=HCPerfTimeElapsed, HCPerfValidIntervals=HCPerfValidIntervals, HCPerfCurrentCount=HCPerfCurrentCount, HCPerfIntervalCount=HCPerfIntervalCount, HCPerfTotalCount=HCPerfTotalCount)

# Objects
mibBuilder.exportSymbols("HC-PerfHist-TC-MIB", hcPerfHistTCMIB=hcPerfHistTCMIB)

