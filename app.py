def login(user):
    if user == "admin":
        return "Welcome Admin"
    return "Access Denied"

print(login("admin"))
