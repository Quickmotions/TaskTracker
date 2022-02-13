if len(args) > 0:
    group_id = args[0]
    if group_id in team.groups:
        user.current_group = team.groups[group_id]
        print(f"Now editing {user.current_group.name}")
        return
print("Unable to find group\n"
      "Specify the id of the group as:\n"
      "eg (group id)")
