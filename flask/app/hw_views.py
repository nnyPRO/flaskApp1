# เมษนี ลายเฮือง - แนน
# 650510676
# Sec001

from flask import jsonify, render_template, redirect, url_for, flash, request, redirect
from app import app, db
import json
import bcrypt
from urllib.request import urlopen
import datetime
import calendar
from app.forms import forms
from app.models.blogEntry import BlogEntry


@app.route('/weather')
def hw01_localweather():
    return app.send_static_file('hw01_localweather.html')


# This route serves the dictionary d at the route /data
@app.route("/api/weather")
def api_weather():
    # define some data
    url = "https://api.waqi.info/feed/Chiangmai/?token=830b47529331aafbd839b57c9415608551d1d4f8"
    d = urlopen(url)
    data = json.load(d)
    a = {
        "AQI": data["data"]["aqi"],
        "PM10": data["data"]["iaqi"]["pm10"]["v"],
        "PM2.5": data["data"]["iaqi"]["pm25"]["v"],
        "Temperature": data["data"]["iaqi"]["t"]["v"],
        "Time": data["data"]["time"]["iso"]
        # "a" : 28
    }
    # app.logger.debug(a)
    return jsonify(a)  # convert your data to JSON and return


@app.route("/hw03/pm25/")
def hw03_pm25():
    url = "https://api.waqi.info/feed/Chiangmai/?token=830b47529331aafbd839b57c9415608551d1d4f8"
    d = urlopen(url)
    data = json.load(d)
    # pm25 = {
    #     "AQI" : data["data"]["forecast"]["daily"]["pm25"][0]
    # }
    list_pm25 = data["data"]["forecast"]["daily"]["pm25"]
    date_ls1 = (list_pm25[0]["day"]).split('-')
    date_ls2 = (list_pm25[-1]["day"]).split('-')
    d1 = datetime.date(int(date_ls1[0]), int(date_ls1[1]), int(date_ls1[2]))
    d2 = datetime.date(int(date_ls2[0]), int(date_ls2[1]), int(date_ls2[2]))
    # d1 = list_pm25[0]["day"]
    # d1 = datetime.date(2023, 12, 1)
    # d2 = datetime.date(2023, 12, 31)
    # d2 = list_pm25[-1]["day"]
    weeks = (d1-d2).days//7
    # app.logger.debug(type(list_pm25[0]["avg"]))

    return render_template('lab03/hw03_pm25.html', list_pm25=list_pm25, weeks=abs(weeks))


@app.route("/hw04")
def hw04_rwd():
    return app.send_static_file('hw04_rwd.html')


@app.route("/hw04/aqicard/")
def hw04_aqicard():
    month = {'01': 'Janauary',
             '02': 'February',
             '03': 'March',
             '04': 'April',
             '05': 'May',
             '06': 'June',
             '07': 'July',
             '08': 'August',
             '09': 'September',
             '10': 'October',
             '11': 'November',
             '12': 'December'}

    url = "https://api.waqi.info/feed/Chiangmai/?token=830b47529331aafbd839b57c9415608551d1d4f8"
    c = urlopen(url)
    chiangmai = json.load(c)
    time = (chiangmai["data"]["time"]["s"]).split(' ')
    new_time = time[0].split('-')
    f = chiangmai["data"]["forecast"]["daily"]["pm25"]
    forecast = []
    i = 0
    while len(forecast) < 3:
        next_time = f[i]["day"].split('-')
        if next_time[2] > new_time[2]:
            forecast.append({
                "avg": f[i]["avg"],
                "day": next_time[2],
                "month": calendar.month_abbr[int(next_time[1])]
            })
        i += 1
    d_chiangmai = {
        "aqi": chiangmai["data"]["aqi"],
        "forecast": forecast,
        "day": new_time[2],
        "month": month[new_time[1]],
        "year": new_time[0]
    }

    url = "https://api.waqi.info/feed/Bangkok/?token=830b47529331aafbd839b57c9415608551d1d4f8"
    b = urlopen(url)
    bangkok = json.load(b)
    time = (bangkok["data"]["time"]["s"]).split(' ')
    new_time = time[0].split('-')
    f = bangkok["data"]["forecast"]["daily"]["pm25"]
    forecast = []
    i = 0
    while len(forecast) < 3:
        next_time = f[i]["day"].split('-')
        if next_time[2] > new_time[2]:
            forecast.append({
                "avg": f[i]["avg"],
                "day": next_time[2],
                "month": calendar.month_abbr[int(next_time[1])]
            })
        i += 1
    d_bangkok = {
        "aqi": bangkok["data"]["aqi"],
        "forecast": forecast,
        "day": new_time[2],
        "month": month[new_time[1]],
        "year": new_time[0]
    }
    url = "https://api.waqi.info/feed/Phuket/?token=830b47529331aafbd839b57c9415608551d1d4f8"
    p = urlopen(url)
    phuket = json.load(p)
    time = (phuket["data"]["time"]["s"]).split(' ')
    new_time = time[0].split('-')
    f = phuket["data"]["forecast"]["daily"]["pm25"]
    forecast = []
    i = 0
    while len(forecast) < 3:
        next_time = f[i]["day"].split('-')
        if next_time[2] > new_time[2]:
            forecast.append({
                "avg": f[i]["avg"],
                "day": next_time[2],
                "month": calendar.month_abbr[int(next_time[1])]
            })
        i += 1
    d_phuket = {
        "aqi": phuket["data"]["aqi"],
        "forecast": forecast,
        "day": new_time[2],
        "month": month[new_time[1]],
        "year": new_time[0]
    }
    url = "https://api.waqi.info/feed/Ubon-Ratchathani/?token=830b47529331aafbd839b57c9415608551d1d4f8"
    u = urlopen(url)
    ubon = json.load(u)
    time = (ubon["data"]["time"]["s"]).split(' ')
    new_time = time[0].split('-')
    f = ubon["data"]["forecast"]["daily"]["pm25"]
    forecast = []
    i = 0
    while len(forecast) < 3:
        next_time = f[i]["day"].split('-')
        if next_time[2] > new_time[2]:
            forecast.append({
                "avg": f[i]["avg"],
                "day": next_time[2],
                "month": calendar.month_abbr[int(next_time[1])]
            })
        i += 1
    d_ubon = {
        "aqi": ubon["data"]["aqi"],
        "forecast": forecast,
        "day": new_time[2],
        "month": month[new_time[1]],
        "year": new_time[0]
    }

    return render_template('hw04_aqicard.html', chiangmai=d_chiangmai, bangkok=d_bangkok, phuket=d_phuket, ubon=d_ubon)


def read_file(filename, mode="rt"):
    with open(filename, mode, encoding='utf-8') as fin:
        return fin.read()


def write_file(filename, contents, mode="wt"):
    with open(filename, mode, encoding="utf-8") as fout:
        fout.write(contents)


@app.route('/hw06/register', methods=('GET', 'POST'))
def hw06_register():
    form = forms.RegistrationForm()
    bool_user = False
    bool_email = False
    if form.validate_on_submit():
        password = form.password.data
        byte = password.encode('utf-8')
        # generating the salt
        salt = bcrypt.gensalt()
        app.logger.debug("salt:", salt)
        # Hashing the password
        hash = str(bcrypt.hashpw(byte, salt))
        username = str.lower(form.username.data)
        email = str.lower(form.email.data)
        raw_json = read_file('app/data/users.json')
        user_list = json.loads(raw_json)
        if user_list != []:
            for user in user_list:
                if username == user['username']:
                    bool_user = True
                elif email == user['email']:
                    bool_email = True

            if bool_user:

                flash('Username already exists')
            elif bool_email:
                flash('Email already exists')
            else:
                user_list.append({'username': username,
                                  'email': email,
                                  'password': hash
                                  })
                write_file('app/data/users.json',
                           json.dumps(user_list, indent=4))
                return redirect(url_for('hw06_users'))

        else:
            user_list.append({'username': username,
                              'email': email,
                              'password': hash
                              })
            write_file('app/data/users.json',
                       json.dumps(user_list, indent=4))
            return redirect(url_for('hw06_users'))

    return render_template('lab06/hw06_register.html', form=form)


@app.route('/hw06/users')
def hw06_users():
    raw_json = read_file('app/data/users.json')
    user_list = json.loads(raw_json)
    return render_template('lab06/hw06_users.html', user_list=user_list)


@app.route('/hw10',  methods=('GET', 'POST'))
def hw10():
    if request.method == 'POST':
        result = request.form.to_dict()
        app.logger.debug(str(result))
        id_ = result.get('id', '')
        validated = True
        validated_dict = dict()
        valid_keys = ['name', 'message', 'email']

        # validate the input
        for key in result:
            app.logger.debug(f"{key}: {result[key]}")
            # screen of unrelated inputs
            if key not in valid_keys:
                continue

            value = result[key].strip()
            if not value or value == 'undefined':
                validated = False
                break
            validated_dict[key] = value
            
        if validated:
            app.logger.debug('validated dict: ' + str(validated_dict))
            # if there is no id: create a new contact entry
            if not id_:
                entry = BlogEntry(**validated_dict)
                app.logger.debug(str(entry))
                db.session.add(entry)
            # if there is an id already: update the blog entry
            else:
                blogEntry = BlogEntry.query.get(id_)
                blogEntry.update(**validated_dict)

            db.session.commit()

        return hw10_db_blogEntries()
    return app.send_static_file('hw10_microblog.html')


@app.route('/hw10/blogEntries')
def hw10_db_blogEntries():
    blogEntries = []
    db_blogEntries = BlogEntry.query.all()

    blogEntries = list(map(lambda x: x.to_dict(), db_blogEntries))
    app.logger.debug("DB Contacts: " + str(blogEntries))

    return jsonify(blogEntries)
