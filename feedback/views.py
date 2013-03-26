from django.shortcuts import get_object_or_404


def accept_feedback_api(request, campaign_slug):
    if request.method == 'POST' and request.is_xhr== True:
        campaign = Campaign.get_object_or_404(Campaign, campaign_slug))
        new_feedback= 

