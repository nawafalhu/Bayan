from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django import forms

@login_required
def home(request):
    return render(request, 'main/home.html')

@login_required
def sign_practice(request):
    return render(request, 'main/sign_practice.html')

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove all help_texts
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['username'].help_text = None
        
        # Customize labels
        self.fields['username'].label = 'Username'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm Password'

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'main/signup.html', {'form': form})

def get_lesson_title(chapter, lesson):
    lessons = {
        1: {
            1: "Alphabet Signs",
            2: "Numbers Signs",
            3: "Greetings Signs"
        },
        2: {
            1: "Common Phrases",
            2: "Family Members",
            3: "Weather Terms"
        },
        3: {
            1: "Emotions & Feelings",
            2: "Time & Calendar",
            3: "Colors & Objects"
        },
        4: {
            1: "Complex Sentences",
            2: "Questions & Answers",
            3: "Story Telling"
        }
    }
    return lessons.get(chapter, {}).get(lesson, "Lesson Not Found")

def lesson_view(request, chapter, lesson):
    lesson_title = get_lesson_title(chapter, lesson)
    return render(request, 'main/lesson.html', {
        'chapter': chapter,
        'lesson': lesson,
        'lesson_title': lesson_title
    })

@login_required
def quiz(request):
    return render(request, 'main/quiz.html')

@login_required
def quiz_start(request, chapter):
    return render(request, 'main/quiz_start.html', {'chapter': chapter})
