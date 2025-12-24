import secrets
import oracledb
ORACLE_DB_USER="JAROSINSKIG"
ORACLE_DB_PASSWORD="JAROSINSKIG"
# ORACLE_DB_DSN="(description= (retry_count=20)(retry_delay=3)(address=(protocol=tcps)(port=1521)(host=adb.uk-london-1.oraclecloud.com))(connect_data=(service_name=g9d4a44f81b78d1_gdjsk2aaqow7bn0i_high.adb.oraclecloud.com))(security=(ssl_server_dn_match=yes)))"
# ORACLE_DB_DSN ="(DESCRIPTION=(ADDRESS = (PROTOCOL = TCP)(HOST = UGL-ODB-001-DEV.UGL.LOCAL)(PORT = 1521))(CONNECT_DATA = (SERVER = DEDICATED) (SERVICE_NAME = DEVCRM.UGL.LOCAL)))"
ORACLE_DB_DSN = "(DESCRIPTION = (ADDRESS = (PROTOCOL = TCP)(HOST = dev-dbhost.nonprd.oci.cloud.local)(PORT = 1521))(CONNECT_DATA = (SERVER = DEDICATED)(SERVICE_NAME = DEVCRM.UGL.LOCAL)))"

connection = oracledb.connect(user=ORACLE_DB_USER, password=ORACLE_DB_PASSWORD, dsn=ORACLE_DB_DSN)

print(connection.version)

print(secrets.token_hex(32))