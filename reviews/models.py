from django.db import models
from django.contrib.auth import get_user_model
from exercises.models import Exercise
User = get_user_model()


class Review(models.Model):

    text = models.TextField(max_length=300)
    owner = models.ForeignKey(
        User, related_name="reviews", on_delete=models.CASCADE)
    exercise = models.ForeignKey(
        Exercise, related_name="reviews", on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    # The below updates the date of the user's review when they edit it.
    # updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.exercise} {self.exercise.level.name} review written by {self.owner} is: {self.text} written at {self.created_date}"
