from flask_restful import Resource

from app.utils.response import success, error

from .models import User, UserSchema


class UserResource(Resource):
    def get(self):
        users = User.query.all()
        return success(
            data=UserSchema(many=True).dump(users), message="Users fetched successfully"
        )


class SingleUserResource(Resource):
    def get(self, id):
        user = User.query.get(id)

        if user is None:
            return error(message="User not found", status=404)

        return success(
            data=UserSchema().dump(user), message="User feteched successfully"
        )
