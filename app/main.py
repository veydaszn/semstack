from fastapi import FastAPI
from app.schemas import MaterialRequest, MaterialResponse
from app.organizer import organize_material

app = FastAPI(
    title="SemStack API",
    description="Semester-based learning material organizer",
    version="1.0"
)

@app.post("/add", response_model=MaterialResponse)
def add_material(request: MaterialRequest):
    organized = organize_material(
        semester=request.semester,
        course=request.course,
        topic=request.topic,
        content=request.content
    )
    return MaterialResponse(message=organized)
