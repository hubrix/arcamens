from django.conf import settings
from core_app.views import GuardianView
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from github_app.models import GithubHook, EGithubCommit
from core_app.models import User, Membership
from card_app.models import Card
from note_app.models import Note
from . import forms
from re import findall
import json
import sys

COMMIT_FMT =  (
  '### Github Commit\n'
  '##### Author: {author}\n'
  '##### Commit: [{url}]({url})\n' 
  '##### Message: {message}\n'
)

class Authenticator(GuardianView):
    def post(self, request):
        pass

@method_decorator(csrf_exempt, name='dispatch')
class GithubHandle(View):
    def post(self, request):
        encoding = request.encoding if request.encoding \
        else settings.DEFAULT_CHARSET 

        data      = json.loads(request.body.decode(encoding))
        full_name = data['repository']['full_name']

        for ind in data['commits']:
            self.create_refs(full_name, ind)

        return HttpResponse(status=200)

    def create_refs(self, full_name, commit):
        print('Data:', full_name, file=sys.stderr)

        REGX  ='card_app/card-link/([0-9]+)'
        ids   = findall(REGX, commit['message'])
        cards = Card.objects.filter(id__in = ids)

        # Filter cards whose organization has a github hook
        # whose address is the one in the push payload.
        # Note: Not sure if there is a better way.
        # cards = cards.filter(
            # ancestor__ancestor__organization__github_hooks__full_name=full_name)

        # First grab the hooks.
        hooks = GithubHook.objects.filter(full_name=full_name)
        organizations = hooks.values_list('organization')
    
        # Check if the card organizations are in the hook organizations.
        is_ok = Q(ancestor__ancestor__organization__in=organizations)

        # Just create events for cards which have a hook 
        # mapping to the repository.
        cards = cards.filter(is_ok)

        data  = COMMIT_FMT.format(author=commit['author']['name'],
        message=commit['message'], url=commit['url'])

        for ind in cards:
            self.create_note(ind, data, commit['url'])

    def create_note(self, card, data, url):
        bitbot, _ = User.objects.get_or_create(
        email=settings.GITHUB_BOT_EMAIL, name=settings.GITHUB_BOT_NAME)

        note  = Note.objects.create(card=card, data=data, owner=bitbot)
        event = EGithubCommit.objects.create(
        organization=card.ancestor.ancestor.organization, 
        note=note, url=url, user=bitbot)

        # All the board members get aware of the event.
        event.dispatch(*card.workers.all(), 
            *card.ancestor.ancestor.members.all())

        event.save()

class ListGithubHooks(GuardianView):
    def get(self, request):
        user = User.objects.get(id=self.user_id)
        hooks = user.default.github_hooks.all()

        return render(request, 'github_app/list-github-hooks.html', 
        {'user': user, 'hooks': hooks})

class DeleteGithubHook(GuardianView):
    def get(self, request, hook_id):
        membership = Membership.objects.get(
            user=self.me, organization=self.me.default)

        ERROR0 = "Only staffs can do that!"
        if membership.status != '0':
            return HttpResponse(ERROR0, status=403)


        hook = GithubHook.objects.get(id=hook_id)
        hook.delete()

        return redirect('github_app:list-github-hooks')

class CreateGithubHook(GuardianView):
    def get(self, request):
        form = forms.GithubHookForm()

        return render(request, 'github_app/create-github-hook.html', 
        {'form':form, 'user': self.me})

    def post(self, request):
        membership = Membership.objects.get(
            user=self.me, organization=self.me.default)

        ERROR0 = "Only staffs can do that!"
        if membership.status != '0':
            return HttpResponse(ERROR0, status=403)

        form = forms.GithubHookForm(request.POST)

        if not form.is_valid():
            return render(request, 
                'github_app/create-github-hook.html', 
                    {'form':form, 'user': self.me})

        record = form.save(commit=False)
        record.organization = self.me.default
        record.save()
        return redirect('github_app:list-github-hooks')





