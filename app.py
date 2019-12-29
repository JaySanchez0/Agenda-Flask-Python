from main import app,db
app.run()
db.create_all()
db.session.commit()