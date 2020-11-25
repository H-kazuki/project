from django.shortcuts import render, redirect
from .forms import SinUpForm


def user_accounts(request):
	if (request.method == 'POST'):
		sinup = SinUpForm(request.POST)
		if sinup.is_valid():
			sinup.save()
			return redirect(to = '/accountstop')

	params = {
		'title': 'NewAccount',
		'form': SinUpForm()
	}
	return render(request, 'accounts/new_accounts.html', params)