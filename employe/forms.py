from django import forms

from .models import Employe

class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = ['first_name', 'last_name', 'birthday', 'fonction', 'photo']

    def clean(self):
        super().clean()
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        birthday = self.cleaned_data.get("birthday")
        fonction = self.cleaned_data.get("fonction")
        photo = self.cleaned_data.get("photo")

        if not first_name:
            self.add_error(first_name, "Nom ne doit pas etre vide.")
        if not last_name:
            self.add_error(last_name, "Last ne doit pas etre vide.")
        if not birthday:
            self.add_error(birthday, "Birthday ne doit pas etre vide.")
        if not fonction:
            self.add_error(fonction, "Fonction ne doit pas etre vide.")
