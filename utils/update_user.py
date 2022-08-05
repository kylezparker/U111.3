import requests 

URL= "http://127.0.0.1:5000/users"

def update_user(id, first_name, last_name, hobbies):
    user ={
        "first_name": first_name,
        "last_name": last_name,
        "hobbies": hobbies
    }
    url = URL + "/" + id
    response= requests.put(url, json=user)

    if response.status_code== 204:
        print("ok")
    else:
        print("something went wrong")




#     if response.status_code == 201:
#         print(
#             "Successfully created new record; Got: %s"
#             % response.json().get("message")
#         )
#     else:
#         print(
#             "Something went wrong while trying to create a new user."
#         )

if __name__ == "__main__":
    user_id= input("Type in the user's id: ")
    fname= input("Type in the user's first name: ")
    lname= input("Type in the user's last name: ")
    hobbies= input("Type in the user' hobbies: ")
    update_user(user_id, fname, lname, hobbies)
