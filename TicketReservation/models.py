from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Ticket(models.Model):
    arabian_visitor = 'Arabian_Visitor'
    arabian_student = 'Arabian_Student'
    foreign_visitor = 'Foreing_Visitor'
    foreign_student = 'Foreing_Student'
    photography = 'Photography'   
    ticket_types = [
        (arabian_visitor,'Arabian_Visitor'),
        (arabian_student,'Arabian_Student'),
        (foreign_visitor,'Foreign_Visitor'),
        (foreign_student,'Foreign_Student'),
        (photography,'Photography'),
    ]

    ticket_type =  models.CharField(max_length=20,choices=ticket_types)
    price = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return self.ticket_type 


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank=1)
    phone = PhoneNumberField(blank=1)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=1)
    def name(self):
        return self.first_name + " " + self.last_name
    
 
class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='tickets',null=1)
    ticket = models.ForeignKey(Ticket,on_delete=models.CASCADE,related_name='ticket')
    amount = models.PositiveSmallIntegerField()


