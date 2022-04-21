from rest_framework import serializers
from ..models import *

# The class used to control how a Exercise is serialized to JSON. Derives/inherits from the default ModelSerializer


class ExerciseSerializer(serializers.ModelSerializer):

    class Meta:

        # The class type we want it to serialize
        model = Exercise

        # Which fields to serialize to JSON. __all__ means all fields.
        # We can be specific with the fields too, e.g.
        # fields = ('id', 'title', 'image')
        fields = ('__all__')


# The class used to control how a Level is serialized to JSON. Derives/inherits from the default ModelSerializer
class LevelSerializer(serializers.ModelSerializer):

    class Meta:

        # The class type we want it to serialize
        model = Level

        # Which fields to serialize to JSON. __all__ means all fields.
        # We can be specific with the fields too, e.g.
        # fields = ('id', 'name')
        fields = ('__all__')


# The class used to control how a Muscle is serialized to JSON. Derives/inherits from the default ModelSerializer
class MuscleSerializer(serializers.ModelSerializer):

    class Meta:

        # The class type we want it to serialize
        model = Muscle

        # Which fields to serialize to JSON. __all__ means all fields.
        # We can be specific with the fields too, e.g.
        # fields = ('id', 'name')
        fields = ('__all__')


# Nested serializer derives from/inherits the ExerciseSerializer. Has extra serializers for nested objects
class PopulatedExerciseSerializer(ExerciseSerializer):

    # When a 'level' property is found on the object it will use this serializer
    level = LevelSerializer()

    # When a 'muscles' property is found on the object it will use this serializer
    muscles = MuscleSerializer(many=True)


class ExerciseWithMusclesSerializer(ExerciseSerializer):

    muscles = MuscleSerializer(many=True)


class PopulatedLevelSerializer(LevelSerializer):

    exercises = ExerciseWithMusclesSerializer(many=True)
