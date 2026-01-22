from data.storage import save_material
from app.models import StudyMaterial

def organize_material(semester, course, topic, content):
    material = StudyMaterial(semester, course, topic, content)
    save_material(material)
    return f"Material saved under {semester} → {course} → {topic}"
