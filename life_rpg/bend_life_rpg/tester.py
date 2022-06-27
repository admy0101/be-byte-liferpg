from bend_life_rpg.models import User
from bend_life_rpg.serializers import UserSerializer
from rest_framework.renderers import JSONRenderer

user = User(username='aloush')
user.save()

serializer = UserSerializer(user)
serializer.data


# content = JSONRenderer().render(serializer.data)
# content