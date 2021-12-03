def success(data, message="operation successful", status=200):
    """
    Formatted success response method for easy access
            :return: object, int
    """

    return {"message": message, "data": data, "status": status}, status


def error(errors=[], message="Error occured. Try again later", status=500):
    """
    Formatted error response method for easy access
            :return: object, int
    """

    return {"message": message, "errors": errors, "status": status}, status
