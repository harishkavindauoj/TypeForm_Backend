from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.models import FormData, FormResponse
from app.database import get_db
from bson import ObjectId

router = APIRouter()

@router.post("/form", response_model=FormResponse)
async def create_form(data: FormData, db=Depends(get_db)):
    form_data = data.dict()
    if form_data.get("linkedin_url"):
        form_data["linkedin_url"] = str(form_data["linkedin_url"])
    result = await db.insert_one(form_data)
    new_form = await db.find_one({"_id": result.inserted_id})
    if new_form is None:
        raise HTTPException(status_code=404, detail="Form not found")
    return FormResponse(id=str(new_form["_id"]), **new_form)

@router.get("/forms", response_model=List[FormResponse])
async def read_forms(skip: int = 0, limit: int = 10, db=Depends(get_db)):
    forms = await db.find().skip(skip).limit(limit).to_list(length=limit)
    return [FormResponse(id=str(form["_id"]), **form) for form in forms]

@router.get("/form/{id}", response_model=FormResponse)
async def read_form(id: str, db=Depends(get_db)):
    form = await db.find_one({"_id": ObjectId(id)})
    if form is None:
        raise HTTPException(status_code=404, detail="Form not found")
    return FormResponse(id=str(form["_id"]), **form)

@router.put("/form/{id}", response_model=FormResponse)
async def update_form(id: str, data: FormData, db=Depends(get_db)):
    form_data = data.dict()
    if form_data.get("linkedin_url"):
        form_data["linkedin_url"] = str(form_data["linkedin_url"])
    result = await db.update_one({"_id": ObjectId(id)}, {"$set": form_data})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Form not found or no changes made")
    updated_form = await db.find_one({"_id": ObjectId(id)})
    return FormResponse(id=str(updated_form["_id"]), **updated_form)

@router.delete("/form/{id}", response_model=dict)
async def delete_form(id: str, db=Depends(get_db)):
    result = await db.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Form not found")
    return {"message": "Form deleted successfully"}
