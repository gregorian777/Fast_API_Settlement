from sqlalchemy import Table, Column, Integer, String, Numeric, Date
from sqlalchemy.sql import func

from app.database import metadata

# This is an example of a table definition from the Automations
# process lookup table. This informs the ORM on how to interact with
# the table.
PROCESS_LK = Table(
    "PROCESS_LK",
    metadata,
    Column("PROCESS_ID", Integer, nullable=False),
    Column("PROCESS_NAME", String(100), nullable=False),
    Column("PROJECT", String(100)),
    Column("STATUS_ID", Integer),
    Column("JIRA_ID", String(20)),
    Column("OUTAGE_ID", Integer, nullable=False),
    Column("OUTAGE_COMMS", String(1)),
    Column("AUTOMATOR_ID", Integer),
)

# As a bonus, here's an example of a table definition from CRM
ENQUIRIES = Table(
    "ENQUIRIES",
    metadata,
    Column('MPANCORE', String(13), nullable=True),
    Column('RAISED_BY', String(30), nullable=True),
    Column('DATE_RAISED', Date, nullable=True),
    Column('CONTACT_TYPE', Numeric(30, 0), nullable=True),
    Column('REQUEST_TYPE', Numeric(30, 0), nullable=True),
    Column('DUE_DATE', Date, nullable=True),
    Column('COMMENTS_1', String(4000), nullable=True),
    Column('COMMENTS_2', String(4000), nullable=True),
    Column('RESOLVED', String(1), nullable=True),
    Column('RESOLVED_COMMENTS', String(4000), nullable=True),
    Column('RESOLVED_BY', String(30), nullable=True),
    Column('DATE_RESOLVED', Date, nullable=True),
    Column('OWNER', String(30), nullable=True),
    Column('ACTUAL_DATE_RAISED', Date, nullable=True),
    Column('TIMED_OUT', String(1), nullable=True),
    Column('CUSTOMER_ID', Numeric, nullable=True),
    Column('SITE_ID', Numeric, nullable=True),
    Column('RECORD_ID', Numeric, nullable=True),
    Column('SYSTEM_ROLE', String(1), nullable=True),
    Column('EXPIRY_CODE', String(1), nullable=True),
    schema="ENQUIRY",
)

SETTLEMENT = Table(
    "SETTLEMENT_PROCESS",
    metadata,
    Column("SETTLEMENT_ID", Integer, primary_key=True, nullable=False),
    Column("DEBT_ID", Integer),
    Column("AGREEMENT_ID", Integer, nullable=False),
    Column("CUSTOMER_ID", Integer, nullable=False),
    Column("FINAL_BILL_PRINTED_DATE", Date),
    Column("PERIOD_FROM", Date),
    Column("DT_LETTER_ID", Integer),
    Column("LETTER_REF", String(10)),
    Column("LETTER_DATE_PRINTED", Date),
    Column("LETTER_DATE_SENT", Date),
    Column("ACCOUNT_STATUS", String(20)),
    Column("ACCOUNT_TYPE", String(20)),
    Column("OUTSTANDING_BALANCE", Numeric),
    Column("EMAIL", String(200)),
    Column("MOBILE_NUMBER", String(40)),
    Column("NO_FORWARDING_ADDRESS", String(10)),
    Column("NO_BANK_DETAILS", String(10)),
    Column("REFUND_REQUESTED", String(10)),
    Column("LAST_UPDATED_DATE", Date),
    Column("LAST_UPDATED_BY", String(50)),
    Column("DATE_ADDED", Date, server_default=func.sysdate()),
    schema="CBT",
)

SETTLEMENT_TRANSACTION_LOG = Table(
    "SETTLEMENT_TRANSACTION_LOG",
    metadata,
    Column("TRANSACTION_ID", Integer, primary_key=True, nullable=False),
    Column("SETTLEMENT_ID", Integer),
    Column("AGREEMENT_ID", Integer),
    Column("TRANSACTION_TYPE", String(20)),
    Column("TRANSACTION_TYPE_ID", Integer),
    Column("REASON_TYPE", String(20)),
    Column("ORIGINAL_BALANCE", Numeric),
    Column("DEDUCTION_PERCENTAGE", Numeric),
    Column("TRANSACTION_AMOUNT", Numeric),
    Column("NEW_BALANCE", Numeric),
    Column("TRANSACTION_DATE", Date, server_default=func.sysdate()),
    schema="CBT",
)