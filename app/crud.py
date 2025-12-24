from app.models import PROCESS_LK, SETTLEMENT,SETTLEMENT_TRANSACTION_LOG
from sqlalchemy import text

from app.database import Session

async def basic_select(database: Session):
    """This basic select confirms that the session is live."""
    query = text("SELECT * FROM DUAL")
    return database.execute(query)

async def get_processes(database: Session):
    """This queries all processes from the database."""
    # This uses the process table model to create a query.
    # The .all() method returns all rows.
    processes = database.query(PROCESS_LK).all()
    return processes

async def get_process(database: Session, process_id: int):
    """This queries a single process by its ID."""
    # This also uses the process table model; however, we're using the
    # .filter_by() method to specify the primary key.
    process = database.query(PROCESS_LK).filter_by(
        PROCESS_ID=process_id
    ).first()
    return process

async def get_settlement_by_agreement(database : Session, agreement_id:int):
    agreement_model = database.query(SETTLEMENT).filter_by(AGREEMENT_ID=agreement_id).first()
    return agreement_model

async def get_settlement_by_customer(database: Session, customer_id: int):
    customer_model = database.query(SETTLEMENT).filter_by(CUSTOMER_ID=customer_id).first()
    return customer_model

async def get_settlement_all(database: Session):
    settlement_model = database.query(SETTLEMENT).all()
    return settlement_model

async def get_settlement_by_settlement(database: Session, settlement_id: int):
    customer_model = database.query(SETTLEMENT).filter_by(SETTLEMENT_ID=settlement_id).first()
    return customer_model

async def get_transaction_by_settlement(database: Session, settlement_id: int):
    transaction_model = database.query(SETTLEMENT_TRANSACTION_LOG).filter_by(SETTLEMENT_ID=settlement_id).all()
    return transaction_model

async def audit_log_start(database: Session, process_id: int, queued: int, completed: int):
    """This calls a stored procedure to log the start of an audit"""
    # Define the statement to call the stored procedure.
    # Use named parameters (:name) for clarity and security.
    statement = text("CALL automationpro.PR_PROCESS_AUDIT_LOG_START(:p_process_id, :p_queued, :p_completed)")

    # Bind the IN parameters.
    statement = statement.bindparams(
        p_process_id=process_id,
        p_queued=queued,
        p_completed=completed,
    )

    # Run the procedure
    database.execute(statement)

    # Commit the changes
    database.commit()
