
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PollForm, AnswerFormSet
from django.views import View
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Poll, Answer, Vote




class DashboardView(LoginRequiredMixin, ListView):
    model = Poll
    template_name = 'polls/dashboard.html'
    context_object_name = 'polls'

    def get_queryset(self):
        return Poll.objects.filter(creator=self.request.user).order_by('-created_at')


# Create a new poll along with its answers.
class PollCreateView(LoginRequiredMixin, CreateView):
    model = Poll
    form_class = PollForm
    template_name = 'polls/poll_form.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['answers'] = AnswerFormSet(self.request.POST)
        else:
            data['answers'] = AnswerFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        answers = context['answers']
        # Assign the poll's creator
        form.instance.creator = self.request.user
        self.object = form.save()
        if answers.is_valid():
            answers.instance = self.object
            answers.save()
        else:
            return self.form_invalid(form)
        return super().form_valid(form)


# Update an existing poll and its answers.
class PollUpdateView(LoginRequiredMixin, UpdateView):
    model = Poll
    form_class = PollForm
    template_name = 'polls/poll_form.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['answers'] = AnswerFormSet(self.request.POST, instance=self.object)
        else:
            data['answers'] = AnswerFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        answers = context['answers']
        self.object = form.save()
        if answers.is_valid():
            answers.instance = self.object
            answers.save()
        else:
            return self.form_invalid(form)
        return super().form_valid(form)


# Delete a poll.
class PollDeleteView(LoginRequiredMixin, DeleteView):
    model = Poll
    template_name = 'polls/poll_confirm_delete.html'
    success_url = reverse_lazy('polls:dashboard')


# Display poll details with a share link and voting options.
class PollDetailView(DetailView):
    model = Poll
    template_name = 'polls/poll_detail.html'
    context_object_name = 'poll'



class PollVoteView(View):
    def post(self, request, pk, *args, **kwargs):
        poll = get_object_or_404(Poll, pk=pk)

        # Check if poll is expired
        if poll.has_expired():
            messages.error(request, "This poll has expired and you can no longer vote.")
            return redirect('polls:poll_detail', pk=poll.pk)

        answer_id = request.POST.get('answer')

        # Check if the user has already voted
        if poll.votes.filter(voter=request.user).exists():
            messages.error(request, "You have already voted on this poll.")
            return redirect('polls:poll_detail', pk=poll.pk)

        if answer_id:
            try:
                selected_answer = poll.answers.get(id=answer_id)
                Vote.objects.create(
                    poll=poll,
                    answer=selected_answer,
                    voter=request.user
                )
                messages.success(request, "Your vote has been recorded.")
            except Answer.DoesNotExist:
                messages.error(request, "Invalid answer selected.")
        else:
            messages.error(request, "No answer selected.")

        return redirect('polls:poll_detail', pk=poll.pk)
