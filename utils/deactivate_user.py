import requests 

URL= "http://127.0.0.1:5000/users"

def deactivate_user(id):


    url = URL + "/" + id
    response= requests.delete(url)
    if response.status_code == 204:
        print(
            "Successfully deactivated user; Got: %d" % id
        )
    else:
        print(
            "Something went wrong while trying to deactivate user. id: %d" % id
        )

# if __name__ == "__main__":
#     fname= input("Type in the user's first name: ")
#     lname= input("Type in the user's last name: ")
#     hobbies= input("Type in the user' hobbies: ")
#     create_user(fname, lname, hobbies)
