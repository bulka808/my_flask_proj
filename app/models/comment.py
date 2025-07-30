from app import db

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000), nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Comment {self.name}>'