from django.test import TestCase

# Create your tests here.
# In Django shell or a custom script
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# Create test users
user1 = User.objects.create_user('admin', 'admin@example.com', 'password123')
user2 = User.objects.create_user('editor', 'editor@example.com', 'password123')
user3 = User.objects.create_user('viewer', 'viewer@example.com', 'password123')

# Assign users to groups
admins_group = Group.objects.get(name='Admins')
editors_group = Group.objects.get(name='Editors')
viewers_group = Group.objects.get(name='Viewers')

user1.groups.add(admins_group)
user2.groups.add(editors_group)
user3.groups.add(viewers_group)
