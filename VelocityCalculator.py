def sprint(x):
    if x == 1:
        y = 5
    elif x == 2:
        y = 10
    elif x == 3:
        y = 15
    else:
        y = 20
    return y

def velocity_calc(): 
    run_calc = True
    
    while run_calc:
        hours_per_day = 6
        
        calc_question = input("\nWhat do you want to Calc? (V=Velocity, T=New Team Velocity, S=New Sprint Size, Q=Quit) ")
        if calc_question.lower() == 'q':
            run_calc = False
            print("\nEnd")

        elif calc_question.lower() == 'v': 
            try:
                velocity = float(input("Sprint Velocity: "))
            except ValueError:
                print("Not a Valid number")
                velocity = float(input("Sprint Velocity: ")) 
            try:
                total_team_members = float(input("Total Team Members in New Sprint: "))            
            except ValueError:
                print("Not a Valid number")
                total_team_members = float(input("Total Team Members in New Sprint: "))            
            try:
                sprint_length = int(input("How Long is Your Sprint (1-4 Weeks)? "))           
            except ValueError:
                print("Not a Valid number")
                sprint_length = int(input("How Long is Your Sprint (1-4 Weeks)? "))   
            try:
                total_days_out = float(input("Total Days Out: "))            
            except ValueError:
                print("Not a Valid number")
                total_days_out = float(input("Total Days Out: "))  
            try:
                average_injections = float(input("Average Injections Per Sprint: "))           
            except ValueError:
                print("Not a Valid number")
                average_injections = float(input("Average Injections Per Sprint: "))  
            try:
                average_injection_effort = float(input("Average Injection Effort (recommend a 2 if unknown): "))           
            except ValueError:
                print("Not a Valid number")
                average_injection_effort = float(input("Average Injection Effort (recommend a 2 if unknown): "))
            try:
                additional_hours = float(input("How Many Additional Hours Subtracted for This Sprint (deploys, meetings, etc.)? "))            
            except ValueError:
                print("Not a Valid number")
                additional_hours = float(input("How Many Additional Hours Subtracted for This Sprint (deploys, meetings, etc.)? "))  
            try:
                rollover_points = float(input("How Many Rollover Points this Sprint? "))           
            except ValueError:
                print("Not a Valid number")
                rollover_points = float(input("How Many Rollover Points this Sprint? "))  

            sprint_day_count = sprint(sprint_length)
            sprint_hours = float(sprint_day_count) * float(hours_per_day) * float(total_team_members)
            hours_per_point = float(sprint_hours) / float(velocity)
            injection_points = float(average_injections) * float(average_injection_effort)

            total_hours_out_per_sprint = float(total_days_out) * float(hours_per_day) + float(additional_hours)
            total_days_out_per_sprint = float(total_hours_out_per_sprint) / float(hours_per_day)
            velocity_per_person_per_day = float(velocity) / (float(sprint_day_count) * float(total_team_members))
            plan_for = float(velocity) - (float(total_days_out_per_sprint) * float(velocity_per_person_per_day)) - float(injection_points) - float(rollover_points)
            
            print(f"""
    Numbers You Chose For Your Sprint:
        Velocity: {velocity}
        Team Size: {total_team_members}
        Sprint Length: {sprint_length} Weeks
        Total Days Out: {total_days_out}
        Injections: {average_injections}
        Additional Hours: {additional_hours}
        Rollover Points: {rollover_points}

    Calculations for Your Sprint:
        The Hours-Per-Point Will Be: v
        {hours_per_point}
        Total Points Used for Injections: {injection_points}
        Total Hours Out for the Team: {total_hours_out_per_sprint}
        If Using a 6 Hour Day of Total Development, Total Days Out: 
            {total_days_out_per_sprint}
        Velocity-Per-Person for This Sprint: {velocity_per_person_per_day}
        
    Plan For {round(plan_for)}, Total for the Sprint Would Be {round(plan_for) + round(injection_points) + round(rollover_points)}
            """)

        elif calc_question.lower() == 't':
            try:
                current_velocity = float(input("Current Velocity: "))           
            except ValueError:
                print("Not a Valid number")
                current_velocity = float(input("Current Velocity: "))  
            try:
                old_team_count = float(input("Team Members in Previous Sprint: "))           
            except ValueError:
                print("Not a Valid number")
                old_team_count = float(input("Team Members in Previous Sprint: ")) 
            try:
                new_team_members = float(input("Total Team Members in New Sprint: "))           
            except ValueError:
                print("Not a Valid number")
                new_team_members = float(input("Total Team Members in New Sprint: ")) 

            determine_velocity = float(current_velocity) / float(old_team_count)
            new_velocity = float(determine_velocity) * float(new_team_members)
            print("Use " + str(round(new_velocity)) + " for your Velocity")

        elif calc_question.lower() == 's':
            try:
                current_velocity = float(input("Current Velocity: "))          
            except ValueError:
                print("Not a Valid number")
                current_velocity = float(input("Current Velocity: ")) 
            try:
                team_count = float(input("Team Members in Previous Sprint: "))           
            except ValueError:
                print("Not a Valid number")
                team_count = float(input("Team Members in Previous Sprint: ")) 
            try:
                old_sprint_length = float(input("How Long is Your Old Sprint (1-4 Weeks)? "))           
            except ValueError:
                print("Not a Valid number")
                old_sprint_length = float(input("How Long is Your Old Sprint (1-4 Weeks)? ")) 
            try:
                new_sprint_length = float(input("How Long is Your New Sprint (1-4 Weeks)? "))           
            except ValueError:
                print("Not a Valid number")
                new_sprint_length = float(input("How Long is Your New Sprint (1-4 Weeks)? "))             
            
            velocity_per_day_per_team_member = float(current_velocity) / float(team_count) / float(old_sprint_length)
            new_velocity = float(velocity_per_day_per_team_member) * float(team_count) * float(new_sprint_length)
            print("Plan For " + str(round(new_velocity)) + " for your Velocity")
            
        else:
            print("\nThat's not a V, T, S or Q...try again")

velocity_calc()
