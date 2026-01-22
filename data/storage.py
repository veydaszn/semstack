DATABASE = []

def save_material(material):
    DATABASE.append({
        "semester": material.semester,
        "course": material.course,
        "topic": material.topic,
        "content": material.content
    })
