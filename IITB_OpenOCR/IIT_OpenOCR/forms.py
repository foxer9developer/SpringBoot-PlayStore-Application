from django import forms
from .models import sets, users, book


class setsform(forms.ModelForm):

    class Meta:
        model = sets
        fields = "__all__"

class bookform(forms.ModelForm):
    class Meta:
        model = book
        fields = "__all__"

class newsetsform(forms.ModelForm):
    class Meta:
        model = sets
        fields = ['setID', 'number', 'bookid', 'status', 'projectmanager', 'repoistoryName', 'vone_deadline']

class AddUserForm(forms.ModelForm):
    class Meta:
        model = users
        fields = ['github_username', 'user_role', 'name', 'user_email']