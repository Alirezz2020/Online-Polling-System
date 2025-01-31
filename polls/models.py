from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class Poll(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='polls')
    question = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    duration = models.PositiveIntegerField(
        help_text="Duration in minutes (e.g., 120 for 2 hours)",
        default=60  # Default duration: 1 hour
    )

    def get_absolute_url(self):
        # This URL is used as the share link for voting.
        return reverse('polls:poll_detail', kwargs={'pk': self.pk})



    def get_end_time(self):
        """Calculate when the poll should expire based on duration."""
        return self.created_at + timezone.timedelta(minutes=self.duration)

    def has_expired(self):
        """Return True if the poll duration has passed."""
        return timezone.now() > self.get_end_time()

    def __str__(self):
        return self.question


class Answer(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class Vote(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='votes')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='votes')
    # For registered voters, you can link to the User. Allowing null for anonymous votes.
    voter = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    voted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('poll', 'voter')  # This prevents duplicate votes for the same poll by the same user

    def __str__(self):
        return f"Vote by {self.voter} on {self.poll}"
