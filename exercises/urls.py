from django.urls import path
from .views import *

urlpatterns = [

    # Generic views for exercises
    path('exercises/', ExerciseList.as_view()),

    # Wire up the view - <int:pk> is known as a captured value - it works the same as a placeholder in react/express: ":id"
    # It's made up of two parts:
    # On the left is the path converter - in this case we've specified an integer or "int"
    # On the right is the placeholder - in this case pk but could be anything
    # The path converter is optional, but you should use it to ensure it's the type you expect
    # Without it, the captured value would be written like: <pk>
    path('exercises/<int:pk>/', ExerciseUpdateDestroy.as_view()),

    # We can't have the same route as above for details too so we need to change the url
    # Only 1 view per route allowed - some classes can have multiple route handlers in them though as you can see with the class-based routes below
    path('exercises/detail/<int:pk>/', ExerciseDetail.as_view()),

    # Class-based views for levels
    path('levels/', LevelListCreate.as_view()),
    path('levels/<int:pk>/', LevelRetrieveUpdateDelete.as_view()),

]
