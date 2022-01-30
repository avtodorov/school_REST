from rest_framework import routers, serializers, viewsets
from school_app.models import Student, Group


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', ]


class StudentDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'age', ]


class StudentNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', ]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['group_name', ]


class GroupDetailsSerializer(serializers.HyperlinkedModelSerializer):
    students = StudentNestedSerializer(read_only=True, many=True)

    class Meta:
        model = Group
        fields = ['group_name', 'students', ]
