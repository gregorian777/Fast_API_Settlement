from pydantic import BaseModel
from datetime import date
from decimal import Decimal

# This creates a Pydantic model for a process API response, which is
# used to validate the data returned from the database.
class Process(BaseModel):
    """Schema for a process."""
    PROCESS_ID: int
    PROCESS_NAME: str
    PROJECT: str | None
    STATUS_ID: int | None

    class Config:
        # This allows Pydantic to read data from ORM models
        # For Pydantic v1, this was "orm_mode = True"
        from_attributes = True
        
class Settlement(BaseModel):
    """Schema for a settlement process."""
    SETTLEMENT_ID: int
    DEBT_ID: int | None = None
    AGREEMENT_ID: int
    CUSTOMER_ID: int | None = None
    FINAL_BILL_PRINTED_DATE: date | None = None
    PERIOD_FROM: date | None = None
    DT_LETTER_ID: int | None = None
    LETTER_REF: str | None = None
    LETTER_DATE_PRINTED: date | None = None
    LETTER_DATE_SENT: date | None = None
    ACCOUNT_STATUS: str | None = None
    ACCOUNT_TYPE: str | None = None
    OUTSTANDING_BALANCE: Decimal | None = None
    EMAIL: str | None = None
    MOBILE_NUMBER: str | None = None
    NO_FORWARDING_ADDRESS: str | None = None
    NO_BANK_DETAILS: str | None = None
    REFUND_REQUESTED: str | None = None
    LAST_UPDATED_DATE: date | None = None
    LAST_UPDATED_BY: str | None = None
    DATE_ADDED: date | None = None
    
    class Config:
        from_attributes = True
        
class SettlementTransaction(BaseModel):
    """Schema for a settlement transaction log entry."""
    TRANSACTION_ID: int
    SETTLEMENT_ID: int | None = None
    AGREEMENT_ID: int | None = None
    TRANSACTION_TYPE: str | None = None
    TRANSACTION_TYPE_ID: int | None = None
    REASON_TYPE: str | None = None
    ORIGINAL_BALANCE: Decimal | None = None
    DEDUCTION_PERCENTAGE: Decimal | None = None
    TRANSACTION_AMOUNT: Decimal | None = None
    NEW_BALANCE: Decimal | None = None
    TRANSACTION_DATE: date | None = None

    class Config:
        from_attributes = True

class CustomerIdOut(BaseModel):
    customer_id: int | None = None
    
class AgreementIdOut(BaseModel):
    agreement_id: int | None = None
    
# This creates a Pydantic model for the request body to start an
# audit log. This enables FastAPI to validate the request body and
# will provide type hints and validation in the swagger docs.
class AuditLogStartIn(BaseModel):
    """Schema for the request body to start an audit log."""
    process_id: int
    queued: int
    completed: int

class SettlementTransaction(BaseModel):
    """Schema for a settlement transaction log entry."""
    TRANSACTION_ID: int
    SETTLEMENT_ID: int | None = None
    AGREEMENT_ID: int | None = None
    TRANSACTION_TYPE: str | None = None
    TRANSACTION_TYPE_ID: int | None = None
    REASON_TYPE: str | None = None
    ORIGINAL_BALANCE: Decimal | None = None
    DEDUCTION_PERCENTAGE: Decimal | None = None
    TRANSACTION_AMOUNT: Decimal | None = None
    NEW_BALANCE: Decimal | None = None
    TRANSACTION_DATE: date | None = None

    class Config:
        from_attributes = True
