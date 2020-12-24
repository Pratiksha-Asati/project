from django.shortcuts import render
from .forms import CustomerForm
# Create your views here.
def customerModelFormMethod(request):
    # if(request.method=="POST"):
    #     frm=CustomerForm(request.POST)
    frm = CustomerForm()
    context = {'form':frm}
    return  render(request,'customerForm.html',context)