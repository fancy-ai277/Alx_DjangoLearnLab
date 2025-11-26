from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Check if user is a Member
def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Member view restricted to Member users
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
