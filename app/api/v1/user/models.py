from uuid import uuid4
from datetime import datetime
from marshmallow import fields, Schema, validates_schema
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID

from app.core.db import db
from app.utils.types import JSON
from app.utils.validators import validate_unique_field

class User(db.Model):
    id = Column(UUID(as_uuid=True), primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    fullname = db.Column(db.String(120), nullable=False)

    def __init__(self, id=None, fullname=None, email=None):
        self.fullname = fullname
        self.email = email

        if not id:
            id = uuid4()
        self.id = id
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at

    def __repr__(self):
        return "<User %r>" % self.fullname



class UserSchema(Schema):
    id = fields.Str(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)

    @validates_schema
    def validate_unique_fields(self, data: JSON, partial: bool, many: bool) -> None:
        """Valdiate username and email to make sure they are unique."""
        id = None
        if "user" in self.context:
            id = self.context["user"].id

        username = data.get("username")
        validate_unique_field(User, "username", username, id)
        email = data.get("email")
        validate_unique_field(User, "email", email, id)
