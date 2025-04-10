from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from flask import Flask

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"

db = SQLAlchemy(app)

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Post(db.Model):
    id : Mapped[int] = mapped_column(primary_key = True)
    description : Mapped[str] = mapped_column(String(250), unique=True,nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), primary_key=True)
    user_to = relationship('User', foreign_keys=[user_id], backref='user_to_post')

class Follower(db.Model):
    user_from_id: Mapped[int] = mapped_column(ForeignKey('user.id'), primary_key=True)
    user_to_id: Mapped[int] = mapped_column(ForeignKey('user.id'), primary_key=True)
    user_from = relationship('User', foreign_keys=[user_from_id], backref='followers_from')
    user_to = relationship('User', foreign_keys=[user_to_id], backref='followers_to')

class Comment(db.Model):
    id: Mapped[int] = mapped_column(primary_key = True)
    comment_text: Mapped[str] = mapped_column(nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey('user.id'),nullable=False)
    author_to = relationship('User', foreign_keys=[author_id], backref='author_to')
    post_id: Mapped[int] = mapped_column(ForeignKey('post.id'), nullable=False)
    post_from = relationship('Post',foreign_keys=[post_id],backref='post_from')

class Media(db.Model):
    id: Mapped[int] = mapped_column(primary_key = True)
    tipo:Mapped[str] = mapped_column(String(120),nullable=False)
    url: Mapped[str] = mapped_column(nullable=False)
    post_id_2: Mapped[int] = mapped_column(ForeignKey('post.id'),nullable=False)
    post_from_id = relationship('Post',foreign_keys=[post_id_2],backref='post_from_id')