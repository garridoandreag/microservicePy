import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Account(BaseModel):
    accountNumber: str
    firstName: str
    lastName: str

app = FastAPI(title="Accounts Microservice")

APP_VERSION = os.getenv("APP_VERSION", "v1")

accounts = [
    Account(accountNumber="1001", firstName="Andrea", lastName="Gomez"),
    Account(accountNumber="1002", firstName="Carlos", lastName="Ramirez"),
    Account(accountNumber="1003", firstName="Maria", lastName="Lopez"),
]

@app.get("/accounts", response_model=list[Account])
def get_accounts() -> list[Account]:
    return accounts

@app.get("/accounts/{account_number}", response_model=Account)
def get_account_by_number(account_number: str) -> Account:
    account = next((item for item in accounts if item.accountNumber == account_number), None)

    if account is None:
        raise HTTPException(status_code=404, detail="Account not found")

    return account

@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "OK", "version": APP_VERSION}

@app.get("/version")
def version() -> dict[str, str]:
    return {"version": APP_VERSION}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)