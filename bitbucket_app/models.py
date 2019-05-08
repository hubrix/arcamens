from django.utils.translation import ugettext_lazy as _
from core_app.models import Event
from django.db import models

class BitbucketHook(models.Model):
    """
    """

    organization = models.ForeignKey('core_app.Organization', null=False, on_delete=models.CASCADE,
    related_name='bitbucket_hooks')

    full_name = models.CharField(null=True, 
    help_text='Example: team/repo_name',
    blank=False, default='', max_length=626)

class EBitbucketCommit(Event):
    # Not sure if i should have abitbuckethooker 
    # foreignkey here. The user actor will
    # be the bitbucket addon.
    # We need to add commit_id too, for updating
    # in case the commit is deleted(not sure yet though).
    hook = models.ForeignKey('BitbucketHook', null=True, on_delete=models.SET_NULL)

    url = models.CharField(null=True, blank=False, 
    max_length=626)

    note = models.OneToOneField('note_app.Note', null=True, on_delete=models.SET_NULL,
    related_name='bitbucket_commits')

    html_template = 'bitbucket_app/e-bitbucket-commit.html'










