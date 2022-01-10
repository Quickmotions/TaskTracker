try:
    selected_group = input("Group ID: ")
    if selected_group in team.groups:
        selected_user = input("Member ID: ")
        if selected_user in team.users:
            selected_user = team.users[selected_user]
            team.groups[selected_group].members.append(selected_user.id)
            print(f"Added {selected_user.name} to {team.groups[selected_group].name}")
        else:
            print(f"Unable to find user with ID: {selected_user}")
            return
    else:
        print(f"Unable to find group with ID: {selected_group}")
        return

except Exception as e:
    print(e)