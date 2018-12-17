users = []

class User_Accounts(object):
    """  Creates user accounts model """

    def register_user(self, username, email, password):
        ''' method to register user '''
        user = dict(
            username = username,
            email = email,
            password = password
        )


        users.append(user)
        return users, {
            "message" : "registration was successfull"
        }