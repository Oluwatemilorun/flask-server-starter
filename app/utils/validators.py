from uuid import UUID
from typing import Optional

from marshmallow import ValidationError

from app.core.db import db

def validate_unique_field(
    model: db.Model, name: str, value: Optional[str], id: Optional[UUID] = None
) -> None:
    """Validate unique field.

    Args:
        name: field name to validate ('username' or 'email')
        value: value to validate
        id: optional user id, should be specified on user update

    Returns:
        Nothing, raises ValidationError if validation failed.
    """
    query = model.query.filter(getattr(model, name) == value)
    if id is not None:
        # Allow updating username or email for the user to the
        # same value.
        query = query.filter(model.id != id)
    if query.first():
        raise ValidationError("{} should be unique: {}".format(name, value), name)
