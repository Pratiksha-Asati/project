from django.http import  HttpResponse
def index(request):
    return HttpResponse("""<h1>Add Customer<h2>
    <form action="addCustomer/" method="GET">
        Customer id<input type"txtId" name"id"><br />
        Name<input type"txtName" name"name" ><br />
        Address<input type"txtAdd" name"name" ><br />
        Moblie No<input type"txtMob" name"name ><br />
        <input type="submit" value="AddCustomer" />


    </form>
""")
def index2(request):
    return HttpResponse("""<h1>Customer added succesfully</h1>"
    <form action="" method="GET">
                        <input type="submit" value="Back" />
                        </form>""")
