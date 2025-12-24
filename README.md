# Settlement Process API Documentation

**Version:** `0.1.0`

---

## Introduction
The **Settlement Process API** provides endpoints to manage debt settlement processes and automation tasks. It allows authorized applications to:

- Retrieve process information
- Manage settlements
- View transaction logs
- Monitor service health

Built with **FastAPI** and backed by an **Oracle database** for robust performance.

---

## Table of Contents
- [Introduction](#introduction)
- [Authentication](#authentication)
- [API Endpoints](#api-endpoints)
  - [Health](#health)
  - [Processes](#processes)
  - [Settlements](#settlements)
  - [Audit Log](#audit-log)
- [Example Requests](#example-requests)
- [Future Enhancements](#future-enhancements)

---

## Authentication
> **Note:** Authentication is not yet implemented. This section will be updated once security measures are in place.

---

## API Endpoints

### Health
#### `GET /health`
- **Description:** Performs a health check on the database connection.
- **Success Response (200 OK):**
```json
{ "status": "Service is operational" }
```
- **Error Response (503 Service Unavailable):**
```json
{ "error": "Database connection failed" }
```

### Processes
#### `GET /process`
- Retrieves all automation processes.

#### `GET /process/{process_id}`
- Retrieves a single process by ID.
- **Path Parameter:** `process_id` *(integer, required)*

### Settlements
#### `GET /settlements/by_agreement/{agreement_id}`
- Retrieves settlement by `AGREEMENT_ID`.

#### `GET /settlements/by_customer_id/{customer_id}`
- Retrieves settlement by `CUSTOMER_ID`.

#### `GET /settlements/by_settlement_id/{settlement_id}`
- Retrieves settlement by `SETTLEMENT_ID`.

#### `GET /settlements/customers`
- Retrieves all unique `CUSTOMER_ID`s.

#### `GET /settlements/agreements`
- Retrieves all unique `AGREEMENT_ID`s.

#### `GET /settlements/transactions/{settlement_id}`
- Retrieves all transaction logs for a given settlement.

### Audit Log
#### `POST /audit_log/start`
- Starts a new audit log for a process.
- **Request Body:**
```json
{
  "process_id": 1,
  "queued_count": 10,
  "completed_count": 0
}
```

---

## Example Requests

### Health Check
```bash
curl -X GET "http://localhost:8000/health"
```

### Get All Processes
```bash
curl -X GET "http://localhost:8000/process"
```

### Get Process by ID
```bash
curl -X GET "http://localhost:8000/process/1"
```

### Get Settlement by Agreement ID
```bash
curl -X GET "http://localhost:8000/settlements/by_agreement/123"
```

### Start Audit Log
```bash
curl -X POST "http://localhost:8000/audit_log/start" -H "Content-Type: application/json" -d '{"process_id":1,"queued_count":10,"completed_count":0}'
```

---

## Future Enhancements
- Implement authentication and authorization.
- Add pagination for large datasets.
- Include detailed error codes and troubleshooting steps.

