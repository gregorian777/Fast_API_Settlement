from fastapi import FastAPI, HTTPException, Depends, status, Path
from typing import Annotated, List
from sqlalchemy import text
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import Process, AuditLogStartIn, Settlement, CustomerIdOut, AgreementIdOut, SettlementTransaction
from app.crud import (
    basic_select,
    get_processes,
    get_process,
    audit_log_start,
    get_settlement_by_agreement,
    get_settlement_by_customer,
    get_settlement_all,
    get_settlement_by_settlement,
    get_transaction_by_settlement
)
from app.database import Session, get_db

DESCRIPTION =Path(__file__).resolve().parent/ "README.md"
DESCRIPTION = DESCRIPTION.read_text(encoding="utf-8") 

app = FastAPI(title = "Settlement Process API",
              version ="0.1.0",
              description = DESCRIPTION,
              redoc_url="/redoc"
              )

orgins= ["*"]

app.add_middleware(
  CORSMiddleware,
  allow_origins=orgins,
  allow_credentials=True,
  allow_methods = ["*"],
  allow_headers = ["*"]
)

# The "Depends" wrapper is used to ensure the session is available
# to all endpoints.

db_dependency = Annotated[Session, Depends(get_db)]

@app.get('/process', response_model=List[Process])
async def get_all_processes(database: db_dependency):
    """Retrieve all processes."""
    results = await get_processes(database)
    return results


@app.get('/process/{process_id}', response_model=Process)
async def get_process_from_id(database: db_dependency, process_id: int):
    """Retrieve a single process by its ID."""
    process = await get_process(database, process_id)
    if process is None:
        raise HTTPException(status_code=404, detail="Process not found")
    return process


@app.post("/audit_log/start", status_code=202)
async def start_audit_log(database: db_dependency, body: AuditLogStartIn):
    """Starts a new audit log for a process."""
    await audit_log_start(
        database,
        process_id=body.process_id,
        queued=body.queued,
        completed=body.completed,
    )
    return {"message": "Audit log start successful."}

@app.get("/health")
async def health(database: db_dependency):
    try:
        await basic_select(database)
        return {"message": "Still alive."}
    except Exception:
        raise HTTPException(status_code=503, detail="Database connection is not healthy")
    
@app.get("/settlements/by_agreement/{agreement_id}", status_code= status.HTTP_200_OK, response_model= Settlement)
async def get_sett_by_agr_id(database: db_dependency, agreement_id: int = Path(gt=0)):
    settlement = await get_settlement_by_agreement(database, agreement_id)
    if settlement is None:
        raise HTTPException(status_code=404, detail="Settlement not found")
    return settlement


@app.get("/settlements/by_customer_id/{customer_id}", status_code= status.HTTP_200_OK, response_model= Settlement)
async def get_sett_by_cust_id(database: db_dependency, customer_id: int = Path(gt=0)):
    settlement = await get_settlement_by_customer(database, customer_id)
    if settlement is None:
        raise HTTPException(status_code=404, detail="Settlement not found")
    return settlement


@app.get("/settlements/by_settlement_id/{settlement_id}", status_code= status.HTTP_200_OK, response_model= Settlement)
async def get_sett_by_sett_id(database: db_dependency, settlement_id: int = Path(gt=0)):
    settlement = await get_settlement_by_settlement(database, settlement_id)
    if settlement is None:
        raise HTTPException(status_code=404, detail="Settlement not found")
    return settlement

@app.get("/settlements/customers", status_code= status.HTTP_200_OK, response_model = List[CustomerIdOut])
async def get_sett_all_cust(database: db_dependency):
    settlement = await get_settlement_all(database)
    if settlement is None:
        raise HTTPException(status_code=404, detail="Settlement not found")
    return [
        CustomerIdOut(customer_id = s.CUSTOMER_ID)
            for s in settlement 
            ]

@app.get("/settlements/agreements", status_code= status.HTTP_200_OK, response_model = List[AgreementIdOut])
async def get_sett_all_agr(database: db_dependency):
    settlement = await get_settlement_all(database)
    if settlement is None:
        raise HTTPException(status_code=404, detail="Settlement not found")
    return [
        AgreementIdOut(agreement_id = s.AGREEMENT_ID)
            for s in settlement 
            ]
    
@app.get("/settlements/transactions/{settlement_id}", status_code= status.HTTP_200_OK, response_model= List[SettlementTransaction])
async def get_trans_by_sett_id(database: db_dependency, settlement_id: int = Path(gt=0)):
    transaction = await get_transaction_by_settlement(database, settlement_id)
    if transaction is None:
        raise HTTPException(status_code=404, detail="Settlement not found")
    return transaction