from django.db import models

class LoginChatSignup(models.Model):
    id = models.AutoField(primary_key=True)  # Adjust fields to match table
    username = models.CharField(max_length=100)

    class Meta:
        db_table = 'login_chat_signup'
        managed = False  # Tells Django not to create or modify this table

class LeaveForm(models.Model):
    user = models.ForeignKey(LoginChatSignup, on_delete=models.CASCADE)
    reason = models.TextField()
    Address=models.CharField(max_length=200)
    City = models.CharField(max_length=50)
    State=models.CharField(max_length=30)
    Zipcode=models.CharField(max_length=6)
    Room_number=models.IntegerField(unique=True)
    enrollment_number=models.CharField(max_length=12)
    submitted_on = models.DateTimeField(auto_now_add=True)
    Parents_contact_number=models.CharField(max_length=10)
    Destination = models.CharField(max_length=60)
    Leave_From_date=models.DateField(auto_now_add=False)
    Leave_to_date=models.DateField(auto_now_add=False)
    
    def __str__(self):
        return f"{self.user.username}'s leave"
