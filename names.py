pupil_name = " " #variable to store the name of a pupil

count = 0       #variable set to 0 to count the total names entered by the user

#loop until the value of pupil_name is Stop

while pupil_name != "Stop":

    #input for the name of the pupil

    pupil_name = input("Enter the name of a pupil: ")

    #if the name is not Stop, increase the count by 1

    if pupil_name != "Stop":

        count = count + 1

#print the value of the count

print("The total number of pupils is: ", count)