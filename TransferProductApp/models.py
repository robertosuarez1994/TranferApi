from django.db import models

# Create your models here.

class Product (models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return(self.name)


class BranchOffice (models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return(self.name)

class Stock (models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    branchOffice = models.ForeignKey(BranchOffice,on_delete=models.CASCADE)
    stock = models.IntegerField(null=True)

    def __str__(self):
        s = str(self.product.name)+'_'+self.branchOffice.name;
        return(s)

    


