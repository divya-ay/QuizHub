from django.contrib import admin

from .models import (
    Category,
    Quiz,
    Question,
    Choice,
    Tag,
    QuizAttempt,
    UserAnswer,
    UserStreak,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "is_active",
        "created_at",
    )

    search_fields = ("name",)

    list_filter = ("is_active",)


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "difficulty",
        "passing_score",
        "time_limit",
        "is_active",
        "created_at",
    )

    search_fields = (
        "title",
        "description",
    )

    list_filter = (
        "category",
        "difficulty",
        "is_active",
    )

    ordering = ("title",)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "short_text",
        "quiz",
        "points",
        "created_at",
    )

    search_fields = ("text",)

    list_filter = ("quiz",)

    def short_text(self, obj):
        return obj.text[:50]

    short_text.short_description = "Question"


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = (
        "text",
        "question",
        "is_correct",
    )

    search_fields = ("text",)

    list_filter = (
        "question",
        "is_correct",
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
    )

    search_fields = (
        "name",
        "slug",
    )


@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = (
        "quiz",
        "user",
        "score",
        "passed",
        "started_at",
        "completed_at",
    )

    search_fields = (
        "quiz__title",
        "user__username",
    )

    list_filter = (
        "quiz",
        "passed",
        "started_at",
    )


@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = (
        "attempt",
        "question",
        "selected_choice",
        "answered_at",
    )

    search_fields = (
        "question__text",
        "attempt__user__username",
    )

    list_filter = (
        "answered_at",
    )


@admin.register(UserStreak)
class UserStreakAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "current_streak",
        "longest_streak",
        "last_activity_date",
    )

    search_fields = (
        "user__username",
    )