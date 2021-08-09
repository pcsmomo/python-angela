class User:
    # Constructor
    def __init__(self, user_id, username):
        print("new user being created...");
        self.id = user_id
        self.username = username
        self.followers = 0

user_1 = User('001', 'Noah')
# user_1.id = '001'
# user_1.username = "Noah"

print(user_1.username)
print(user_1.followers)

user_2 = User('002', 'Jack')
# user_2.id = '002'
# user_2.username = "jack"
print(user_2.id)