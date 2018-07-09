from django.shortcuts import render
from khayyam import JalaliDate
from datetime import timedelta
from Zanbil.models import Services, Sans, Reserves, Review, Business
from Zanbil.views import user
from .db import cur
import sys


class ServicePageController:
    def Render(request, service_id):
        date = JalaliDate.today().__str__().replace('-', '/')

        today = date
        weekday = JalaliDate.today().weekday()
        cur.execute("SELeCT * from services join timetable on (services.timetable_id=timetable.id)   where services.id = %s ",(str(service_id)))
        service = cur.fetchall()
        cur.execute("SELeCT * from users  where   users.id in( select owner_id from business where business.id =  %s) ",(str(service[0]['business_id'])))
        owner  = cur.fetchall()
        cur.execute(
            "Select * from  sans where weekday = %s and id not in  (SELECT sans_id from reserves where date  like  %s  and service_id = %s ) ",(str(weekday), str(today), str(service_id)))

        sanses = cur.fetchall

        return render(request, 'ServicePage.html',
                      {'service': service[0], 'days': sanses, 'date': date,
                       'user': user,'owner':owner})

    def RenderTimeTable(request):
        if request.method == 'POST':
            service_id = int(request.POST.get('service'))
            try:
                timetable_id = request.POST.get('time_table', '')

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

                today = date
                weekday = day.weekday()
                # service = Services.objects.get(id=service_id)
                cur.execute(
                    "SELeCT * from services join timetable on (services.timetable_id=timetable.id)   where services.id = %s ",
                    (str(service_id)))
                service = cur.fetchall()

                cur.execute(
                    "SELeCT * from users  where   users.id in( select owner_id from business where business.id =  %s) ",
                    (str(service[0]['business_id'])))
                owner = cur.fetchall()
                timetable_id = str(service[0]['timetable_id'])
                # selected_sanses = Sans.objects.filter(time_table__id=service.timetable.id).order_by('start_time')
                cur.execute("SELECT * from sans where time_table_id = %s ", (timetable_id))

                cur.execute(
                    "Select * from  sans where weekday = %s and id not in  (SELECT sans_id from reserves where date  like  %s  and service_id = %s ) ",
                    (str(weekday), str(today), str(service_id)))

                sanses = cur.fetchall

                return render(request, 'ServicePage.html',
                              {'service': service[0], 'days': sanses, 'date': date,
                               'user': user, 'owner': owner[0]})
            except:
                date = JalaliDate.today().__str__().replace('-', '/')

                today = date
                weekday = JalaliDate.today().weekday()
                cur.execute(
                    "SELeCT * from services join timetable on (services.timetable_id=timetable.id)   where services.id = %s ",
                    (str(service_id)))
                service = cur.fetchall()
                cur.execute(
                    "SELeCT * from users  where   users.id in( select owner_id from business where business.id =  %s) ",
                    (str(service[0]['business_id'])))
                owner = cur.fetchall()
                cur.execute(
                    "Select * from  sans where weekday = %s and id not in  (SELECT sans_id from reserves where date  like  %s  and service_id = %s ) ",
                    (str(weekday), str(today), str(service_id)))

                sanses = cur.fetchall

                return render(request, 'ServicePage.html',
                              {'service': service[0], 'days': sanses, 'date': date,
                               'user': user, 'owner': owner})

    def Book(request):
        if (request.method == 'POST'):
            date = str(request.POST.get('date', ''))
            sans_id = request.POST.get('sans_id', '')
            description = request.POST.get('description', '')
            service_id = request.POST.get('service_id', '')
            day = request.POST.get('day','')
            date_splited = date.split('/')
            try:
                if(int(date_splited[1])>12):
                    hazard =True

                if(0<int(date_splited[1])<=6 and int(date_splited[0])>30 ):
                    hazard =True

                if( 6< int(date_splited[1])<12 and int(date_splited[0])>30 ):
                    hazard =True

                if(int(date_splited[1]) == 12 and int(date_splited[0])==30 ):
                    hazard =True
                saturday = JalaliDate(int(date_splited[0]), int(date_splited[1]), int(date_splited[2]))
                targetday = saturday + timedelta(days=int(day))
                targetday=targetday.__str__().replace('-','/')

                if(date.__contains__("INSERT") or date.__contains__("DELETE") or date.__contains__("AND") or date.__contains__(";") or date.__contains__("DROP") or date.__contains__("'") or date.__contains__("=") or date.__contains__(")") or date.__contains__("$") or date.__contains__("&")):
                    raise Exception

                cur.execute("INSERT INTO reserves( description, date, user_id, sans_id, service_id) VALUES (%s,%s,%s,%s,%s)",(str(description),str(day),str(user.id),str(sans_id),str(service_id)))
                cur.execute(
                    "select * from business join categories on (categories.id = business.category_id) where owner_id=" + str(user.id))

                mybusiness = cur.fetchall()
                cur.execute("select * from  reserves  join  services on (services.id = reserves.service_id) join business on (business.id = services.business_id) join sans on (sans.id = reserves.sans_id) where user_id  = %s",(str(user.id)))

                history = cur.fetchall()
                return render(request, 'AccountPage.html',
                              {'user': user, 'historys': history, 'mybusiness': mybusiness })
            except  Exception as e:
                ServicePageController.Render(request, service_id)
class SansContext:
    def __init__(self,sans,reserved):
        self.sansdata = sans
        self.is_reserved = reserved
    def __str__(self):
        return (str(self.sans) + str(self.is_reserved))

