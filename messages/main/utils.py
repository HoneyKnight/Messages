from django.shortcuts import redirect, render


def form_edit(request, model, form, redirect_url):
    if not form.is_valid():
        context = {
            'model': model,
            'form': form,
        }
        return render(request, 'main/edit_message.html', context)
    form.save
    return redirect(redirect_url)
