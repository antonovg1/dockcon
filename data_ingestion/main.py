from fastapi import FastAPI, UploadFile, File, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from models import DataEntry, Base
import pandas as pd
import asyncio

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API is running!"}

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...), db: AsyncSession = Depends(get_db)):
    # ???????? ?? ??????? ??????
    if file.content_type not in ["text/csv", "application/vnd.ms-excel", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"]:
        raise HTTPException(status_code=400, detail="????????? ??????, ??????????? CSV ??? Excel")

    # ?????? ?? ?????
    try:
        contents = await file.read()
        if file.filename.endswith(".csv"):
            df = pd.read_csv(pd.io.common.BytesIO(contents))
        else:
            df = pd.read_excel(pd.io.common.BytesIO(contents))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"?????? ??? ?????? ?? ?????: {e}")

    # ???????? ?? ???????????? ??????
    required_columns = {"name", "age", "email"}
    if not required_columns.issubset(df.columns):
        raise HTTPException(status_code=400, detail=f"??????? ???????????? ??????: {required_columns - set(df.columns)}")

    # ????????? ?? ??????? ? ??????
    entries = [DataEntry(name=row["name"], age=row["age"], email=row["email"]) for _, row in df.iterrows()]
    
    async with db.begin():
        db.add_all(entries)
    
    return {"status": "?????? ? ????????? ???????!"}
