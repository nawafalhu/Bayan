from django.db import models
from django.contrib.auth.models import User

class dictionary(models.Model):
    pass

class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    video_file = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title

class QuizScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chapter = models.IntegerField()
    score = models.IntegerField()
    total_questions = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'chapter')

    def __str__(self):
        return f"{self.user.username} - Chapter {self.chapter} - {self.score}/{self.total_questions}"

class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chapter = models.IntegerField()
    lesson = models.IntegerField()
    completed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'chapter', 'lesson')
        ordering = ['chapter', 'lesson']

    def __str__(self):
        return f"{self.user.username} - Chapter {self.chapter}, Lesson {self.lesson}"

class ContactMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.user.username}: {self.subject}"

    class Meta:
        ordering = ['-created_at']
