from django.urls import reverse_lazy
from django.views.generic import FormView

from relaxy_taxi.main.forms import CallbackForm


class HomePageView(FormView):
    template_name = "pages/home.html"
    form_class = CallbackForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        user = self.request.user
        form.save(user=user)
        return super().form_valid(form)
