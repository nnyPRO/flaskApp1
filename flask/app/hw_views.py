# เมษนี ลายเฮือง - แนน
# 650510676
# Sec001

from flask import jsonify, render_template, redirect, url_for, flash, request, redirect
from flask_login import login_user, login_required, logout_user, current_user
from app import app, db, login_manager
import json
import bcrypt
from urllib.request import urlopen
import datetime
import calendar
from app.forms import forms
from app.models.blogEntry import BlogEntry
from app.models.authuser import AuthUser, PrivateContact
from werkzeug.security import check_password_hash
from werkzeug.urls import url_parse
from werkzeug.security import generate_password_hash, check_password_hash



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
                print(validated_dict)
                entry = BlogEntry(**validated_dict)
                app.logger.debug(str(entry))
                db.session.add(entry)
            # if there is an id already: update the blog entry
            else:
                blogEntry = BlogEntry.query.get(id_)
                blogEntry.update(**validated_dict)

            db.session.commit()
        return hw10_db_blogEntries()
    return render_template('hw11/hw10_microblog.html')


@app.route('/hw10/blogEntries')
def hw10_db_blogEntries():
    blogEntries = []
    db_blogEntries = BlogEntry.query.all()

    blogEntries = list(map(lambda x: x.to_dict(), db_blogEntries))
    app.logger.debug("DB Contacts: " + str(blogEntries))

    return jsonify(blogEntries)


@app.route('/hw10/remove_blogEntries', methods=('GET', 'POST'))
def hw10_remove_blogEntries():
    if request.method == 'POST':
        result = request.form.to_dict()
        id_ = result.get('id', '')
        blogEntry = BlogEntry.query.get(id_)
        db.session.delete(blogEntry)
        db.session.commit()

    return hw10_db_blogEntries()


@app.route('/hw11/login', methods=('GET', 'POST'))
def hw11_login():
    if request.method == 'POST':
        # login code goes here
        email = request.form.get('email')
        password = request.form.get('password')
        remember = bool(request.form.get('remember'))

        user = AuthUser.query.filter_by(email=email).first()

        # check if the user actually exists
        # take the user-supplied password, hash it, and compare it to the
        # hashed password in the database
        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            # if the user doesn't exist or password is wrong, reload the page
            return redirect(url_for('hw11_login'))

        # if the above check passes, then we know the user has the right
        # credentials
        login_user(user, remember=remember)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('lab11_profile')
        return redirect(next_page)

    return render_template('hw11/login.html')

@app.route('/hw11/signup', methods=('GET', 'POST'))
def hw11_signup():

    if request.method == 'POST':
        result = request.form.to_dict()
        app.logger.debug(str(result))

        validated = True
        validated_dict = {}
        valid_keys = ['email', 'name', 'password']

        # validate the input
        for key in result:
            app.logger.debug(str(key)+": " + str(result[key]))
            # screen of unrelated inputs
            if key not in valid_keys:
                continue

            value = result[key].strip()
            if not value or value == 'undefined':
                validated = False
                break
            validated_dict[key] = value
            # code to validate and add user to database goes here
        app.logger.debug("validation done")
        if validated:
            app.logger.debug('validated dict: ' + str(validated_dict))
            email = validated_dict['email']
            name = validated_dict['name']
            password = validated_dict['password']
            # if this returns a user, then the email already exists in database
            user = AuthUser.query.filter_by(email=email).first()

            if user:
                # if a user is found, we want to redirect back to signup
                # page so user can try again
                flash('Email address already exists')
                return redirect(url_for('hw11_signup'))

            # create a new user with the form data. Hash the password so
            # the plaintext version isn't saved.
            app.logger.debug("preparing to add")
            avatar_url = gen_avatar_url(email, name)
            new_user = AuthUser(email=email, name=name,
                                password=generate_password_hash(
                                    password, method='sha256'),
                                avatar_url=avatar_url)
            # add the new user to the database
            db.session.add(new_user)
            db.session.commit()

        return redirect(url_for('hw11_login'))
    return render_template('hw11/signup.html')


def gen_avatar_url(email, name):
    bgcolor = generate_password_hash(email, method='sha256')[-6:]
    color = hex(int('0xffffff', 0) -
                int('0x'+bgcolor, 0)).replace('0x', '')
    lname = ''
    temp = name.split()
    fname = temp[0][0]
    if len(temp) > 1:
        lname = temp[1][0]

    avatar_url = "https://ui-avatars.com/api/?name=" + \
        fname + "+" + lname + "&background=" + \
        bgcolor + "&color=" + color
    return avatar_url


@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our
    # user table, use it in the query for the user
    return AuthUser.query.get(int(user_id))


@app.route('/hw11/logout')
@login_required
def hw11_logout():
    logout_user()
    return redirect(url_for('hw10'))
