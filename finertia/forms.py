from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FinancialForm(forms.Form):
    annual_income = forms.FloatField(label='Annual Income')
    birthday_count = forms.IntegerField(label='Birthday Count')
    employed_days = forms.IntegerField(label='Employed Days')
    mobile_phone = forms.BooleanField(label='Mobile Phone', required=False)
    work_phone = forms.BooleanField(label='Work Phone', required=False)
    phone = forms.BooleanField(label='Phone', required=False)
    email_id = forms.BooleanField(label='Email ID', required=False)
    family_members = forms.IntegerField(label='Family Members')
    total_amount = forms.FloatField(label='Total Amount')
    mean_amount = forms.FloatField(label='Mean Amount')
    std_amount = forms.FloatField(label='Std Amount')
    productive_ratio = forms.FloatField(label='Productive Ratio')
    gender_f = forms.BooleanField(label='Female', required=False)
    car_owner_y = forms.BooleanField(label='Car Owner', required=False)
    propert_owner_y = forms.BooleanField(label='Property Owner', required=False)
    type_income = forms.ChoiceField(label='Type of Income', choices=[
        ('Commercial associate', 'Commercial associate'),
        ('Pensioner', 'Pensioner'),
        ('State servant', 'State servant'),
        ('Student', 'Student')
    ])
    education = forms.ChoiceField(label='Education', choices=[
        ('Higher education', 'Higher education'),
        ('Incomplete higher', 'Incomplete higher'),
        ('Secondary / secondary special', 'Secondary / secondary special')
    ])
    marital_status = forms.ChoiceField(label='Marital Status', choices=[
        ('Married', 'Married'),
        ('Single / not married', 'Single / not married'),
        ('Widow / Widower', 'Widow / Widower')
    ])
    housing_type = forms.ChoiceField(label='Housing Type', choices=[
        ('House / apartment', 'House / apartment'),
        ('Municipal apartment', 'Municipal apartment'),
        ('Office apartment', 'Office apartment')
    ])
    type_occupation = forms.ChoiceField(label='Type of Occupation', choices=[
        ('Management', 'Management'),
        ('Laborers', 'Laborers'),
        ('Private service staff', 'Private service staff'),
        ('Sales staff', 'Sales staff')
    ])
    cibil_score = forms.IntegerField(label='CIBIL Score')
    bank_assets_value = forms.FloatField(label='Bank Assets Value')


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    mobile_number = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'mobile_number', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.mobile_number = self.cleaned_data['mobile_number']
        if commit:
            user.save()
        return user