from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

# Create your models here.
class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        db_index=True,
        help_text="Category_name"
    )
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    
class Quiz(models.Model):
    title = models.CharField(
        max_length=200
    )

    description = models.TextField(blank=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='quizzes'
    )

    difficulty = models.CharField(
        max_length=20,
        choices=[
            ('easy', 'Easy'),
            ('medium', 'Medium'),
            ('hard', 'Hard'),
        ],
        default='easy'
    )

    passing_score = models.PositiveIntegerField(
        default=50,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )

    time_limit = models.PositiveIntegerField(
        default=10,
        validators=[MinValueValidator(1)],
        help_text="Time limit in minutes"
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']

        constraints = [
            models.UniqueConstraint(
                fields=['title', 'category'],
                name='unique_quiz_title_per_category'
            ),

            models.CheckConstraint(
                check=models.Q(time_limit__gte=1),
                name='time_limit_gte_1'
            ),
        ]

    def clean(self):
        if self.time_limit > 180:
            raise ValidationError(
                "Quiz time limit cannot exceed 180 minutes."
            )

    def __str__(self):
        return self.title
    
class Question(models.Model):
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name='questions'
    )

    text = models.TextField()

    points = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1)]
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(points__gte=1),
                name='question_points_gte_1'
            )
        ]

    def __str__(self):
        return self.text[:50]
    
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)
    quizzes = models.ManyToManyField(Quiz, related_name='tags')

    def __str__(self):
        return self.name
    

class Choice(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='choices'
    )

    text = models.CharField(max_length=255)

    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
    
class QuizAttempt(models.Model):
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name='attempts'
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='quiz_attempts'
    )

    score = models.PositiveIntegerField(default=0)

    passed = models.BooleanField(default=False)

    started_at = models.DateTimeField(auto_now_add=True)

    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.quiz.title} - {self.score}"
    

class UserAnswer(models.Model):
    attempt = models.ForeignKey(
        QuizAttempt,
        on_delete=models.CASCADE,
        related_name='answers'
    )

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )

    selected_choice = models.ForeignKey(
        Choice,
        on_delete=models.CASCADE
    )

    answered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.attempt.user.username} - {self.question.id}"
    
class UserStreak(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='streaks'
    )

    current_streak = models.PositiveIntegerField(default=0)

    longest_streak = models.PositiveIntegerField(default=0)

    last_activity_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - Current Streak: {self.current_streak} - Longest Streak: {self.longest_streak}"