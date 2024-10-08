class Instagram:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        if user not in self.users:
            self.users.append(user)

class User:
    def __init__(self, name, telephone):
        self.name = name
        self.telephone = telephone
        self.followers = []
        self.following = []

    def follow(self, user):
        Ig = Instagram()
        if user not in Ig.users:
            self.following.append(user)
            user.followers.append(self)
            print(f"{self.name.title()} seguiu {user.name.title()}")
        else:
            print("Usuário não encontrado")

    def unfollow(self, user):
        Ig = Instagram()
        if user not in Ig.users:
            self.following.remove(user)

        else:
            print("Usuário não encontrado")

    #def remove_folower(self, follower):



ig = Instagram()
user1 = User("Alen", 1)
user2 = User("jeff", 2)
user3 = User("zuck", 3)

ig.add_user(user1)
ig.add_user(user2)
ig.add_user(user3)


user1.follow(user2)
user2.follow(user1)
user3.follow(user1)
user3.follow(user2)

print(f"{user1.name.title()} folowers: {user1.followers} following:{user1.following}")
print(f"{user2.name.title()} folowers: {user2.followers} following:{user2.following}")
print(f"{user2.name.title()} folowers: {user2.followers} following:{user2.following}")



