from django.db import models

# Create your models here.
class Skill(models.Model):
    skill_name = models.CharField(max_length=80)

    def __str__(self):
        return self.skill_name
    
class Stack(models.Model):
    skill_type = models.ForeignKey(Skill, on_delete=models.CASCADE)
    technology = models.CharField(max_length=50)
    icon_class = models.CharField(max_length=80)

    def __str__(self):
        return self.technology
    
class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=150)
    location = models.CharField(max_length=100, blank=True, null=True)
    start_year = models.CharField(max_length=10)
    end_year = models.CharField(max_length=10)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.degree} - {self.institution}"



class Experience(models.Model):
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=150)
    location = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.CharField(max_length=20)
    end_date = models.CharField(max_length=20)
    description = models.TextField(help_text="Use new lines for bullet points.")

    def __str__(self):
        return f"{self.position} at {self.company}"


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    github_link = models.URLField(blank=True, null=True)
    live_demo = models.URLField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Resume(models.Model):
    title = models.CharField(max_length=100, default="My Resume")
    file = models.FileField(upload_to='resumes/')

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title