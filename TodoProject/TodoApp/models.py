from django.db import models

"""
Todo Application:
 - Create an item in the todo list
- Read the complete todo list
- Update the items with status as "Not Started", "In Progress", or "Complete"
- Delete the items from the list
"""


STATUS_CHOICES = (
    ("Not-Started", "Not Started"),
    ("In-Progress", "In Progress"),
    ("Complete", "Complete")
)


class Todo(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=12)

