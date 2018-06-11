from django.shortcuts import render
from khayyam import JalaliDate
from datetime import timedelta
from Zanbil.models import Services, Sans, Reserves, Review, Business
from Zanbil.views import user


class ServicePageController:
    def Render(request, service_id):
        date = JalaliDate.today().__str__().replace('-', '/')
        week_start_date = JalaliDate.today()-timedelta(days=JalaliDate.today().weekday())
        weekday_date=week_start_date
        this_week_days = []
        for i in range(7):
            weekday_date.__str__().replace('-','/')
            this_week_days.append(weekday_date.__str__().replace('-','/'))
            weekday_date = weekday_date + timedelta(1)
        service = Services.objects.get(id=service_id)
        selected_sanses = Sans.objects.filter(time_table__id=service.timetable.id).order_by('start_time')
        sanses = [[],[],[],[],[],[],[]]
        reserved_sanses = Reserves.objects.filter(date__in=this_week_days)
        #print(reserved_sanses)
        #reserved_sanses = [e.sans for e in reserved_sanses]
       # print(reserved_sanses)
        for sans in selected_sanses:
            is_reserved=False
            for reserved in reserved_sanses:
                if(sans.id==reserved.sans.id):
                    is_reserved=True
            sanses[sans.weekday].append(SansContext(sans,is_reserved))

        #print(sanses)


        return render(request, 'ServicePage.html',
                      {'service': service, 'days': sanses, 'date': date,
                       'user': user})

    def RenderTimeTable(request):
        if request.method == 'POST':
            timetable_id = request.POST.get('time_table', '')
            service_id = int(request.POST.get('service'))
            date = request.POST.get('date', '')
            date_splited = date.split('/')
            day = JalaliDate(int(date_splited[0]), int(date_splited[1]), int(date_splited[2]))
            week_start_date = day - timedelta(days=JalaliDate.today().weekday())
            weekday_date = week_start_date
            this_week_days = []
            for i in range(7):
                weekday_date.__str__().replace('-', '/')
                this_week_days.append(weekday_date.__str__().replace('-', '/'))
                weekday_date = weekday_date + timedelta(1)
            service = Services.objects.get(id=service_id)
            selected_sanses = Sans.objects.filter(time_table__id=service.timetable.id).order_by('start_time')
            sanses = [[], [], [], [], [], [], []]
            reserved_sanses = Reserves.objects.filter(date__in=this_week_days)
            print(reserved_sanses)
            # reserved_sanses = [e.sans for e in reserved_sanses]
            # print(reserved_sanses)
            for sans in selected_sanses:
                is_reserved = False
                for reserved in reserved_sanses:
                    if (sans.id == reserved.sans.id):
                        is_reserved = True
                sanses[sans.weekday].append(SansContext(sans, is_reserved))

            print(sanses)

            return render(request, 'ServicePage.html',
                          {'service': service, 'days': sanses, 'date': date,
                           'user': user})

            selected_sanses = [sans for sans in selected_sanses]
            if (JalaliDate.today() <= day):
                final = set(selected_sanses).difference(set(reserved))
            else:
                date = JalaliDate.today().__str__().replace('-', '/')
                day = JalaliDate().today()
                final = []
            return render(request, 'ServicePage.html',
                          {'service': service, 'sanses': final, 'day_name': day.weekdayname(),
                           'date': date, 'user': user})

    def Book(request):
        if (request.method == 'POST'):
            date = request.POST.get('date', '')
            sans_id = request.POST.get('sans_id', '')
            description = request.POST.get('description', '')
            service = Services.objects.get(id=request.POST.get('service_id', ''))
            day = request.POST.get('day','')
            date_splited = date.split('/')
            saturday = JalaliDate(int(date_splited[0]), int(date_splited[1]), int(date_splited[2]))
            targetday = saturday + timedelta(days=int(day))
            targetday=targetday.__str__().replace('-','/')
            print(targetday)
            sans = Sans.objects.get(pk=sans_id)
            check_obj = Reserves.objects.filter(date=targetday, service_id=service.id,sans_id=sans_id)
            print(check_obj)
            if (len(check_obj) == 0):
                Reserves.objects.create(user=user, sans=sans, date=targetday, description=description, service_id=service.id)
                mybusiness = Business.objects.filter(id=service.business.id)
                history = Reserves.objects.filter(user_id=user.id).order_by('date')
                return render(request, 'AccountPage.html',
                              {'user': user, 'historys': history, 'mybusiness': mybusiness})
            else:
                return ServicePageController.Render(request,service.id)

class SansContext:
    def __init__(self,sans,reserved):
        self.sansdata = sans
        self.is_reserved = reserved
    def __str__(self):
        return (str(self.sans) + str(self.is_reserved))

