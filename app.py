
from datetime import datetime, timedelta, timezone
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import smtplib
from flask import Flask, flash, jsonify, redirect, request, render_template, session, url_for
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
import json
from pytz import timezone
from sqlalchemy.types import DateTime
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.secret_key = os.getenv('SECRET_KEY')
app.config['EMAIL_ADDRESS'] = os.getenv('EMAIL_ADDRESS')
app.config['EMAIL_PASSWORD'] = os.getenv('EMAIL_PASSWORD')
app.permanent_session_lifetime = timedelta(minutes=30)
db = SQLAlchemy(app)

india_timezone = timezone('Asia/Kolkata')

#For User 
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    otp = db.Column(db.String(6), nullable=False)
    otp_expires_at = db.Column(DateTime(timezone=True), nullable=False)
    verified = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<User {self.email}>'
    
# Teacher model use to store data in database
class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    teacher_id = db.Column(db.Integer)
    mobile_number = db.Column(db.String(20), nullable=True)
    first_name = db.Column(db.String(100), nullable=True)
    last_name = db.Column(db.String(100), nullable=True)
    date = db.Column(db.Date, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    is_teacher = db.Column(db.Boolean, default=False)
    can_work_with_ous =  db.Column(db.String(50))
    gender = db.Column(db.String(50))
    city = db.Column(db.String(50))
    city_type = db.Column(db.String(50))
    is_married = db.Column(db.Boolean, default=False)
    has_kids = db.Column(db.Boolean, default=False)
    kids_age_range = db.Column(db.String(20))
    teacher_type = db.Column(db.String(50))
    can_teach_personal_student = db.Column(db.Boolean, default=False)
    can_teach_iit = db.Column(db.Boolean)
    _iit_options = db.Column(db.Text, nullable=True)
    can_teach_neet = db.Column(db.Boolean)
    _neet_options = db.Column(db.Text, nullable=True)
    can_teach_upsc = db.Column(db.Boolean)
    _upsc_options = db.Column(db.Text, nullable=True)
    can_teach_banking = db.Column(db.Boolean)
    _banking_options = db.Column(db.Text, nullable=True)
    can_teach_personally = db.Column(db.Boolean)
    _personally_options = db.Column(db.Text, nullable=True)
    can_teach_cat = db.Column(db.Boolean)
    _cat_options = db.Column(db.Text, nullable=True)
    can_teach_gmat = db.Column(db.Boolean)
    _gmat_options = db.Column(db.Text, nullable=True)
    laptop = db.Column(db.Boolean, default=False)
    connected_with_ous = db.Column(db.Boolean, default=False)
    batch_capacity = db.Column(db.Integer,nullable=True)    
    updated_by = db.Column(db.Integer, nullable=True, default=0)
    
    @property
    def iit_options(self):
        return json.loads(self._iit_options or '[]')
    @iit_options.setter
    def iit_options(self, value):
        self._iit_options = json.dumps(value) if value else None

    @property
    def neet_options(self):
        return json.loads(self._neet_options or '[]')
    @neet_options.setter
    def neet_options(self, value):
        self._neet_options = json.dumps(value) if value else None

    @property
    def upsc_options(self):
        return json.loads(self._upsc_options or '[]')
    @upsc_options.setter
    def upsc_options(self, value):
        self._upsc_options = json.dumps(value) if value else None

    @property
    def banking_options(self):
        return json.loads(self._banking_options or '[]')
    @banking_options.setter
    def banking_options(self, value):
        self._banking_options = json.dumps(value) if value else None

    @property
    def personally_options(self):
        return json.loads(self._personally_options or '[]')
    @personally_options.setter
    def personally_options(self, value):
        self._personally_options = json.dumps(value) if value else None

    @property
    def cat_options(self):
        return json.loads(self._cat_options or '[]')
    @cat_options.setter
    def cat_options(self, value):
        self._cat_options = json.dumps(value) if value else None

    @property
    def gmat_options(self):
        return json.loads(self._gmat_options or '[]')
    @gmat_options.setter
    def gmat_options(self, value):
        self._gmat_options = json.dumps(value) if value else None

with app.app_context():
    db.create_all()

#Generate otp method
def generate_otp():
    return str(random.randint(100000, 999999))

#Sent otp method
def send_otp(email, otp):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(app.config['EMAIL_ADDRESS'], app.config['EMAIL_PASSWORD'])        
        subject = 'OTP Verification'        
        # HTML email template
        html_body = render_template('email_template.html', otp=otp)       
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = app.config['EMAIL_ADDRESS']
        msg['To'] = email
        text_body = f'Your OTP is: {otp} Please Do Not Share With Anyone! '
        msg.attach(MIMEText(text_body, 'plain'))        
        msg.attach(MIMEText(html_body, 'html'))        
        smtp.sendmail(app.config['EMAIL_ADDRESS'], email, msg.as_string())

#Login Route
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        user = User.query.filter_by(email=email).first()
        if user:
            otp = generate_otp()
            otp_expires_at = datetime.now(india_timezone) + timedelta(minutes=1)
            user.otp = otp
            user.otp_expires_at = otp_expires_at
            db.session.commit()
            send_otp(email, otp)
            session['email'] = email
            session['otp'] = otp
            return redirect('/verify')
        else:
            flash('Email does not exist!', 'error')
            session.pop('email', None) 
            session.pop('otp', None)
            return redirect(url_for('login'))  
    return render_template('login.html')

@app.route('/resend_otp', methods=['POST'])
def resend_otp():
    if 'email' in session and 'otp' in session:
        email = session['email']
        user = User.query.filter_by(email=email).first()
        if user:
            otp = generate_otp()
            otp_expires_at = datetime.now(india_timezone) + timedelta(minutes=1)
            user.otp = otp
            user.otp_expires_at = otp_expires_at
            db.session.commit()
            send_otp(email, otp)
            flash('Email ', 'error')
            return redirect('/verify')
        else:
            return jsonify({'error': 'User not found'}), 404
    else:
        return jsonify({'error': 'Session data missing'}), 400
    
#verify Route
@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if 'email' in session and 'otp' in session:
        if request.method == 'POST':
            user_otp = request.form['otp']
            email = session['email']
            user = User.query.filter_by(email=email, otp=user_otp).first()
            if user:
                if user.otp_expires_at.astimezone(india_timezone) > datetime.now(india_timezone):
                    user.verified = True
                    db.session.commit()
                    return redirect('/dashboard')
                else:
                    flash('OTP has expired. Please try again.', 'error')
                    return redirect(url_for('login'))
            else:
                flash('Please enter a valid OTP.', 'error')
                return redirect(url_for('verify'))
        return render_template('verify.html')
    else:
        return redirect('/')

#Dashboard Route    
@app.route('/dashboard')
def dashboard():
    if 'email' not in session:
        return redirect(url_for('login'))
    user_count = User.query.count()
    teacher_count = Teacher.query.count()
    not_updated_teachers = Teacher.query.filter_by(updated_by=0).count()
    return render_template('index.html', user_count=user_count,not_updated_teachers=not_updated_teachers, teacher_count=teacher_count)

#Route for teacher form
@app.route('/form', methods=['GET', 'POST'])
def index():
        if 'email' not in session:
            return redirect(url_for('login'))  

        if request.method == 'POST':
            session.pop('email', None)

            data = {}
            for fieldset in ['iit', 'neet', 'upsc', 'banking', 'personally', 'cat', 'gmat']:
                can_teach_key = f'can_teach_{fieldset}'
                can_teach_val = request.form.get(can_teach_key)
                can_teach = can_teach_val == 'on'  
                options_key = f'{fieldset}_options'
                options_val = request.form.getlist(f'can_teach_{fieldset}_opt[]')
                data[can_teach_key] = can_teach
                data[options_key] = options_val
            
            teacher_id = request.form.get('teacher_id')
            
            if teacher_id:  
                existing_entry = Teacher.query.filter_by(id=teacher_id).first()
                if existing_entry:
                    for key, value in data.items():
                        setattr(existing_entry, key, value)
                    db.session.commit()
                    return f"Data updated successfully! ID: {teacher_id}"
                else:
                    return "Teacher ID not found", 404
            else:  
                teaching_model = Teacher(**data)
                db.session.add(teaching_model)
                db.session.commit()
                return f"Form updated successfully! Data: {teaching_model}"
        return render_template('form.html')

#Route for get teacher data in form
@app.route('/get_teacher_data', methods=['GET'])
def get_teacher_data():
    if 'email' not in session:
            return redirect(url_for('login')) 
    try:
        teaching_id = request.args.get('id')
        
        if not teaching_id:
            return jsonify({'error': 'ID is required'}), 400
        teaching_data = Teacher.query.filter_by(id=teaching_id).first()
        if not teaching_data:
            return jsonify({'error': 'Data not found'}), 404
        iit_options = json.dumps(teaching_data.iit_options)
        neet_options = json.dumps(teaching_data.neet_options)
        upsc_options = json.dumps(teaching_data.upsc_options)
        banking_options = json.dumps(teaching_data.banking_options)
        personally_options = json.dumps(teaching_data.personally_options)
        cat_options = json.dumps(teaching_data.cat_options)
        gmat_options = json.dumps(teaching_data.gmat_options)
        data = {
            'mobile_number': teaching_data.mobile_number,
            'first_name': teaching_data.first_name,
            'last_name': teaching_data.last_name,
            'date': str(teaching_data.date),
            'age': teaching_data.age,
            'is_teacher': teaching_data.is_teacher,
            'can_work_with_ous': teaching_data.can_work_with_ous,
            'gender': teaching_data.gender,
            'city': teaching_data.city,
            'city_type': teaching_data.city_type,
            'is_married': teaching_data.is_married,
            'has_kids': teaching_data.has_kids,
            'kids_age_range': teaching_data.kids_age_range,
            'teacher_type': teaching_data.teacher_type,
            'can_teach_personal_student': teaching_data.can_teach_personal_student,
            'can_teach_iit': teaching_data.can_teach_iit,        
            'can_teach_neet': teaching_data.can_teach_neet,            
            'can_teach_upsc': teaching_data.can_teach_upsc,
            'can_teach_banking': teaching_data.can_teach_banking,            
            'can_teach_personally': teaching_data.can_teach_personally,            
            'can_teach_cat': teaching_data.can_teach_cat,
            'can_teach_gmat': teaching_data.can_teach_gmat,
            'can_teach_iit_opt': iit_options,
            'can_teach_neet_opt': neet_options,
            'can_teach_upsc_opt': upsc_options,
            'can_teach_banking_opt': banking_options,
            'can_teach_personally_opt': personally_options,
            'can_teach_cat_opt': cat_options,
            'can_teach_gmat_opt': gmat_options,
            'laptop': teaching_data.laptop,
            'connected_with_ous': teaching_data.connected_with_ous,
            'batch_capacity': teaching_data.batch_capacity
            
        }  
        return jsonify(data)
    except Exception as e:
        print(f'Error: {e}')
        return jsonify({'error': 'Internal Server Error'}), 500

#Route for get teacher ids in form(dropdown)
@app.route('/get_teacher_ids', methods=['GET'])
def get_teacher_ids():
    if 'email' not in session:
            return redirect(url_for('login'))
    search_term = request.args.get('q', '').lower()
    try:
        #teachers = teacher.query.filter(teacher.updated_by != 0, teacher.id.ilike(f'%{search_term}%')).all()       
        teachers = Teacher.query.filter(Teacher.id.ilike(f'%{search_term}%')).all()       
        if not teachers:
            return jsonify({'message': 'No teachers found with updated_by not equal to 0'})      
        ids = [str(teacher.id) for teacher in teachers]
        return jsonify({'id': ids})
    except Exception as e:
        print('An error occurred: %s', str(e))
        return jsonify({'error': str(e)}), 500
    
#Route edit teacher form - before any update
@app.route('/edit_teacher', methods=['GET'])
def edit_teacher():
    if 'email' not in session:
            return redirect(url_for('login'))
    teacher = Teacher.query.filter(Teacher.updated_by == 0, Teacher.age >= 18).first()
    if not teacher:
        flash('No teacher found with Added By User. Please add a new teacher.', 'danger')
        return redirect(url_for('dashboard'))  
    
    return render_template('edit_teacher.html', teacher=teacher, teachers=Teacher.query.all(), teacher_id=teacher.teacher_id)

#Route for get teacher selected id in form(dropdown)
@app.route('/get_teacher_new_id', methods=['GET'])
def get_teacher_new_id():
    if 'email' not in session:
        return redirect(url_for('login'))
    try:
        teacher = Teacher.query.filter(Teacher.updated_by == 0, Teacher.age >= 18).first()       
        if not teacher:
            return jsonify({'message': 'No teachers found with updated_by == 0'})
        return jsonify({'id': teacher.teacher_id})
    except Exception as e:        
        return jsonify({'error': str(e)}), 500
    
#Route for Update teacher
@app.route('/update_teacher', methods=['POST'])
def update_teacher():
    if 'email' not in session:
            return redirect(url_for('login'))        
    email = session['email']
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({'error': 'Unauthorized or invalid user'}), 403    
    try:
        teacher_id = request.form.get('teacher_id')      
        if not teacher_id:
            return jsonify({'error': 'Teacher ID is required'}), 400
        existing_teacher = Teacher.query.filter_by(id=teacher_id).first()
        existing_teacher.mobile_number = request.form.get('mobile_number')
        existing_teacher.first_name = request.form.get('first_name')
        existing_teacher.last_name = request.form.get('last_name')
        existing_teacher.date = request.form.get('date')
        existing_teacher.age = request.form.get('age')
        existing_teacher.is_teacher = request.form.get('is_teacher') == 'true'
        existing_teacher.can_work_with_ous = request.form.get('can_work_with_ous')
        existing_teacher.gender = request.form.get('gender')
        existing_teacher.city_type = request.form.get('city_type')
        existing_teacher.is_married = request.form.get('is_married') == 'true'
        existing_teacher.has_kids = request.form.get('has_kids') == 'true'
        existing_teacher.city = request.form.get('city')
        existing_teacher.can_teach_personal_student = request.form.get('can_teach_personal_student') == 'true'
        existing_teacher.kids_age_range = request.form.get('kids_age_range')
        existing_teacher.teacher_type = request.form.get('teacher_type')
        existing_teacher.laptop = request.form.get('laptop') == 'true'
        existing_teacher.connected_with_ous = request.form.get('connected_with_ous') == 'true'
        if existing_teacher.updated_by == 0:
            existing_teacher.updated_by = user.id
        batch_capacity = request.form.get('batch_capacity')
        existing_teacher.batch_capacity = int(batch_capacity) if batch_capacity else None
        if not existing_teacher:
            return jsonify({'error': 'Teacher not found'}), 404        
        data = {}       
        for fieldset in ['iit', 'neet', 'upsc', 'banking', 'personally', 'cat', 'gmat']:
            can_teach_key = f'can_teach_{fieldset}'
            can_teach_val = request.form.get(can_teach_key)
            can_teach = can_teach_val == 'True'  
            options_key = f'{fieldset}_options'
            options_val = request.form.getlist(f'can_teach_{fieldset}_opt[]')
            data[can_teach_key] = can_teach
            data[options_key] = options_val
        for key, value in data.items():
            setattr(existing_teacher, key, value)
            db.session.commit()
        return jsonify({'message': 'Teacher data updated successfully'}), 200
    except Exception as e:
        print('errorr',e)
        return jsonify({'error': str(e)}), 500

#Route for List view teacher
@app.route('/teacherlist', methods=['GET'])
def success():
    if 'email' not in session:
        return redirect(url_for('login'))    
    teachers = Teacher.query.all()
    return render_template('success.html', teachers=teachers, success_flag=True)

#Route for logout User
@app.route('/logout')
def logout():
    session.pop('email',None)
    return redirect('/')
    
if __name__ == '__main__':
    app.run(debug=True, port=5002) # app.run(debug=True, port=5002) add if get error releted to port 5000