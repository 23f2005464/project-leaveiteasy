from django.db import models

class Chat_signup(models.Model):
    username = models.CharField(max_length=120, unique=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128)
    date_joined = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=120, default="user")

    def __str__(self):
        return self.username

    class Meta:
        app_label = 'login'


class LeaveForm(models.Model):
   #  username = models.ForeignKey(Chat_signup, on_delete=models.CASCADE)
    name =models.CharField(max_length=50,default="null")
    reason = models.TextField()
    Address = models.CharField(max_length=200)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=30)
    Zipcode = models.CharField(max_length=6)
    Room_number = models.IntegerField(unique=True)
    enrollment_number = models.CharField(max_length=12)
    submitted_on = models.DateTimeField(auto_now_add=True)
    Parents_contact_number = models.CharField(max_length=10)
    Destination = models.CharField(max_length=60)
    Leave_From_date = models.DateField()
    Leave_to_date = models.DateField()

    def __str__(self):
        return f"{self.user.username}'s leave"
