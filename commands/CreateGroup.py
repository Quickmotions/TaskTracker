if len(args) > 0:
    group_name = args[0]
    if group_name not in team.groups:
        # new_group = Group(lead=user, group_name=group_name)
        # team.groups[new_group.id] = new_group
        # print(f"Created Group: {new_group.name} with ID: {new_group.id}")
        return
    else:
        print(f"Group named: {group_name} already exists")
print("Specify the name of the group as:\n"
      "cg (group name)")
