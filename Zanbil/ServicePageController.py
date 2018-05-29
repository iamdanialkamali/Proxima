from django.shortcuts import render
from khayyam import JalaliDate

from Zanbil.models import Services, Sans, Reserves, Review, Business
from Zanbil.views import user


class ServicePageController:
    def Render(request, service_id):
        date = JalaliDate.today().__str__().replace('-', '/')
        day_name = JalaliDate().today().weekdayname()
        service = Services.objects.get(id=service_id)
        selected_sanses = Sans.objects.filter(time_table__id=service.timetable.id,
                                              weekday=JalaliDate.today().weekday()).order_by('start_time')
        print(date.split())
        reserved = Reserves.objects.filter(date__contains=date)
        reserved = [e.sans for e in reserved]
        #print(reserved)
        selected_sanses = [sans for sans in selected_sanses]
        final = set(selected_sanses).difference(set(reserved))
        #print(final)
        reviews = Review.objects.filter(service_id=service.id)
        return render(request, 'ServicePage.html',
                      {'service': service, 'sanses': final, 'day_name': day_name, 'reviews': reviews, 'date': date,
                       'user': user})

    def RenderTimeTable(request):
        if request.method == 'POST':
            timetable_id = request.POST.get('time_table', '')
            service_id = int(request.POST.get('service'))
            date = request.POST.get('date', '')
            date_splited = date.split('/')
            day = JalaliDate(int(date_splited[0]), int(date_splited[1]), int(date_splited[2]))
            service = Services.objects.get(id=service_id)
            selected_sanses = Sans.objects.filter(time_table__id=timetable_id, weekday=day.weekday())
            print(date.split())
            reserved = Reserves.objects.filter(date=date)
            reserved = [e.sans for e in reserved]
            print(reserved)
            selected_sanses = [sans for sans in selected_sanses]
            if (JalaliDate.today() <= day):
                final = set(selected_sanses).difference(set(reserved))
            else:
                date = JalaliDate.today().__str__().replace('-', '/')
                day = JalaliDate().today()
                final = []
            reviews = Review.objects.filter(service_id=service.id)
            return render(request, 'ServicePage.html',
                          {'service': service, 'sanses': final, 'day_name': day.weekdayname(), 'reviews': reviews,
                           'date': date, 'user': user})

    def Book(request):
        if (request.method == 'POST'):
            date = request.POST.get('date', '')
            sans_id = request.POST.get('sans_id', '')
            description = request.POST.get('description', '')
            service = Services.objects.get(id=request.POST.get('service_id', ''))
            sans = Sans.objects.get(pk=sans_id)
            check_obj = Reserves.objects.filter(date=date, service_id=service.id, sans=sans)
            if (len(check_obj) == 0):
                Reserves.objects.create(user=user, sans=sans, date=date, description=description, service_id=service.id)
                mybusiness = Business.objects.filter(id=service.business.id)
                history = Reserves.objects.filter(user_id=user.id).order_by('date')
                return render(request, 'AccountPage.html',
                              {'user': user, 'historys': history, 'mybusiness': mybusiness})
            else:
                return ServicePageController.Render(request,service.id)


