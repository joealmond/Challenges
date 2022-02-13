from turtle import forward
from urllib import response
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

import challenges

monthly_challenges = {
    "january": "january text",
    "february": "february text",
    "march": "march text",
    "april": "april text",
    "may": "may text"
}


# Create your views here.

# def index(request):
#     months = list(monthly_challenges.keys())
#     monthsItem = []
#     for x in range(0, len(months)):
#         monthsItem.append(
#             f"<li><a href='/challenges/{x+1}'>{months[x]}<a/></li>")
#     return HttpResponse(monthsItem)

def index(request):
    months = list(monthly_challenges.keys())
    list_items = ""
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}<a/></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month!")

    redirect_month = months[month - 1]
    redirect_path = reverse(
        "month-challenge", args=[redirect_month])  # /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
