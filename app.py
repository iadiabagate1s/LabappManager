
from flask import Flask, request, render_template, redirect, flash, session, jsonify 
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db,Tech, Project, Task ,Freezer
from forms import LoginForm, Register, Tasksform, Projform, Edituser
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgres:///labmanager')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY']=os.environ.get('SECRET_KEY','malachixxl')
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)
db.create_all()


@app.route('/addtech', methods= ['GET', 'POST'])
def adduser():
    ''' add  a user show form and handle form submit'''
    form = Register()
    if form.validate_on_submit():
        
        first_name = form.first_name.data
        last_name = form.last_name.data
        lab_id = form.lab_id.data
        avatar = form.avatar.data
        
        
        newuser = Tech.register(lab_id,first_name, last_name, avatar)
        
        db.session.commit()
        session['lab_id']= newuser.lab_id
        session['first_name'] = newuser.first_name
        session['last_name'] = newuser.last_name
        session['admin'] = newuser.admin
        print('newuser -----', newuser)
        
        
        return redirect(f'/user/home/{newuser.first_name}')
    
    return render_template('adduser.html', form = form)


@app.route('/', methods = ['GET', 'POST'])
def homelogin():
    
    if 'labid' in session:
        lab_id = session['lab_id']
        user = Tech.query.get_or_404(lab_id)
        return redirect(f'/user/home/{user.first_name}')
    else:
        form = LoginForm()
        if form.validate_on_submit():
            last_name = form.last_name.data
            lab_id = form.lab_id.data
        
            currentuser = Tech.authenticate(last_name, lab_id)
            if (currentuser == False ):
                return redirect('/')
            else :
                session['lab_id']= currentuser.lab_id
                session['first_name'] = currentuser.first_name
                session['last_name'] = currentuser.last_name
                session['admin'] = currentuser.admin
                
                return redirect(f"/user/home/{currentuser.first_name}")
    
    return render_template('Loginhome.html', form = form)

#logout
@app.route('/logout')
def logout():
    
    session.pop('lab_id')
    session.pop('first_name')
    session.pop('last_name')
    session.pop('admin')
    
    
    return redirect('/')
#userhome
@app.route('/user/home/<name>' , methods= ['GET', 'POST'])
def userhome(name):
    curruser = Tech.query.filter_by(first_name = name).first()
    form = Edituser(obj = curruser)
    
    #total number samples that haven't been processed
    count = 0 
    for num in curruser.projects :
        count += num.num_samples
   # number of tasks that have been completed by user
    tt= db.session.query(Task).filter_by( lab_id = curruser.lab_id).filter_by(complete = True).all()
    count2 = 0
    for task in tt:
        count2 += task.project.num_samples
    if form.validate_on_submit():
        
        curruser.first_name = form.first_name.data
        curruser.last_name = form.last_name.data
        curruser.avatar = form.avatar.data
        db.session.commit()
        return redirect(f'/user/home/{curruser.first_name}')   
            
    return render_template('userhome.html', curruser = curruser, form = form, count = count, count2 = count2)

################################## ---USER -- ###########################
@app.route('/admin')
def admintab():
    '''admin dashboard'''
    users = Tech.query.all()
    projects = Project.query.all()
    tasks = Task.query.all()
    
    return render_template('admintab.html', users = users, projects = projects,tasks = tasks )

@app.route('/user/edit/<first_name>', methods = ['GET', 'POST'])
def edituser(first_name):
    '''edit user using first name'''
    if 'first_name' not in session:
        
        return redirect ('/')
    
    
    if session['admin'] or first_name == session['first_name']:
        user = Tech.query.filter_by(first_name = first_name).first()
        form = Edituser(obj=user)
        print('working ')
        
        
    
        if form.validate_on_submit():
            
            user = Tech.query.filter_by(first_name = first_name).first()
            
            
            print('fist ----admin-----', user.admin)
            user.first_name = form.first_name.data
            user.last_name = form.last_name.data
            user.avatar = form.avatar.data
            user.admin = form.admin.data
            print('2nd ----admin-----', user.admin)
            
        
        
            
            db.session.commit()
            
            
            
            return redirect('/admin')
            
            
        return render_template('edituserform.html', form = form, user=user )
    
    else:
        print('didnt work ')
        return redirect(f"/user/home/{session['first_name']}")
    
    
@app.route ('/user/delete/<last_name>', methods=['POST'])
def deleteuser(last_name):
    '''delete user by last_name'''
    if 'first_name' not in session:
        
        return jsonify(message = 'Not allowed sign in')
    
    
    if session['admin'] and last_name != session['last_name']  :
        print('------ all adds up', )
        data = request.json
        
        data = data['lab_id']
        lab_id = data['id']
        print('-------=========-----labid axios', lab_id)
       
        techs =Tech.query.filter_by(last_name = last_name).all()
        for tech in techs:
            if tech.lab_id == lab_id :
                
            
                db.session.delete(tech)
                db.session.commit()
                return jsonify(message = 'deleted')
    else:
        return redirect('/')
    
################################## --PROJECT-- ##########################
#Project home
@app.route('/projects')
def allprojects():
    ''' all projects'''
    allprojects = Project.query.all()
    
    
    return render_template('allprojects.html', allprojects = allprojects)

#create a project
@app.route('/createproj' ,methods = ['GET', 'POST'])
def createproj():
    '''add project'''
    
    allfreezers = Freezer.query.all()
    freezer = [(i.freezer_name, i.freezer_name ) for i in allfreezers]
    form = Projform()
    form.freezer.choices = freezer
    
    if form.validate_on_submit():
            quote_id = form.quote_id.data
            company = form.company.data
            sample_type = form.sample_type.data
            num_samples = form.num_samples.data
            process = form.process1.data
            location = form.freezer.data
            
            newproject = Project(quote_id = quote_id, company = company, sample_type =sample_type, num_samples = num_samples, process = process, freezer_name = location)
            db.session.add(newproject)
            db.session.commit()
           
            return redirect('/projects')
    return render_template('projform.html', form = form, freezers = allfreezers)



# single project detail page 
@app.route('/projects/<projid>')
def projinfo(projid):
    ''' view one project by id'''
    projid = int(projid)
    
    proj = Project.query.get(projid)
    
    return render_template('projectdetail.html', proj= proj)


@app.route('/projects/edit/<id>', methods = ['GET', 'POST'])
def editproject(id):
    ''' edit one project by id '''
    id= int(id)
    project =  Project.query.get_or_404(id)
    form = Projform(obj = project)
    allfreezers = Freezer.query.all()
    freezer = [(i.freezer_name, i.freezer_name ) for i in allfreezers]
    form.freezer.choices = freezer
    
    if form.validate_on_submit():
        
        project.quote_id = form.quote_id.data
        project.company = form.company.data
        project.sample_type = form.sample_type.data
        project.num_samples = form.num_samples.data
        project.process = form.process1.data
        project.freezer_name = form.freezer.data
        
        db.session.add(project)
        
        db.session.commit()
        
        return redirect(f'/projects/{project.quote_id}')
        
    
    return render_template ('projectedit.html', form = form )

@app.route ('/projects/delete/<projid>', methods=['POST'])
def deleteproject(projid):
    ''' delete project '''
    projid = int(projid)
    Project.query.filter_by(quote_id = projid).delete()
    db.session.commit()
    
    return redirect('/projects')


################################## --TASKS-- ###########################
#all tasks page admin
@app.route('/tasks')
def edittasks():
    '''all tasks'''
    alltasks = (db.session.query(Task).all())
    
    return render_template('alltasks.html', alltasks = alltasks)

#create tasks
@app.route('/createtask', methods= ['GET', 'POST'])
def createtask():
    ''' create a task'''
    form =  Tasksform()
    allproj = (db.session.query(Project.quote_id).all())
    alltechs = (db.session.query(Tech.lab_id, Tech.first_name, Tech.last_name).all())
    projects = [(p.quote_id, p.quote_id ) for p in allproj]
    tech = [(t.lab_id, t.first_name ) for t in alltechs]
    
    form.lab_id.choices = tech
    form.quote_id.choices = projects
    if form.validate_on_submit():
            quote_id = form.quote_id.data
            quote_id = int(quote_id)
            lab_id = form.lab_id.data 
            kit = form.Kit.data
            task = form.task.data
            
            print('-------------------------------')
            print(quote_id)
            print(lab_id)
            print(kit)
            print(task)
            print('-------------------------------')
            
            newtask = Task(quote_id = quote_id, lab_id= lab_id, kit = kit, task = task)
            db.session.add(newtask)
            db.session.commit()
            
            return redirect(f'/tasks/{newtask.task_id}')
    
    return render_template('taskform.html', form = form)



#one task detail
@app.route('/tasks/<taskid>')
def taskinfo(taskid):
    ''' get single task '''
    taskid = int(taskid)
    
    task = Task.query.get_or_404(taskid)
    
    return render_template('taskdetail.html', task= task)

@app.route('/task/edit/<id>', methods = ['GET', 'POST'])
def edittask(id):
    ''' edit a task'''
    id= int(id)
    task =  Task.query.get_or_404(id)
    form = Tasksform(obj = task)

    
    allproj = (db.session.query(Project.quote_id).all())
    alltechs = (db.session.query(Tech.lab_id, Tech.first_name, Tech.last_name).all())
    projects = [(p.quote_id, p.quote_id ) for p in allproj]
    tech = [(t.lab_id, t.first_name ) for t in alltechs]
    
    form.lab_id.choices = tech
    form.quote_id.choices = projects
    if form.validate_on_submit():
        
        task.quote_id = form.quote_id.data
        
        task.lab_id = form.lab_id.data
       
        task.kit = form.Kit.data
        task.task = form.task.data
        
        db.session.add(task)
        
        db.session.commit()
        
        return redirect(f'/tasks/{task.task_id}')
        
    
    return render_template ('taskedit.html', form = form )


    
    

@app.route ('/tasks/delete/<taskid>', methods=['POST'])
def taskdelete(taskid):
    ''' delete task '''
    task = int(taskid)
    Task.query.filter_by(task_id = taskid).delete()
    db.session.commit()
    
    return redirect('/tasks')

    
    
@app.route('/task/complete/<taskid>', methods = ['POST'])
def complete(taskid):
    '''mark task complete '''
    taskid= int(taskid)
    
    
    task = Task.query.get_or_404(taskid)
    task.complete = True
    
    db.session.add(task)
    db.session.commit()
    taskjson = {
        "task_id": task.task_id,
        "todo": task.task,
        'company': task.project.company
    }
    return jsonify(message = 'marked complete', task =taskjson)
    

    
    
    
    
    
    
    







    

    
    

