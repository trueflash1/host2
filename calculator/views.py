
from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
# import cgi
from fuzzywuzzy import fuzz

# storage = cgi.FieldStorage()

auth = 1
def index(request):
    if request.method == "GET":
        return render(request, 'login.html')
    if request.method == "POST":
        if request.is_ajax():
            search = request.POST
            s = search.dict()
            search = s['data']
            a = str(search).upper()
            splite = a.split()
            # cursor = connection.cursor()
            global auth
            # if str(splite[0]).split(":")[0] == "AUTH":
            #     data = dict()
            #     for row in cursor.execute('select * from login_table'):
            #         if row[0] == search.split(":")[1] and row[1] == search.split(":")[2]:
            #             auth = 1
            #     print(auth)
            # if str(splite[0]).split(":")[0] == "LOGOUT":
            #     data = dict()
            #     auth = 0
            #     print(auth)
            if str(splite[0]).split(":")[0] == "EDIT" and auth == 1:
                data = edit(search)
            if str(splite[0]).split(":")[0] == "EDITSTRING" and auth == 1:
                data = edit_string(search)
            if str(splite[0]).split(":")[0] == "STRING" and auth == 1:
                data = string(search)
            if str(splite[0]).split(":")[0] == "SEARCHADDTABLE" and auth == 1:
                data = search_add_table(search)
            if str(splite[0]).split(":")[0] == "SEARCHTABLE" and auth == 1:
                data = search_table(search)
            if str(splite[0]).split(":")[0] == "SEARCHALLTABLE" and auth == 1:
                data = search_all_table(search)
            if str(splite[0]).split(":")[0] == "SEARCHINTABLE" and auth == 1:
                data = search_in_table(search)
                print(search)
            if str(splite[0]).split(":")[0] == "SEARCHINTABLEVIEW" and auth == 1:
                data = search_in_table_view(search)
                print(search)
            if str(splite[0]).split(":")[0] == "ADDSTRING" and auth == 1:
                data = addString(search)
            if str(splite[0]).split(":")[0] == "DELETE" and auth == 1:
                data = dell(search)
            if str(splite[0]).split(":")[0] == "CREATETABLE" and auth == 1:
                data = add(search)
            # if str(splite[0]).split(":")[0] == "ADD":
            #     data = add_view(str(splite[0]).split(":")[1])


            q = dict()

            if splite[0] == "HELP" and auth == 1:
                data = replace(":SPRAV_NAME")
            if str(splite[0]).split(":")[0] == "VIEW" and auth == 1:
                data = replace(search)

            if splite[0] == "HELP1" and auth == 1:
                data = edit_view(":SPRAV_NAME")
            if str(splite[0]).split(":")[0] == "EDIT_VIEW" and auth == 1:
                data = edit_view(search)
            if auth == 0:
                data = {"actionButton": "<h2>авторизация не пройдена</h2>"}
            return JsonResponse(data)

def connect(data):
    if data.method == "GET":
        return render(data, 'connect.html')
    if data.method == "POST":
        if data.is_ajax():
            s = 0
    return data
def edit(data):
    if data != None:
        cursor = connection.cursor()
        s = "UPDATE " + str(data.split(":")[1]) + " SET "
        size = len(data.split(":"))-5
        size = int(size)/2
        s += str(data.split(":")[4+int(size)]) + " = '" + str(data.split(":")[4]) + "'"
        print(size)
        for i in range(int(size)-1):
            s += ", " + str(data.split(":")[5+i+int(size)]) + " = '" + str(data.split(":")[5+i]) + "'"
        s += " WHERE " + str(data.split(":")[3]) + " = '" + str(data.split(":")[2]) + "'"
        cursor.execute(s)
        # send = dict()
        send = edit_view(":" + str(data.split(":")[1]))
        print(s)
        print(data)
        return send

def edit_string(data):
    if data != None:
        diction = dict()
        cursor = connection.cursor()
        s = ""
        col = 0
        cursor.execute('select * from ' + data.split(":")[1])
        col_names = [row[0] for row in cursor.description]
        for i in col_names:
            s += "<th>" + str(i) + "</th>"
        s += "<tr>"
        for row in cursor.execute('select * FROM ' + data.split(":")[1].upper()):
            if str(row[0]) == str(data.split(":")[2]):
                dateTable = row[0]
                for i in row:
                    if str(i) == "None":
                        s += "<td><textarea rows=6 id='name" + str(col) + "'></textarea></td>"
                    else:
                        s += "<td><textarea rows=6 id='name" + str(col) + "'  >" + str(i) + "</textarea></td>"
                    col += 1
        s += "</tr>"
        diction.update({"add": s})

        s = "<button class='btn btn-lpbuilder wave-effect' onclick=if(confirm('сохранить?')){vala7('" + str(data.split(":")[1]) + ":" + str(dateTable) + ":" + str(col_names[0]) + "')"
        for i in range(0, col):
            s += ",vala7(document.getElementById('name" + str(i) + "').value)"
        for i in range(0, col):
            s += ",vala7('" + str(col_names[i]) + "')"
        s += ",vala6();}else{event.stopPropagation();event.preventDefault();};>Применить изменения</button>"
        if data.split(":")[int(len(data.split(":"))-1)] == "back":
            s += "<button onclick=vala('EDIT_VIEW:" + str(data.split(":")[1]) + "') class='btn btn-lpbuilder wave-effect'>Назад</button>"
        else:
            s += "<button onclick=vala5('" + str(data.split(":")[int(len(data.split(":"))-1)]) + "') class='btn btn-lpbuilder wave-effect'>Назад</button>"
        diction.update({"addButton": s})
        return diction

def string(data):
    if data != None:
        diction = dict()
        # print(data)
        cursor = connection.cursor()
        s = ""
        col = 0
        cursor.execute('select * from ' + data.split(":")[1])
        col_names = [row[0] for row in cursor.description]
        for i in col_names:
            s += "<th>" + str(i) + "</th>"
        s += "<tr>"
        for row in cursor.execute('select * FROM ' + data.split(":")[1].upper()):
            if str(row[0]) == str(data.split(":")[2]):
                dateTable = row[0]
                for i in row:
                    if str(i) == "None":
                        s += "<td><textarea disabled rows=6 id='name" + str(col) + "' " + "'></textarea></td>"
                    else:
                        s += "<td><textarea disabled rows=6 id='name" + str(col) + "'  >" + str(i) + "</textarea></td>"
                    col += 1
        s += "</tr>"
        diction.update({"add": s})
        s = ""
        if data.split(":")[int(len(data.split(":")) - 1)] == "back":
            s += "<button onclick=vala('VIEW:" + str(
                data.split(":")[1]) + "') class='btn btn-lpbuilder wave-effect'>Назад</button>"
        else:
            s += "<button onclick=vala5('" + str(data.split(":")[int(len(
                data.split(":")) - 1)]) + "') class='btn btn-lpbuilder wave-effect'>Назад</button>"
        diction.update({"addButton": s})
        return diction

def search_add_table(data):
    if data != None:
        s ="<tr><th colspan=3>справочники с таким названием</th></tr><th>название таблицы</th><th>название справочника</th><th>действие</th>"
        diction = dict()
        flag = 0
        tochnost = 0
        cursor = connection.cursor()
        cursor1 = connection.cursor()
        for row in cursor.execute('select * from sprav_name'):
            for i in range(0, len(row)):
                if fuzz.WRatio(str(data.split(":")[1]).replace("_", " "), str(row[i])) > 86 and len(str(data.split(":")[1]).replace("_", " ")) <= len(str(row[i])):
                    flag = 1
                    s += "<tr>"
                    for i in row:
                        s += "<td>" + str(i) + "</td>"
                    s += "<td><button class=edit onclick=vala('EDIT_VIEW:" + row[0] + ":" + data.split(":")[1].replace(" ", "_") + "') >открыть</button></td>"
                    s += "</tr>"
        if flag == 0:
            s = ""
        s += "<tr><th colspan=3>найдены совпадения в следующих справочниках</th></tr>"
        for row1 in cursor.execute('select * from sprav_name'):
            o = 1
            for row2 in cursor1.execute('select * from ' + str(row1[0])):
                for i in range(0, len(row2)):
                    if fuzz.WRatio(str(data.split(":")[1].replace("_", " ")), str(row2[i])) > 86 and len(str(data.split(":")[1]).replace("_", " ")) <= len(str(row2[i])):
                        tochnost = 1
                        if o == 1:
                            s += "<tr><th colspan=2 >название справочника: " + row1[
                                1] + "</th><th><button class=edit onclick=vala('EDIT_VIEW:" + str(row1[0]) + ":" + data.split(":")[1].replace(" ", "_") + "') >открыть</button></th></tr>"
                            o = 0
                        s += "<tr>"
                        s += "<td colspan=2>" + str(row2[i]) + "</td>"
                        s += "<td><button class=edit onclick=vala('EDITSTRING:" + str(row1[0]) + ":" + str(row2[0]) + ":" + data.split(":")[1].replace(" ", "_") + "') >показать</button></td>"
                        s += "</tr>"
        if tochnost == 0:
            for row1 in cursor.execute('select * from sprav_name'):
                o = 1
                for row2 in cursor1.execute('select * from ' + str(row1[0])):
                    for i in range(0, len(row2)):
                        if fuzz.WRatio(str(data.split(":")[1].replace("_", " ")), str(row2[i])) > 85 and len(
                                str(data.split(":")[1]).replace("_", " ")) <= len(str(row2[i])):
                            if o == 1:
                                s += "<tr><th colspan=2 >название справочника: " + row1[
                                    1] + "</th><th><button class=edit onclick=vala('VIEW:" + str(row1[0]) + ":" + \
                                     data.split(":")[1].replace(" ", "_") + "') >открыть</button></th></tr>"
                                o = 0
                            s += "<tr>"
                            s += "<td colspan=2>" + str(row2[i]) + "</td>"
                            s += "<td><button class=edit onclick=vala('STRING:" + str(row1[0]) + ":" + str(
                                row2[0]) + ":" + data.split(":")[1].replace(" ", "_") + "') >показать</button></td>"
                            s += "</tr>"
        diction.update({"add": s})
    return diction

def search_table(data):
    if data != None:
        s ="<tr><th colspan=3>справочники с таким названием</th></tr><th>название таблицы</th><th>название справочника</th><th>действие</th>"
        diction = dict()
        flag = 0
        tochnost = 0
        cursor = connection.cursor()
        cursor1 = connection.cursor()
        for row in cursor.execute('select * from sprav_name'):
            for i in range(0, len(row)):
                if fuzz.WRatio(str(data.split(":")[1]).replace("_", " "), str(row[i])) > 86 and len(str(data.split(":")[1]).replace("_", " ")) <= len(str(row[i])):
                    flag = 1
                    s += "<tr>"
                    for i in row:
                        s += "<td>" + str(i) + "</td>"
                    s += "<td><button class=edit onclick=vala('VIEW:" + row[0] + ":" + data.split(":")[1].replace("_", " ") + "') >открыть</button></td>"
                    s += "</tr>"
        if flag == 0:
            s = ""
        s += "<tr><th colspan=3>найдены совпадения в следующих справочниках</th></tr>"
        for row1 in cursor.execute('select * from sprav_name'):
            o = 1
            for row2 in cursor1.execute('select * from ' + str(row1[0])):
                for i in range(0, len(row2)):
                    if fuzz.WRatio(str(data.split(":")[1].replace("_", " ")), str(row2[i])) > 86 and len(str(data.split(":")[1]).replace("_", " ")) <= len(str(row2[i])):
                        tochnost = 1
                        if o == 1:
                            s += "<tr><th colspan=2 >название справочника: " + row1[
                                1] + "</th><th><button class=edit onclick=vala('VIEW:" + str(row1[0]) + ":" + data.split(":")[1].replace(" ", "_") + "') >открыть</button></th></tr>"
                            o = 0
                        s += "<tr>"
                        s += "<td colspan=2>" + str(row2[i]) + "</td>"
                        s += "<td><button class=edit onclick=vala('STRING:" + str(row1[0]) + ":" + str(row2[0]) + ":" + data.split(":")[1].replace(" ", "_") + "') >показать</button></td>"
                        s += "</tr>"
        if tochnost == 0:
            for row1 in cursor.execute('select * from sprav_name'):
                o = 1
                for row2 in cursor1.execute('select * from ' + str(row1[0])):
                    for i in range(0, len(row2)):
                        if fuzz.WRatio(str(data.split(":")[1].replace("_", " ")), str(row2[i])) > 85 and len(
                                str(data.split(":")[1]).replace("_", " ")) <= len(str(row2[i])):
                            if o == 1:
                                s += "<tr><th colspan=2 >название справочника: " + row1[
                                    1] + "</th><th><button class=edit onclick=vala('VIEW:" + str(row1[0]) + ":" + \
                                     data.split(":")[1].replace(" ", "_") + "') >открыть</button></th></tr>"
                                o = 0
                            s += "<tr>"
                            s += "<td colspan=2>" + str(row2[i]) + "</td>"
                            s += "<td><button class=edit onclick=vala('STRING:" + str(row1[0]) + ":" + str(
                                row2[0]) + ":" + data.split(":")[1].replace(" ", "_") + "') >показать</button></td>"
                            s += "</tr>"
        diction.update({"add": s})
    return diction

def search_in_table_view(data):
    if data != None:
        diction = dict()
        s = ""
        tochnost = 0
        cursor = connection.cursor()
        cursor.execute('select * from ' + data.split(":")[1])
        col_names = [row[0] for row in cursor.description]
        for i in col_names:
            s += "<th>" + str(i) + "</th>"
        for row1 in cursor.execute('select * from ' + str(data.split(":")[1])):
            for i in range(0, len(row1)):
                if fuzz.WRatio(str(data.split(":")[2].replace("_", " ")), str(row1[i])) > 86 and len(
                        str(data.split(":")[2]).replace("_", " ")) <= len(str(row1[i])):
                    s += "<tr>"
                    tochnost = 1
                    for i in range(0, len(row1)):
                        s += "<td>" + str(row1[i]) + "</td>"
        if tochnost == 0:
            for row1 in cursor.execute('select * from ' + str(data.split(":")[1])):
                for i in range(0, len(row1)):
                    if fuzz.WRatio(str(data.split(":")[2].replace("_", " ")), str(row1[i])) > 85 and len(
                            str(data.split(":")[2]).replace("_", " ")) <= len(str(row1[i])):
                        s += "<tr>"
                        for i in range(0, len(row1)):
                            s += "<td>" + str(row1[i]) + "</td>"
        diction.update({"add": s})
        s = "<button class='btn btn-lpbuilder wave-effect' onclick=vala('VIEW:" + str(data.split(":")[1]) + "')>Назад</button>"
        diction.update({"actionButton": s})
    return diction

def search_in_table(data):
    if data != None:
        diction = dict()
        s = ""
        tochnost = 0
        cursor = connection.cursor()
        cursor.execute('select * from ' + data.split(":")[1])
        col_names = [row[0] for row in cursor.description]
        for i in col_names:
            s += "<th>" + str(i) + "</th>"
        s += "<th>Действие</th>"
        for row1 in cursor.execute('select * from ' + str(data.split(":")[1])):
            for i in range(0, len(row1)):
                if fuzz.WRatio(str(data.split(":")[2].replace("_", " ")), str(row1[i])) > 86 and len(
                        str(data.split(":")[2]).replace("_", " ")) <= len(str(row1[i])):
                    s += "<tr>"
                    tochnost = 1
                    for i in range(0, len(row1)):
                        s += "<td>" + str(row1[i]) + "</td>"
                    s += "<td><button onclick=if(confirm('Удалить?')){vala('DELETE:" + str(
                        data.split(":")[1].upper()) + ":" + str(row1[0]) + ":" + str(col_names[0]) + \
                         "');}else{event.stopPropagation();event.preventDefault();}; class='dell'>Удалить</button>" \
                         "<button class='edit' onclick=vala('EDITSTRING:" + str(data.split(":")[1]) + ":" + str(
                        row1[0]) + ":back:" + str(data.split(":")[2].replace(" ", "_")) + "')>редактировать</button></td></tr>"
        if tochnost == 0:
            for row1 in cursor.execute('select * from ' + str(data.split(":")[1])):
                for i in range(0, len(row1)):
                    if fuzz.WRatio(str(data.split(":")[2].replace("_", " ")), str(row1[i])) > 85 and len(
                            str(data.split(":")[2]).replace("_", " ")) <= len(str(row1[i])):
                        s += "<tr>"
                        for i in range(0, len(row1)):
                            s += "<td>" + str(row1[i]) + "</td>"
                        s += "<td><button onclick=if(confirm('Удалить?')){vala('DELETE:" + str(
                            data.split(":")[1].upper()) + ":" + str(row1[0]) + ":" + str(col_names[0]) + \
                             "');}else{event.stopPropagation();event.preventDefault();}; class='dell'>Удалить</button>" \
                             "<button class='edit' onclick=vala('EDITSTRING:" + str(data.split(":")[1]) + ":" + str(
                            row1[0]) + ":back:" + str(data.split(":")[2].replace(" ", "_")) + "')>редактировать</button></td></tr>"
        diction.update({"add": s})
        s = "<button class='btn btn-lpbuilder wave-effect' onclick=vala('EDIT_VIEW:" + str(data.split(":")[1]) + "')>Назад</button>"
        diction.update({"actionButton": s})
    return diction

def search_all_table(data):
    if data != None:
        cursor = connection.cursor()
        cursor1 = connection.cursor()
        diction = dict()
        s = "<tr><th colspan=3>найдены совпадения в следующих справочниках</th></tr>"
        for row1 in cursor.execute('SELECT table_name FROM user_tables'):
            o = 1
            for row2 in cursor1.execute('select * from ' + str(row1[0])):
                for i in range(0, len(row2)):
                    if fuzz.WRatio(str(data.split(":")[1].replace("_", " ")), str(row2[i])) > 86:
                        if o == 1:
                            s += "<tr><th colspan=2 >название справочника: " + row1[
                                0] + "</th><th><button class=edit onclick=vala('EDIT_VIEW:" + str(row1[0]) + ":" + \
                                 data.split(":")[1].replace(" ", "_") + "') >открыть</button></th></tr>"
                            o = 0
                        s += "<tr>"
                        s += "<td colspan=2>" + str(row2[i]) + "</td>"
                        s += "<td><button class=edit onclick=vala('EDITSTRING:" + str(row1[0]) + ":" + str(row2[0]) + ":" + \
                             data.split(":")[1].replace(" ", "_") + "') >показать</button></td>"
                        s += "</tr>"
        diction.update({"add": s})
    return diction
# def add_view(data1):
#     if data1 != None:
#         data = int(data1)
#         diction = dict()
#         tableName = "<tr><th>№</th><th>Название столбца</th><th>тип значения</th><th>размер</th><th>не может быть пустым</th></tr>"
#         diction.update({"name0": tableName})
#         tableName = ""
#         for i in range(0, data):
#             tableName += "<tr>" \
#             "<td>" + str(i+1) + "</td>" \
#             "<td><input id=name" + str(i) + " placeholder='название столбца' type='text' class='input1'></td>" \
#             "<td><select class=input1 id=type" + str(i) + " >" \
#                     "<option value=VARCHAR2>Слова</option>" \
#                     "<option value=NUMBER >Числа</option>" \
#                     "<option value=DATE >Дата</option>" \
#                     "<option value=CLOB >CLOB</option>" \
#                     "<option value=BLOB >BLOB</option>" \
#                     "</select></td>" \
#             "<td><input id=size" + str(i) + " class=input1 type=number min=1 value=10></td>" \
#             "<td><input class=inputCheck value=1 type=checkbox id='check" + str(i) + "'/></td>" \
#             "</tr>"
#         diction.update({"add": tableName})
#         tableName = "<div><input placeholder='Краткое описаине таблицы' class=inputNT id=description></div>" \
#                     "<div><input placeholder='Название таблицы' class=inputNT id=tableName></div>" \
#                     "<div><button onclick=vala1(document.getElementById('tableName').value)," \
#                                  "onclick=vala1(document.getElementById('description').value),"
#         for i in range(0, data):
#             tableName += "vala1(document.getElementById('name" + str(i) + "').value)," \
#                          "vala1(document.getElementById('type" + str(i) + "').value)," \
#                          "vala1(document.getElementById('size" + str(i) + "').value)," \
#                          "vala1(document.getElementById('check" + str(i) + "').checked),"
#         tableName += "vala2()>Создать</button></div>"
#         diction.update({"addButton": tableName})
#         return diction

def edit_view(data):
    if data != None:
        cursor = connection.cursor()
        diction = dict()
        cursor.execute('select * from ' + data.split(":")[1])
        col_names = [row[0] for row in cursor.description]
        size = len(col_names)
        s = ""
        for i in col_names:
            s += "<th>" + i + "</th>"
        s += "<th>Действие</th>"
        diction.update({"name0": s})
        if data.split(":")[1] == "SPRAV_NAME":
            dablic = 0
            s = ""
            for row in cursor.execute('select * from ' + data.split(":")[1]):
                s += "<tr>"
                for i in range(0, size):
                    if dablic == 0:
                        s += "<td><a onclick=vala('EDIT_VIEW:" + str(row[i]) + "')>" + str(row[i]) + "</a></td>"
                        dablic = 1
                    else:
                        s += "<td>" + str(row[i]) + "</td>"
                        # s += "<td><button onclick=if(confirm('Удалить?')){vala('DELETE:SPRAV_NAME:" + str(row[0]) + ":" + str(col_names[0]) +"');}else{event.stopPropagation();event.preventDefault();}; class='dell'>Удалить</button>" \
                        s += "<td><button class='edit' onclick=vala('EDIT_VIEW:" + str(row[0]) + "')>открыть</button></td>"
                        dablic = 0
                s += "</tr>"
            diction.update({"add": s})
            # s = "<button class='btn btn-lpbuilder wave-effect'>Тут должна быть кнопка добаления записей</button>"
            # diction.update({"actionButton": s})
        else:
            s = "<tr>"
            for i in range(0, size, 1):
                s += "<td><input id=name" + str(i) + " placeholder='значение поля' type='text' class='input'></input></td>"
            s += "<td><button onclick=vala3('" + str(data.split(":")[1].upper()) + "'),"
            for i in range(0, size, 1):
                s += "vala3(document.getElementById('name" + str(i) + "').value),"
            for i in col_names:
                s += "vala3('" + i + "'),"
            s += "vala4() class = 'add' >добавить</button></td></tr>"
            diction.update({"add": s})
            s = ""
            for row in cursor.execute('select * from ' + data.split(":")[1]):
                s += "<tr>"
                for i in range(0, size):
                    s += "<td>" + str(row[i]) + "</td>"
                s += "<td><button onclick=if(confirm('Удалить?')){vala('DELETE:" + str(data.split(":")[1].upper()) + ":" + str(row[0]) + ":" + str(col_names[0]) + \
                     "');}else{event.stopPropagation();event.preventDefault();}; class='dell'>Удалить</button>" \
                     "<button class='edit' onclick=vala('EDITSTRING:" + str(data.split(":")[1]) + ":" + str(row[0]) + ":back')>редактировать</button></td></tr>"
            diction.update({"add1": s})
            if len(data.split(":")) == 2:
                s = "<div align=150px><button onclick=vala('HELP1') class='btn btn-lpbuilder wave-effect'>Назад</button></div>"
            else:
                s = "<div align=150px><button onclick=vala5('" + data.split(":")[2] + "') class='btn btn-lpbuilder wave-effect'>Назад</button></div>"
            s += "<input id=search class=inputNT placeholder='поиск по этой таблице' type='text'></input><button onclick=vala('searchintable:'+'" + str(data.split(":")[1]) + ":'+document.getElementById('search').value) class='upbutton'>Поиск</button>"
            diction.update({"actionButton": s})

        return diction

def addString(data):
    if data != None:
        tableName = str(data.split(":")[1])
        dataPoly = list()
        namePoly = list()
        size = len(data.split(":"))
        size = int(((size-3)/2)+2)
        for i in range(2, size):
            dataPoly.append(str(data.split(":")[i]))
        for i in range(size, size+size-2):
            namePoly.append(str(data.split(":")[i]))
        s = "INSERT INTO " + str(tableName) + " ("
        for i in range(0, size-2):
            if i == size-3:
                s += str(namePoly[i]) + ") "
            else:
                s += str(namePoly[i]) + ","
        s += "VALUES ("
        for i in range(0, size-2):
            if i == size-3:
                s += "'" + str(dataPoly[i]) + "');"
            else:
                s += "'" + str(dataPoly[i]) + "',"
        cursor = connection.cursor()
        cursor.execute(str(s))
        send = edit_view(":" + tableName)
    return send

def dell(data):
    if data != None:
        nameTable = str(data.split(":")[1])
        dateTable = data.split(":")[2]
        nameColumn = data.split(":")[3]
        s = ""
        if nameTable == "SPRAV_NAME":
            cursor = connection.cursor()
            s += "DELETE FROM " + nameTable + " WHERE " + nameColumn + "='" + dateTable + "';"
            cursor.execute(str(s))
            s = "drop table " + dateTable[0] + ";"
            cursor.execute(str(s))
            send = edit_view("SPRAV_NAME")
        else:
            s += "DELETE FROM " + nameTable + " WHERE " + str(nameColumn) + "='" + str(dateTable) + "';"
            cursor = connection.cursor()
            cursor.execute(str(s))
            send = edit_view(":" + nameTable)
    return send

def add(data):
    if data != None:
        tableNmae = str(data.split(":")[1]).upper()
        description = data.split(":")[2]
        name = list()
        type = list()
        size = list()
        check = list()

        for i in range(3, len(data.split(":"))-3, 4):
            name.append(data.split(":")[i])
        for i in range(4, len(data.split(":"))-3, 4):
            type.append(data.split(":")[i])
        for i in range(5, len(data.split(":"))-2, 4):
            size.append(data.split(":")[i])
        for i in range(6, len(data.split(":"))-1, 4):
            if str(data.split(":")[i]) == "true":
                check.append("NOT NULL")
            else:
                check.append("")
        s = "CREATE TABLE " + str(tableNmae) + " ( "
        for i in range(0, len(name)):
            if i == len(name)-1:
                s += str(name[i]) + " " + str(type[i]) + "(" + str(size[i]) + ") " + str(check[i])
            else:
                s += str(name[i]) + " " + str(type[i]) + "(" + str(size[i]) + ") " + str(check[i]) + ", "
        s += ");"
        cursor = connection.cursor()
        cursor.execute(str(s))
        # print(s)
        s = "INSERT INTO SPRAV_NAME (NAME, DESCRIPTION) VALUES ('" + tableNmae + "', '" + description + "');"
        # print(s)
        cursor.execute(str(s))
        send = edit_view(tableNmae)
        return send

def replace(data):
    if data != None:
        global auth
        print(auth)
        cursor = connection.cursor()
        diction = dict()
        cursor.execute('select * from ' + data.split(":")[1])
        col_names = [row[0] for row in cursor.description]
        size = len(col_names)
        namecolumn = ""
        for i in col_names:
            namecolumn += "<th>" + i + "</th>"
        if data.split(":")[1] == "SPRAV_NAME":
            namecolumn += "<th>Действие</th>"
            diction.update({"name0": namecolumn})
            dablic = 0
            s = ""
            for row in cursor.execute('select * from ' + data.split(":")[1]):
                s += "<tr>"
                for i in range(0, size):
                    if dablic == 0:
                        s += "<td><a onclick=vala('VIEW:" + str(row[i]) + "')>" + str(row[i]) + "</a></td>"
                        dablic = 1
                    else:
                        s += "<td>" + str(row[i]) + "</td>"
                        # s += "<td><button onclick=if(confirm('Удалить?')){vala('DELETE:SPRAV_NAME:" + str(row[0]) + ":" + str(col_names[0]) +"');}else{event.stopPropagation();event.preventDefault();}; class='dell'>Удалить</button>" \
                        s += "<td><button class='edit' onclick=vala('VIEW:" + str(row[0]) + "')>открыть</button></td>"
                        dablic = 0
                s += "</tr>"
            diction.update({"add": s})
            # s = "<button class='btn btn-lpbuilder wave-effect'>Тут должна быть кнопка добаления записей</button>"
            # diction.update({"actionButton": s})
        else:
            diction.update({"name0": namecolumn})
            s = ""
            for row in cursor.execute('select * from ' + data.split(":")[1]):
                s += "<tr>"
                for i in range(0, size):
                    s += "<td>" + str(row[i]) + "</td>"
            diction.update({"add1": s})
            if len(data.split(":")) == 2:
                s = "<div align=150px><button align=150px onclick=vala('HELP') class='btn btn-lpbuilder wave-effect'>Назад</button></div>"
            else:
                s = "<div align=150px><button onclick=vala5('" + data.split(":")[2] + "') class='btn btn-lpbuilder wave-effect'>Назад</button><div>"
            s += "<input id=search class=inputNT placeholder='поиск по этой таблице' type='text'></input><button onclick=vala('searchintableview:'+'" + str(
                data.split(":")[1]) + ":'+document.getElementById('search').value) class='upbutton'>Поиск</button>"
            diction.update({"actionButton": s})

        return diction


def add_sprav(request):
    if request.method == "GET":
        return render(request, 'add_page.html')
    if request.method == "POST":
        if request.is_ajax:
            name = request.POST
            s = name.dict()
            name = s['add']
            a = str(name)
            data = replace(a)
            print(data)
            return JsonResponse(data)

def wiev_sprav(request):
    if request.method == "GET":
        return render(request, 'page2.html')
    if request.method == "POST":
        if request.is_ajax:
            name = request.POST
            s = name.dict()
            name = s['add']
            a = str(name)
            data = replace(a)
            print(data)
            return JsonResponse(data)

def start_page(request):
    if request.method == "GET":
        return render(request, 'page1.html')
    if request.method == "POST":
        if request.is_ajax:
            name = request.POST
            s = name.dict()
            name = s['add']
            a = str(name)
            data = replace(a)
            print(data)
            return JsonResponse(data)


def function1(request):
    data = {"massage": ""}
    if request.method == "GET":
        data["massage"] = "uspeh"
    return JsonResponse(data)


