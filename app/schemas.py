from pydantic import BaseModel

class MaterialRequest(BaseModel):
    semester: str
    course: str
    topic: str
    content: str

class MaterialResponse(BaseModel):
    message: str
