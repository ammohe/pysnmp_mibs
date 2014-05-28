# PySNMP SMI module. Autogenerated from smidump -f python JUNIPER-LICENSE-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:57:51 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( jnxLicenseMibRoot, ) = mibBuilder.importSymbols("JUNIPER-SMI", "jnxLicenseMibRoot")
( Bits, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "TimeTicks", "Unsigned32")
( DisplayString, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString")

# Objects

jnxLicenseMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1)).setRevisions(("2010-07-09 00:00",))
if mibBuilder.loadTexts: jnxLicenseMIB.setOrganization("Juniper Networks, Inc.")
if mibBuilder.loadTexts: jnxLicenseMIB.setContactInfo("Juniper Technical Assistance Center\nJuniper Networks, Inc.\n1194 N. Mathilda Avenue\nSunnyvale, CA 94089\nE-mail: support@juniper.net")
if mibBuilder.loadTexts: jnxLicenseMIB.setDescription("Implementation of enterprise specific MIB\nfor license commands and configuration.")
jnxLicenseNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 0))
jnxLicenseObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1))
jnxLicenseInstallObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1))
jnxLicenseInstallTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 1))
if mibBuilder.loadTexts: jnxLicenseInstallTable.setDescription("This table contains installed feature license information.")
jnxLicenseInstallEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 1, 1)).setIndexNames((1, "JUNIPER-LICENSE-MIB", "jnxLicenseId"))
if mibBuilder.loadTexts: jnxLicenseInstallEntry.setDescription("A row of giving installed feature license information.")
jnxLicenseId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 1, 1, 1), DisplayString()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxLicenseId.setDescription("Installed feature licenses Id.")
jnxLicenseVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLicenseVersion.setDescription("License Version information")
jnxLicenseDeviceId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLicenseDeviceId.setDescription("License Device Id ")
jnxLicenseType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 1, 1, 4), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,3,0,)).subtype(namedValues=NamedValues(("invalid", 0), ("count-down", 1), ("date-based", 2), ("permanent", 3), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLicenseType.setDescription("License type information")
jnxLicenseKeys = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 1, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLicenseKeys.setDescription("License Keys")
jnxLicenseFeatureListTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 2))
if mibBuilder.loadTexts: jnxLicenseFeatureListTable.setDescription("list of features supporting Licensing.")
jnxLicenseFeatureListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 2, 1)).setIndexNames((0, "JUNIPER-LICENSE-MIB", "jnxLicenseFeatureId"))
if mibBuilder.loadTexts: jnxLicenseFeatureListEntry.setDescription("A row of licensed features.")
jnxLicenseFeatureId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 2, 1, 1), Integer32()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxLicenseFeatureId.setDescription("Feature Id to point an entry in this table")
jnxLicenseFeatureName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLicenseFeatureName.setDescription("Feature Name")
jnxLicenseFeatureDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLicenseFeatureDescr.setDescription("Feature Name")
jnxLicenseFeatureLicenseId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLicenseFeatureLicenseId.setDescription("Feature License Id")
jnxLicenseFeatureLicenseUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLicenseFeatureLicenseUsed.setDescription("Licenses Used")
jnxLicenseFeatureLicenseInstalled = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLicenseFeatureLicenseInstalled.setDescription("Licenses Installed")
jnxLicenseFeatureLicenseNeeded = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLicenseFeatureLicenseNeeded.setDescription("Licenses Needed")
jnxLicenseSettings = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 2))
jnxLicenseRenewBeforExpiration = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLicenseRenewBeforExpiration.setDescription("License renew lead time before expiration in days.")
jnxLicenseRenewInterval = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLicenseRenewInterval.setDescription("License checking interval in hours.")
jnxLicenseAutoUpdate = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 2, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLicenseAutoUpdate.setDescription("License auto update URL of a license server.")

# Augmentions

# Notifications

jnxLicenseGraceExpired = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 0, 1)).setObjects(*(("JUNIPER-LICENSE-MIB", "jnxLicenseFeatureName"), ) )
if mibBuilder.loadTexts: jnxLicenseGraceExpired.setDescription("The SNMP trap that is generated when the license grace period for\nfeature identified by jnxLicenseFeatureName is expired")
jnxLicenseGraceAboutToExpire = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 0, 2)).setObjects(*(("JUNIPER-LICENSE-MIB", "jnxLicenseFeatureName"), ) )
if mibBuilder.loadTexts: jnxLicenseGraceAboutToExpire.setDescription("The SNMP trap that is generated when the license grace period for\nfeature identified by jnxLicenseFeatureName is about to expire")
jnxLicenseAboutToExpire = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 0, 3)).setObjects(*(("JUNIPER-LICENSE-MIB", "jnxLicenseFeatureName"), ) )
if mibBuilder.loadTexts: jnxLicenseAboutToExpire.setDescription("The SNMP trap that is generated when the license period for\nfeature identified by jnxLicenseFeatureName is about to expire")
jnxLicenseInfringeCumulative = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 0, 4)).setObjects(*(("JUNIPER-LICENSE-MIB", "jnxLicenseFeatureName"), ) )
if mibBuilder.loadTexts: jnxLicenseInfringeCumulative.setDescription("The SNMP trap that is generated when the feature is used more\ntimes than as specified in number of licenses allowed for feature\nas identified by jnxLicenseFeatureName")
jnxLicenseInfringeSingle = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 0, 5)).setObjects(*(("JUNIPER-LICENSE-MIB", "jnxLicenseFeatureName"), ) )
if mibBuilder.loadTexts: jnxLicenseInfringeSingle.setDescription("The SNMP trap that is generated when the license for feature\nidentified by jnxLicenseFeatureName is not valid i.e. either expired or\nnot available.")

# Exports

# Module identity
mibBuilder.exportSymbols("JUNIPER-LICENSE-MIB", PYSNMP_MODULE_ID=jnxLicenseMIB)

# Objects
mibBuilder.exportSymbols("JUNIPER-LICENSE-MIB", jnxLicenseMIB=jnxLicenseMIB, jnxLicenseNotifications=jnxLicenseNotifications, jnxLicenseObjects=jnxLicenseObjects, jnxLicenseInstallObjects=jnxLicenseInstallObjects, jnxLicenseInstallTable=jnxLicenseInstallTable, jnxLicenseInstallEntry=jnxLicenseInstallEntry, jnxLicenseId=jnxLicenseId, jnxLicenseVersion=jnxLicenseVersion, jnxLicenseDeviceId=jnxLicenseDeviceId, jnxLicenseType=jnxLicenseType, jnxLicenseKeys=jnxLicenseKeys, jnxLicenseFeatureListTable=jnxLicenseFeatureListTable, jnxLicenseFeatureListEntry=jnxLicenseFeatureListEntry, jnxLicenseFeatureId=jnxLicenseFeatureId, jnxLicenseFeatureName=jnxLicenseFeatureName, jnxLicenseFeatureDescr=jnxLicenseFeatureDescr, jnxLicenseFeatureLicenseId=jnxLicenseFeatureLicenseId, jnxLicenseFeatureLicenseUsed=jnxLicenseFeatureLicenseUsed, jnxLicenseFeatureLicenseInstalled=jnxLicenseFeatureLicenseInstalled, jnxLicenseFeatureLicenseNeeded=jnxLicenseFeatureLicenseNeeded, jnxLicenseSettings=jnxLicenseSettings, jnxLicenseRenewBeforExpiration=jnxLicenseRenewBeforExpiration, jnxLicenseRenewInterval=jnxLicenseRenewInterval, jnxLicenseAutoUpdate=jnxLicenseAutoUpdate)

# Notifications
mibBuilder.exportSymbols("JUNIPER-LICENSE-MIB", jnxLicenseGraceExpired=jnxLicenseGraceExpired, jnxLicenseGraceAboutToExpire=jnxLicenseGraceAboutToExpire, jnxLicenseAboutToExpire=jnxLicenseAboutToExpire, jnxLicenseInfringeCumulative=jnxLicenseInfringeCumulative, jnxLicenseInfringeSingle=jnxLicenseInfringeSingle)
