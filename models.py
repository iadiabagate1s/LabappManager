from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db= SQLAlchemy()
bcrypt = Bcrypt()

def connect_db(app):
    db.app = app
    db.init_app(app)

default_ava = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOsAAADXCAMAAADMbFYxAAAAqFBMVEX+/vYSFBMAAAD///////z///sTExXCw8EUFhX+/ff///f+/vQbGxyysrAbGxr7+/TOzs3e390NEA/t7eoJCQvW1tL19u6IiIjIyMl1dXWampnz8/GAgIBvb25EREUSFROlpaa5ubcyMjJiYmLj4+IiIiJpaWhXVlVOT00/Pz0qKint7eYzMy/v7/A/P0CTk5EkJCAODRXh4tuIiYXT09Sqq6d8fHxcW1xdQRJsAAALKUlEQVR4nO1df1siOw9lkhamncXAMIzKqAsCirCr970qfv9v9iYdQOWHeu/VZag9+4eK8+zTY9LktGkztVpAQEBAQEBAQEBAQEBAQEBAQEBAQEDAlyNh7HsMfwr0jbharc2+x/BHQFTTzaZmT973SP4ASJ0DnKvvwbWYpilo+hZc8QzgGIWrtTXPfdnqRkNTbpQm0or8jslkDEco6t0ATO9R5/sez5dCmM5+QVavZwBdve/hfDEMXsDPSJDCb7vv0XwtsA9xVALO1L5H87XA22xBlQ2L+x7N1wJhSTWOYGS8DsXPXKPYe663Wfzsw35rKNWEunNgNqvvsalmLhdeDFnHz5xjjdaOmbWdMaRplEG9rTzkmuSkHvqDGctgFk7G9G4yuDzOLe17YF+ARLXGwLhD4cpzFjszXHzvG0xD4lEcwxU6eiT/SL56B6vGaRl6oaVIdhNzKgn7B9OFtMypcI7GcTWIxsPAVKvpx6VWgqE4MZFqHqUDH6NwTTcgipdc+WdDbc460NYeOrHtLJdx0JT5KrGKVVPDeMi1hsdQav1IlXG4Ixlo5KNdaxpPAVKA8Wix66//Hl61FEspMa1f05bItE5vJo96tcFkEVlQNLqFdwGqTDKoXwglIn0sjjzwbWsiSRJLRq/2DUUW451b27G62OvQvgKJxUeOvDXZ/TciEItSX8DEN8OKaVVrKOtVUr2b6wbaLiz2Jop9D+3TkSRGOQuy78o2uFpynea+RadnIPtuDHNUv9x6gBXyvkf0dcCMOcIx6i6n3AjSwttCh5TWJdW0dU2Phmk6L7wUikxUZqbBxtXpSPaeFKdc9C/jOOjisTcoOLVq40SFIePnNgxTa8fsvJeFbLCxiTnJWk+Zcl4dQxxHcMFSwrKNu94p4WcsxEMMHI2MzX/A3NOpKhK4BbGoQmjzLJWEE/ubWM0IopjhzvxYujpqeptYWfKfsnZIoVee5VLaX6qSWHtT+PXIoUm4+pptFjBIHa3KXRjrZzHnGc6Wix0nNfC0IFkiKeG+twX0lxPWr9J6nsh202t0yi+sF/06qkemczyFbRg20fh1Ug9bW4k63I48OilOhG2Aca+1BYNzXrB7dVIPr3l5g5rlwxpUTfGf4cofYUykAE4U5ZvFDJuQbgCQP4YlFvqjXZVl+xt4NeBLKLamw3R2mc6OADr+nNQjBJjjdrIW5zD26baDegQ4LraJfSqOAR79iU1ypeEJ4Ag3uVodA0z82owhfbqD6xHc+1ZdVwPm+uqTRHZOE/UDGsqfyeqgmmtcE6JBQxMK130N6ouwwVXKddAw6ltwVacSgL8HV1M8zXX+LXxYThTrWvItuNYSOWVqv4cPLz4PXA8agWvgeuh4yTV50T3Ed65ElpLF2sZzroRqtOoe4jdXg8dTmPawJOszV5urIaRpCqdYXsDymGuNBhBHR1G86EHgNVecy/WVWA4kem9Xc744+XPnPVeyTcf1J5xo37nWSP8Fchj8qTw34TdXml2DNHEq94R95ipnQ3DUnanvoJuoRkZbS7n/dl1hUdb4FlyXnweuhwzSb3H1q3b1Jlfv6nR3kG7lWvfuoqQZwUIArwEv4Mivw7VW3cCl2XYoQi5zX3llWHwEeNBr53qkG6TNdR98isSJdh788pOENM4MUmLlTNv/Ov6cg1EXMH41J5McW5P4ci4R2HYy8WI/yFrsSdfHV2R0C7Isg2s5zIYDgIEX9xzYXdmD79f0Ak7cip1zq6x7hgCoPTiml+fM64euvUosNi9brsGdEp3xG2CIHnA1yIG2pV7fULE0dv0g5a4OT151AtBED7iyB59tJFDpmRJHdSivclg8B+gcvqLAGxib9avLZOjiZR8NUwA8HbyiEBXRonzNPZPE6JN+f7RQjSZXDfHiPYzv85DoGcDpFg6JtMNRq6u+SenFtUPuvkAcg8cfajVmVQY3eMiXV5wHf8xWmmNx/2C9mCdlRzx46adb8fw7aRE/0gd6ByshdQ3jfNUYcBfR5dM4hgu1deFXfRhsApywWY0VbNzN0VopZYyxxvA32ugHYG1xmOHJ/BYPVp1u+yW6D69+7nb/nnXdJ4VhgcFevO9h/xtYfIKMCazdnjtvnb26Otie5Z2BfHetSE3h9iDDkxIPVuoe6ssu0k4Bo8GLZW90V4TlaatGP1gvNq1ur63pDwOJcSpCdyF6BUCFt+nyhwm6dweRknYMMDOy0m3rA1u325w9GExN32RrXIeNOfNaNYYsHyeU7kZPSOoSLtWh7StKDG6Q7q2ZNYoygChaNsFsLyIRqTkIdW3asDhIcShIFjE4absl+SvEcdkW3XHtLk50JXjuiu0dd+Ph4ZDI5oTXUC+0nSxbtr6gyhMTspLsyoelL5n8fI2ElzDGA6rw5OLBA6X7Gx4cxT+zy35/WrZyzaaLi6/8vLO13KwbyT3Dw+FabiDZYsOqjPRWenGNXWvEOrNCbWvYXnb8h451ezaHoygkBhPhcNOsnFKbyAl1aXG4PRl12veQ/nzOQqyiMzyU6/qKdVBD28ZmYHJzlMUCc130D+fJGwHESweosxeT8+J9k/gQEpu7LdB8i1XL+KOUk07xIiyn9ee/CU/ZmZLZ3jqMF7vpK8g60sBoK1eWDCcNic9HIoKz6PWU/iktyiSKZ1tvBlcNpsEx2Km+7Vwj4Shfhq1242bjDxLzuo4Kyc5Vn7Lsd4UUVK35K9tCc+mosWt8iTXNGiJe+10dRmQGZaGy0m7MKuIK4Dep411mjUvhlF4q1z073wxg6S2v7q5Yi1S86kFl0c10d1IVD06X7zSQrfIN+7MXI3UyXgpU24uVUxGJXi3b1gEXI+xepsLVBZ9Nruzh0CbJW4Nqyydp9z4j3FzerLiOtBRco/SXknsrttg2rbMpihKpdonHlSpE0u6KwbxWJzIdWcD1sKakFf62R+EOcwXwVOFmDDY/4lmW6+s3uLbQoHs7B5y3isb2J+sx/E2yOd6s7KGR3BVlEtXc6cEcZNPGQ7OczLBItJuQpqcci0/FiyvqxmKJR80hVPTPDhyluwi+4hpBH00xls3FfbPaClvUYaIkwb7JI3YZdkFpJ1hRGF3RQiWnfYnBv4kl4k6jvmT83hNs0lWJZ9/k1uHKxY/K5D92pdZnZO96sUzZgSGdsadUr594IR6MuSSRd2yWwmQepe8aNoKCrJR4qiefxN9mckbrXQ/mJQyOtq7j1547Y0VRxRIPk4RHNutfH+Aw4AA23L0Men6wTVLiuahaeMKJbBXh/UfsNUcz+8BzdU6ySa0L7nBbhSBVpy5RF94PTBJi78bZ+/NVwpMuWytWacaSbHS6fewPUI1jWdV9hGs6VsYOpM1edUIx59YrOFZbqje7WLwtJFbPyQKhkPaJ+2b4AoRPPKzRB6ku6UbvWjfNOqb4IcFs3wyfQWrCAvajZl2BxfE7bKWb1WXFego6ux7/U67ZpAdvioo63CmVVeq2UpLwfD3DAdQ/IIWfEUNjax3k5RNd5eZrlbjK4Qg0E3nj0T8gW5/O33BijsMwN6YJcZVyTpLojmzoqrt0d/vof4G4ryxHgius0C20hCTpjA2pjQbo/w3KyB7sQ6VCEy/U219SXJObPZU7RJ1IK9ozpT91489iuy7nwT7z//wU4Bzgpst+J8cMPwFaIfHfD1oVmqwlLMkBH4CLXuOzMDitA4y71XtPFLnO9hefGoYZZ7mu4PtY3DvEsX0/rX8WsmG/QJtU9cXkRn9uzqleVHqBhBLzWaBapeuvcrDd2k/KO+un5AMCAgICAgICAgICAgICAgICAgICAgICAgICAg4R/weUubMDfjGbVQAAAABJRU5ErkJggg=='
    
#models 
class Tech(db.Model):
    '''lab tech model '''
    __tablename__= 'labtechs'
    
    lab_id = db.Column(db.String, primary_key=True )
    first_name = db.Column(db.Text, nullable = False )
    last_name = db.Column(db.Text, nullable = False )
    admin = db.Column(db.Boolean, nullable = True, default = False)
    avatar = db.Column(db.Text, nullable = True, default = default_ava)
    
    
    task = db.relationship('Task',cascade="all,delete", backref = 'tech')
    projects = db.relationship('Project', secondary="tasks", backref='techs')
    
    @classmethod
    def register(cls,lab_id,first_name, last_name, avatar):
        """Register user w/hashed password & return user."""

        hashed = bcrypt.generate_password_hash(lab_id)
        # turn bytestring into normal (unicode utf8) string
        hashed_utf8 = hashed.decode("utf8")

        # return instance of user w/username and hashed pwd
        newtech = cls(lab_id=hashed_utf8,first_name = first_name, last_name = last_name, avatar = avatar)
        db.session.add(newtech)
        return newtech
    
    @classmethod
    def authenticate (cls, last_name, lab_id):
        '''Return user if valid; else return False.'''
        """Find user with `username` and `password`

        This is a class method (call it on the class, not an individual user.)
        It searches for a user whose password hash matches this password
        and, if it finds such a user, returns that user object.

        If can't find matching user (or if password is wrong), returns False.
        """

        techs = cls.query.filter_by(last_name=last_name).all()
        
        print('-----------user', techs)
        for tech in techs:
            is_auth = bcrypt.check_password_hash(tech.lab_id, lab_id)
            if is_auth:
                print('tech--------------',tech)
                return tech
        print('wrong user ', )
        return False
    
    
class Freezer(db.Model):
    __tablename__ = "freezers"
    
    freezer_name = db.Column(db.Text,primary_key=True)
    
    
        

class Project(db.Model):
    '''Project Model'''
    __tablename__ = 'projects'
    
    quote_id = db.Column(db.Integer, primary_key = True)
    company = db.Column(db.Text, nullable= False )
    sample_type = db.Column(db.Text)
    num_samples = db.Column(db.Integer, nullable = False)
    process = db.Column(db.Text, nullable = False)
    freezer_name= db.Column(db.Text, db.ForeignKey('freezers.freezer_name'))
    
    task = db.relationship('Task',cascade="all,delete", backref = 'project') 
    
    
class Task(db.Model):
    '''Task Model '''
    __tablename__ = 'tasks'
    
    task_id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    quote_id = db.Column(db.Integer,db.ForeignKey('projects.quote_id', ondelete = 'cascade'), nullable= False )
    lab_id= db.Column(db.String, db.ForeignKey('labtechs.lab_id'))
    kit = db.Column(db.String)
    task = db.Column(db.String)
    complete = db.Column(db.Boolean, nullable = False, default= False)
    
    
    
