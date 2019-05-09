#Shawn Wright
#3/5/19
#MP41
def main():


    with open("loginInfo.txt","w") as outfile:
        title = "Student Login Information"
        firstN = "first"



        outfile.write(title.center(79) +  "\n" + firstN.ljust(10) + "\n" )
        with open("studentInfo.txt","r") as infile:
            email = "@student.faytechcc.edu"

            for line in infile:
                ln = line[0:10]
                fn = line[10:20]
                identification = line[20:28]
                lname = line[0:7]
                lname = lname.rstrip(" ")
                fi = line[10:11]
                last4 = line[24:28]
                username = lname.lower()+ fi.lower()+ last4
                outfile.write(ln + fn + identification.ljust(10) + username.ljust(15) + username + email+"\n" )






main()
