users = [
    {
        "username" : "misocho",
        "email" : "misochobrian@gmail.com",
        "password" : "scorpion234"
    },
    {
        "username" : "ben",
        "email" : "karanjaben@gmail.com",
        "password": "dsjknvujfnuihdf"
    }
]

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

    def get_user_data(self, username):
        user = [user for user in users if user["username"] == username]
        return user

    def edit_username(self, username):
        user = [user for user in users if user["username"] == username]
        return user