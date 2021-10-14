class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']