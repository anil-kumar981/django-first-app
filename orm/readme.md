# ORM in Django

## What is ORM?
**ORM (Object-Relational Mapping)** is a technique that allows developers to interact with a database using Python objects instead of writing raw SQL queries. In Django, ORM maps database tables to Python classes (models) and rows to objects.

---

## ORM Working Flow
1. Define a model (Python class).
2. Django ORM converts it into a database table.
3. Perform operations using Python code (CRUD).
4. ORM translates these operations into SQL queries.
5. Database executes SQL and returns results.
6. ORM converts results back into Python objects.

---

## Real Life Example

### Define Model
```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    
create query
Student.objects.create(name="Harsh", age=22)

retrieve Data
students = Student.objects.all()

update data
student = Student.objects.get(id=1)
student.age = 23
student.save()

delete data
student.delete()
```
