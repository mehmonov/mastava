from django import forms 

class SearchForm(forms.Form):
    search_text =  forms.CharField(
                    required = False,
                    label='Sizga qanday kitob kerak? ',
                    widget=forms.TextInput(attrs={'placeholder': 'Masalan: O\'tkan kunlar!','class':"   "})
                  )
    
    

  