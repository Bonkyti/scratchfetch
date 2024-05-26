import scratchattach as scratch3

session = scratch3.Session(".eJxVkLFOwzAQht8lMwQ7dpy6G5SqIAQDFQNdorN9bkwSO0pcFYF4d2ypS4db_v_03af7LU4Lzh5GLNbFdtjDACN4M4fipoihR59ioNoAs2kQOayk1NAoTZQBTSipxbp7OrDN98cUXh43xO72u2USr89kq6hOmCEcnb91UyJRJkvelDUvKU9NC6fYtVmgdSbXVUXEilcsdeYL_DG00Y34E3y2ux9xdhru3vDcfoa5vwZ0sHRpqaFUNCBYrWqbdK2gRlgJWjbMAicNr2SlhM5eEZeoQ-hdhp8TEM01UoFOD8hiOUMf0_Xogi8vxVK-4zRcwofL8t8_icFt2g:1s3CT9:pbX8QrIIVEkuE_W6i0huXsG4xt8", username="ElSalamandro") #replace with your session_id and username
conn = session.connect_cloud("1013682348") #replace with your project id

client = scratch3.CloudRequests(conn)

@client.request #Project
def pro(argument1):
    print(f"Data requested for project {argument1}")
    project = scratch3.get_project(f"{argument1}") # Warning: Any methods that require authentication will not work on the returned object

    return_data = []


    return_data.append(f"{project.title}")
    return_data.append(f"by: {project.author}")
    return_data.append(f"{project.created}")
    return_data.append(f"{project.share_date}")
    return_data.append(f"{project.loves} loves")
    return_data.append(f"{project.favorites} favorites")


    return return_data

@client.request #less user
def foo(argument1):
    print(f"Data requested for user {argument1}")
    user = scratch3.get_user(argument1)
    stats = user.stats()

    return_data = []


    return_data.append(f"{argument1}")
    return_data.append(f"Joined: {user.join_date}")
    return_data.append(f"{user.about_me}")
    return_data.append(f"{user.wiwo}")
    return_data.append(f"{user.country}")


    return return_data

@client.request #more user
def more(argument1):
    print(f"Data requested for user {argument1}")
    user = scratch3.get_user(argument1)
    stats = user.stats()

    return_data = []


    return_data.append(f"Messages: {user.message_count()}")
    return_data.append(f"Fllowers: {user.follower_count()}")
    return_data.append(f"Following: {user.following_count()}")
    return_data.append(f"Projects: {user.project_count()}")


    return return_data




@client.event
def on_ready():
    print("Request handler is running")

client.run() #make sure this is ALWAYS at the bottom of your Python file