try:
    new_member = create_user(permission_level=input("Permission Level\n"
                                                    "(0=root, 1=lead, 2=user\n"
                                                    ">>> "))
    team.users[new_member.id] = new_member
    print(
        f"Created: {new_member.name} with ID: {new_member.id} and permission level: {new_member.perm_lvl}")
except Exception as e:
    print(e)
