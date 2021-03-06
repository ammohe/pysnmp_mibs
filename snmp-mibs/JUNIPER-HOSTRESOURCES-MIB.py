# PySNMP SMI module. Autogenerated from smidump -f python JUNIPER-HOSTRESOURCES-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:57:50 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( hrStorageEntry, ) = mibBuilder.importSymbols("HOST-RESOURCES-MIB", "hrStorageEntry")
( jnxMibs, ) = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs")
( Bits, Gauge32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")

# Objects

jnxHostResourcesMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 31)).setRevisions(("2004-08-18 00:00","2004-05-05 00:00",))
if mibBuilder.loadTexts: jnxHostResourcesMIB.setOrganization("Juniper Networks, Inc.")
if mibBuilder.loadTexts: jnxHostResourcesMIB.setContactInfo("        Juniper Technical Assistance Center\nJuniper Networks, Inc.\n1194 N. Mathilda Avenue\nSunnyvale, CA 94089\nE-mail: support@juniper.net")
if mibBuilder.loadTexts: jnxHostResourcesMIB.setDescription("Extends the HOST-RESOURCES-MIB (rfc2790).")
jnxHrStorage = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 31, 1))
jnxHrStorageTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 31, 1, 1))
if mibBuilder.loadTexts: jnxHrStorageTable.setDescription("Augments the hrStorageTable with additional data.")
jnxHrStorageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 31, 1, 1, 1))
if mibBuilder.loadTexts: jnxHrStorageEntry.setDescription("Each entry provides additional file system data beyond that\navailable in the hrStorageTable.")
jnxHrStoragePercentUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 31, 1, 1, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxHrStoragePercentUsed.setDescription("The amount of the storage represented by this entry\nthat is allocated, as a percentage of the total amount\navailable.")

# Augmentions
hrStorageEntry, = mibBuilder.importSymbols("HOST-RESOURCES-MIB", "hrStorageEntry")
hrStorageEntry.registerAugmentions(("JUNIPER-HOSTRESOURCES-MIB", "jnxHrStorageEntry"))
jnxHrStorageEntry.setIndexNames(*hrStorageEntry.getIndexNames())

# Exports

# Module identity
mibBuilder.exportSymbols("JUNIPER-HOSTRESOURCES-MIB", PYSNMP_MODULE_ID=jnxHostResourcesMIB)

# Objects
mibBuilder.exportSymbols("JUNIPER-HOSTRESOURCES-MIB", jnxHostResourcesMIB=jnxHostResourcesMIB, jnxHrStorage=jnxHrStorage, jnxHrStorageTable=jnxHrStorageTable, jnxHrStorageEntry=jnxHrStorageEntry, jnxHrStoragePercentUsed=jnxHrStoragePercentUsed)

