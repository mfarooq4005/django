from django import forms
class userForms(forms.Form):
    num1=forms.CharField(label="Enter Your Name", required="False")
    num2=forms.CharField(label="Enter Your Father Name")
class calculator(forms.Form):
    value2=forms.IntegerField(label="Enter First Value")
    value1=forms.IntegerField(label="Enter Second Value")
    #operator=forms.SlugField(label="Enter Operator", required=False)
class evenod(forms.Form):
    evenodd=forms.IntegerField(label="Enter Value")
class sheet(forms.Form):
    maths=forms.IntegerField(label="Math", max_value=75)
    eng=forms.IntegerField(label="English", max_value=75)
    urdu=forms.IntegerField(label="Urdu", max_value=75)
    biy=forms.IntegerField(label="Biology", max_value=60)
    phy=forms.IntegerField(label="Physics", max_value=60)
    chy=forms.IntegerField(label="chemistry", max_value=60)
    ist=forms.IntegerField(label="Islamiat", max_value=50)
    ps=forms.IntegerField(label="Pak Studies", max_value=50)