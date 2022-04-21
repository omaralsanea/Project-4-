from django.db import models

# Create your models here.

# Defines an level model which Django will set up in the database for us


class Level(models.Model):

    # Text field with a maximum length, validation is automatically handled
    name = models.CharField(max_length=100)

    # Function to define how we want an level to look in the admin area, when converting the object to a string
    def __str__(self):
        return self.name


# Defines a Muscle model which Django will set up in the database for us
class Muscle(models.Model):

    # Text field with a maximum length, validation is automatically handled
    name = models.CharField(max_length=30)

    # Function to define how we want a Muscle to look in the admin area, when converting the object to a string
    def __str__(self):
        return self.name


# Defines a Exercise model which Django will set up in the database for us
class Exercise(models.Model):

    # Text field with a maximum length, validation is automatically handled
    title = models.CharField(max_length=50)

    # A one-to-many relationship (one level can have many exercises, a exercise belongs to one level)
    # - related_name value allows us to customise what the relationship looks like from the level object perspective (i.e. the level has 'exercises')
    # - on_delete value defines how we want Django to manage a situation where the level is deleted. Options are:
    #   - models.CASCADE - Delete all exercises belonging to the level
    #   - models.PROTECT - Do not allow a level to be deleted if they have exercises
    #   - models.SET_NULL - Set the level field in the exercise table to NULL which effectively means the exercise no longer has an level (requires null=True on the relationship)
    # Creates a foreign key column in our 'exercises_exercise' table referencing level_id
    level = models.ForeignKey(
        Level, related_name='exercises', on_delete=models.CASCADE, null=True)

    # Text field with a maximum length
    # - blank=True means that we allow empty values to be set here
    image = models.CharField(max_length=200, blank=True)

    # Date field that allows nulls
    ##### release_date = models.DateField(null=True)

    # A many-to-many relationship (An exercise can belong to many Muscles, a Muscle can apply to many exercises)
    # Note: A many-to-many relationship can be defined in either model
    # - related_name value allows us to customise what the relationship looks like from the Muscle perspective (i.e. a Muscle has 'exercises')
    # - blank=True means we allow empty values to be set here (an exercise doesn't need to have a Muscle)
    muscles = models.ManyToManyField(
        Muscle, related_name='exercises', blank=True)

    description = models.CharField(max_length=200, blank=True)

    # Function to define how we want an Exercise to look in the admin area, when converting the object to a string
    def __str__(self):
        return self.title
