import jdatetime
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.views.generic import ListView
from persiantools.jdatetime import JalaliDate

from member_app.forms import MemberForm
from member_app.models import Member


class IndexMember(ListView):
    model = Member
    template_name = 'index.html'
    context_object_name = 'members'
    paginate_by = 10

    def get_queryset(self):
        search = self.request.search
        Member.objects.filter(
            Q(first_name__contains=search)
            | Q(last_name__contains=search)
            | Q(nation_code__contains=search)
            | Q(phone__contains=search)
        ).order_by('-register_at')


@require_POST
def save_member(req):

    data = req.POST or None
    data['birthday'] = JalaliDate(data['year'], data['month'], data['day']).to_gregorian()

    member_form = MemberForm(data)
    if member_form.is_valid():
        data_valid = member_form.cleaned_data
        member = Member(data)
        member.save()
    else:
        return render(req, 'member_app/create.html', {'form': member_form})
    return HttpResponseRedirect(reverse('member_app:index'))
