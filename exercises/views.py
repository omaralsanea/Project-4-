# status gives us a list of possible response codes
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
# This imports rest_framework's APIView that we'll use to extend to our custom view
from rest_framework.views import APIView
# Response gives us a way of sending a HTTP response to the user making the request, passing back data and other information
from rest_framework.response import Response
# Import this when adding error handling, provides a default response when data is not found
from rest_framework.exceptions import NotFound
from .models import *  # Import all our models as we're using them in these views
# Import all our serializers as we're using them in these views
from .serializers.common import *

# Generic exercise views
# Automates a lot of the API endpoint functionality for you

# List exercises generic view


class ExerciseList(ListAPIView):

    # Handles all exercises
    queryset = Exercise.objects.all()

    # Choose serializer to use
    serializer_class = PopulatedExerciseSerializer

# Update or delete exercises generic view


class ExerciseCreate(CreateAPIView):

    # Handles all exercises
    queryset = Exercise.objects.all()

    # Choose serializer to use
    serializer_class = ExerciseSerializer

# Update or delete exercises generic view


class ExerciseUpdateDestroy(RetrieveUpdateDestroyAPIView):

    # Handles all exercises
    queryset = Exercise.objects.all()

    # Choose serializer to use
    serializer_class = ExerciseSerializer

 # Get Exercise by ID generic view


class ExerciseDetail(RetrieveAPIView):

    # Handles all exercises
    queryset = Exercise.objects.all()

    # Choose serializer to use
    serializer_class = PopulatedExerciseSerializer


# Level class-based views
# More basic, fine-grain control of the API endpoint

# Level list and create class-based view
class LevelListCreate(APIView):

    # List Levels
    def get(self, request):

        # Load all levels from the database
        levels = Level.objects.all()

        # Serialize the levels to JSON by using an LevelSerializer with the many=True flag
        serialized_levels = PopulatedLevelSerializer(levels)

        # Return the serialized levels with a HTTP 200 status code
        return Response(data=serialized_levels.data, status=status.HTTP_200_OK)

    # Create level

    def post(self, request):

        # get the name of the incoming level
        # load all levels with that name from the db
        # if there's a match, return a HTTP_409_CONFLICT response
        # if not, continue

        # Create a new serializer with the incoming new level request data
        level_serializer = LevelSerializer(data=request.data)

        # Check whether the new level is valid
        if level_serializer.is_valid():

            # New level is valid so save it to the database
            level_serializer.save()

            # Data has been saved return a 200 response and the new level record
            return Response(data=level_serializer.data, status=status.HTTP_200_OK)

        # Incoming update is not valid so return a HTTP 400 bad request response
        return Response(data=level_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Level retrieve, update and delete class-based view
class LevelRetrieveUpdateDelete(APIView):

    # Get Level by ID - pk is the primary key, passed through our <int:pk> route in urls.py
    def get(self, request, pk):
        # Call the get_level function which will either get the level or raise a HTTP 404 status code response if not present
        level = self.get_level(pk=pk)

        # Create a new serializer with the current level data - we're only returning one level so we don't need the many=True flag
        serialized_level = LevelSerializer(level)

        # Return the serialized level data and a HTTP 200 response
        return Response(data=serialized_level.data, status=status.HTTP_200_OK)

    # Update Level by ID - pk is the primary key, passed through our <int:pk> route in urls.py

    def put(self, request, pk):

        # Call the get_level function which will either get the level or raise a HTTP 404 status code response if not present
        level_to_update = self.get_level(pk=pk)

        # Create a new serializer with the current level data and apply the changes from the incoming request data (updated level)
        # We specify the key `data` because we aren't adhering to the order of the arguments, same as `pk=pk` and `many=True`
        updated_level = LevelSerializer(level_to_update, data=request.data)

        # Check whether the updates are valid
        if updated_level.is_valid():

            # Updates are valid so save them to the database
            updated_level.save()

            # Data has been saved return a 200 response and the updated data
            return Response(updated_level.data, status=status.HTTP_200_OK)

        # Incoming update is not valid so return a HTTP 400 bad request response
        return Response(data=updated_level.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete level by ID - pk is the primary key, passed through our <int:pk> route in urls.py

    def delete(self, request, pk):

        # Call the get_level function which will either get the level or raise a HTTP 404 status code response if not present
        level_to_delete = self.get_level(pk=pk)

        # Delete the level record
        level_to_delete.delete()

        # Return a successful HTTP 204 response
        return Response(status=status.HTTP_204_NO_CONTENT)

    # This is an internal function that doesn't directly handle incoming requests. It is called by other functions in this class. This avoids repeating the same code in each function to handle a missing level.

    def get_level(self, pk):

        # Use a `try` here so if the code within it throws an exception it will be caught in the `except` block and handled rather than returning a HTTP 500 server error response code
        try:
            # Get the level from the database if it exists. If not, an Level.DoesNotExist error will be raised
            return Level.objects.get(pk=pk)

        # Django Models have a DoesNotExist exception that occurs when a query returns no results
        # Link: https://docs.djangoproject.com/en/4.0/ref/models/class/#model-class-reference
        # Level.DoesNotExist errors are caught and handled here
        except Level.DoesNotExist:

            # Raising a NotFound error will return a HTTP 404 response on the API. Further execution of the code will cease.
            # We'll also pass a custom message on the detail key so the user knows what's wrong
            # NotFound returns a 404 response
            # Link: https://www.django-rest-framework.org/api-guide/exceptions/#notfound
            # Raise and return can both be used inside an exception, but NotFound has to be raised
            # Raising an exception is when you're indicating a specific behaviour or outcome like NotFound
            # Returning an exception is for something generic like Response above
            raise NotFound(detail="Can't find that level")



class ExercisesForMuscle(APIView):

    def get(self, request, pk):
        
        print(f"The muscle ID is: {pk}")

        muscle = Muscle.objects.get(pk=pk)

        exercises_for_muscle = muscle.exercises

        exercises_serializer = ExerciseSerializer(exercises_for_muscle, many=True)

        return Response(data=exercises_serializer.data,status=200)