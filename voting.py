import mysql.connector as connection
import string
import random
import re
import time
conn = connection.connect(host = "127.0.0.1", user = "root", password = "", database = "voting")
cursor = conn.cursor()

#Creating a School voting system
class voting():
    def __init__(self):
        print("\nSQI VOTING")
        self.choice = input("""Enter 1 to login
Enter 2 to register
Enter 3 to quit: """)
        if self.choice == '1':     #if statment to  allow for login
            self.log()
            self.info()
            self.vote()
        elif self.choice == '2':       #elif statment to  allow for registration into the voting system
            self.reg()
            self.log()
            self.info()
            self.vote()
        elif self.choice == '3':
            time.sleep(2)
            print("\nGoodbye and have a wonderful day!!")   
        else:
            print("Invalid Input.")     #This tells that the input is not part of the above and should re enter the correct input
            time.sleep()
            voting()

#creating a method that ask for login information
    def log(self):                  
        print("Login\n")
        self.vid = input("\nEnter your voters ID: ").strip().upper()
        self.password = input("Enter your password: ").strip()
        time.sleep(1)
        self.dep()
        self.confirm()

#creating a method that checks the login and authenticates it
    def confirm(self):
        cursor.execute(f"SELECT * FROM {self.pick} WHERE voters_id = '{self.vid}' OR pword = '{self.password}'")
        self.voter = cursor.fetchone()
        print("Processing...........")
        time.sleep(2)
        if self.voter != None:
            if self.vid == self.voter[7] and self.password == self.voter[8]:
                print("Login Successful")
                time.sleep(1)
            else:
                print("Login Failed")
                time.sleep(1)
                self.log()
        else:
            print("You have entered the wrong department or your detail does not exist.")
            self.log()
            
#A method that allows for unregistered voters to register.
    def reg(self):
        print("\nWelcome.")
        self.fname = input("Enter your First name: ").strip().title()
        self.lname = input("Enter your Last name: ").strip().title()
        self.dep()
        time.sleep(1)
        self.lev()
        self.email = input("\nEnter your Email: ")
        time.sleep(1)
        self.check_email()
        self.check = re.findall(r"^[a-z]+[0-9\.\-_a-z]*+@{1}+[a-z]+\.{1}+[a-z]+$", self.email)  #using random expression to test for email
        while not self.check:
            print("Invalid Email")
            self.email = input("Enter your Email: ")
            self.check = re.findall(r"^[a-z]+[0-9\.\-_a-z]*+@{1}+[a-z]+\.{1}+[a-z]+$", self.email)
        else:
            self.phone = input("Enter your Phone Number: ")
            time.sleep(1)
            self.check_phone()
            while len(self.phone) != 11:    #Testing if the length of the phone Number is eleven
                print("\nPhone Number not up to 11 digits.")
                time.sleep(1)
                self.phone = input("Enter your Phone Number: ")
            else:
                #generating a list of 4 randome upper case alphabets and 4 numbers
                self.letters = list("".join(random.choice(string.ascii_uppercase) for i in range(4)) + "".join(random.choice(string.digits) for i in range(4)))
                #Suhffling the randomly generated list of alphabets and numbers
                random.shuffle(self.letters) 
                #joining it back together to form a string
                self.vid = "".join(self.letters)
                time.sleep(1)
                self.check_vid()
                self.password = input("Enter desired Password: ")
                time.sleep(1)
                self.check_password() 
                self.confirm_pass = input("Confirm Password: ")
                while self.confirm_pass != self.password:   #Checks if the confirm password is the same with the actual password
                    time.sleep(1)
                    print("\nPassword is not matching.")
                    self.confirm_pass = input("Confirm Password: ")
                else:
                    cursor.execute(f"INSERT INTO {self.pick} (first_name,last_name,department,level,phone,Email,voters_id,pword,stats1,stats2,stats3) VALUES ('{self.fname}','{self.lname}','{self.choice}','{self.level}','{self.phone}','{self.email}','{self.vid}','{self.password}','Not Voted','Not Voted','Not Voted')")
                    conn.commit()
                    time.sleep(1)
                    print(f"\nYour Voter's Id is {self.vid}\nYour registration is Complete.")

#This allows to select department and give default  values so as to use in the sql querry
    def dep(self):
        self.department = input("""\nEnter 1 for Data science
Enter 2 for Data Analysis
Enter 3 for Web Development
Enter 4 for JavaScript
Enter 5 for Graphic Design and Multimedia
Enter 6 for Cyber Security
Enter 7 for UI/UX: """)
        if self.department == "1":
            self.pick = "data_science"
            self.choice = "Data Science"
        elif self.department == "2":
            self.pick = "data_analysis"
            self.choice = "Data Analysis"
        elif self.department == "3":
            self.pick = "web_development"
            self.choice = "Web Development"
        elif self.department == "4":
            self.pick = "javascript"
            self.choice = "Java Script"
        elif self.department == "5":
            self.pick = "graphics_multimedia"
            self.choice = "Graphics Designs and Multimedia"
        elif self.department == "6":
            self.pick = "cyber_security"
            self.choice = "Cyber Security"
        elif self.department == "7":
            self.pick = "uiux"
            self.choice = "UI/UX"
        else:
            print("Invalid Input.")
            time.sleep(1)
            self.dep()

#Method that as level. serves as multiple option option
    def lev(self):
        self.ask = input("""\nEnter 1 For 100 Level
Enter 2 For 200 Level
Enter 3 For 300 Level
Enter 4 For 400 Level
Enter 5 For 500 Level: """)
        if self.ask == "1":
            self.level = 100
        elif self.ask == "2":
            self.level = 200
        elif self.ask == "3":
            self.level = 300
        elif self.ask == "4":
            self.level = 400
        elif self.ask == "5":
            self.level = 500
        else:
            print("Invalid Input.")
            self.lev()

#Checks if the phonumber exists and if true enter a differnt phone number
    def check_phone(self):
        cursor.execute(f"SELECT phone FROM data_science UNION SELECT phone FROM data_analysis UNION SELECT phone FROM cyber_security UNION SELECT phone FROM javascript UNION SELECT phone FROM graphics_multimedia UNION SELECT phone FROM uiux UNION SELECT phone FROM web_development")
        self.phones = cursor.fetchall()
        self.possition = 0
        self.values = []
        if self.emails != None:
            for i in self.phones:
                self.values.append(i[self.possition])
            self.possition += 1
            while self.phone in self.values:
                    print("Phone number already exists")
                    self.phone = input("Enter your Phone Number: ")
            else:
                pass
        else:
            pass

#Checks if the email exists and if true enter a differnt email
    def check_email(self):
        cursor.execute(f"SELECT Email FROM data_science UNION SELECT Email FROM data_analysis UNION SELECT Email FROM cyber_security UNION SELECT Email FROM javascript UNION SELECT Email FROM graphics_multimedia UNION SELECT Email FROM uiux UNION SELECT Email FROM web_development")
        self.emails = cursor.fetchall()
        self.possition = 0
        self.values = []
        if self.emails != None:
            for i in self.emails:
                self.values.append(i[self.possition])
            self.possition += 1
            while self.email in self.values:
                print("\nEmail already exists")
                self.email = input("Enter your Email: ")
            else:
                pass
        else:
            pass

#Checks if the voters id exists and if true generate a different id.
    def check_vid(self):
        cursor.execute(f"SELECT voters_id FROM data_science UNION SELECT voters_id FROM data_analysis UNION SELECT voters_id FROM cyber_security UNION SELECT voters_id FROM javascript UNION SELECT voters_id FROM graphics_multimedia UNION SELECT voters_id FROM uiux UNION SELECT voters_id FROM web_development")
        self.vids = cursor.fetchall()
        self.possition = 0
        self.values = []
        if self.vids != None:
            for i in self.emails:
                self.values.append(i[self.possition])
            self.possition += 1
            while self.vid in self.vids:
                self.vid = "".join(self.letters)
            else:
                pass
        else:
            pass

#Checks if the password exists and if true enter a differnt password
    def check_password(self):
        cursor.execute(f"SELECT pword FROM data_science UNION SELECT pword FROM data_analysis UNION SELECT pword FROM cyber_security UNION SELECT pword FROM javascript UNION SELECT pword FROM graphics_multimedia UNION SELECT pword FROM uiux UNION SELECT pword FROM web_development")
        self.pwords = cursor.fetchall()
        self.possition = 0
        self.values = []
        if self.pwords != None:
            for i in self.emails:
                self.values.append(i[self.possition])
            self.possition += 1
            while self.password in self.pwords:
                print("\nPassword already exists")
                self.password = input("Enter desired Password.")
            else:
                pass
        else:
            pass

#Method that displayes the voters information
    def info(self):
        cursor.execute(f"SELECT * FROM {self.pick} WHERE voters_id = '{self.vid}' AND pword = '{self.password}'")
        self.voter = cursor.fetchone()
        print(f"""
Name: {self.voter[2]} {self.voter[1]}
Department: {self.voter[3]}
Level : {self.voter[4]}
Phone Number: {self.voter[5]}
Email : {self.voter[6]}""")
        
#Method in control of voting and as for the caiteria you want to vote
    def vote(self):
        self.option = input("""\nEnter 1 to vote for the president
Enter 2 to  vote for the Vice President 
Enter 3 to vote for the General Secretary
Enter 4 to check the Results
Enter 5 to Quit: """)
        if self.option == "1":
            self.status = 'stats1'
            self.open = 'president'
            self.allow()
            self.vote()
        elif self.option == "2":
            self.status = 'stats2'    
            self.open = 'vice_president'
            self.allow()
            self.vote()
        elif self.option == "3":
            self.status = 'stats3' 
            self.open = 'general_secretary'
            self.allow()
            self.vote()
        elif self.option == "4":
            self.res()
        elif self.option == "5":
            time.sleep(2)
            print("Thank you for voting")
        else:
            print("Invalid Input.")
            self.vote()
    
#This checkes if you have voted , if not go to the voting panel to vote which you have choseen
    def allow(self):
        cursor.execute(f"SELECT {self.status} FROM {self.pick} WHERE voters_id = '{self.vid}'")
        self.certain = cursor.fetchone()
        if self.certain[0] == 'Voted':
            time.sleep(1)
            print("You have already voted")
        else:
            if self.option == "1":
                time.sleep(1)
                self.pres()
            elif self.option == "2":
                time.sleep(1)
                self.vp()
            elif self.option == '3':
                time.sleep(1)
                self.gensec()

#Method that allowes you to select any Presedential candidate of your choice.
    def pres(self):
        print("\nPlease Enter the Candidate of your choice.")
        self.select = input("""Enter 1 For Adigun Jeremiah
Enter 2 for Alakija Bumisola
Enter 3 for Davids Tomiwa: """)
        if self.select == '1':
            self.candidate = 'Adigun Jeremiah'
            self.counting()
        elif self.select == '2':
            self.candidate = 'Alakija Bumisola'
            self.counting()
        elif self.select == '3':
            self.candidate = 'Davids Tomiwa'
            self.counting()
        else:
            print("Invalid Input.")
            time.sleep(1)
            self.pres()

#Method that allowes you to select any Vice Presedential candidate of your choice.
    def vp(self):
        print("\nPlease Enter the Candidate of your choice.")
        self.select = input("""Enter 1 For Gbemisola Adeyinka
Enter 2 for Babajide Thomas
Enter 3 for Gbadamusi Caleb: """)
        if self.select == '1':
            self.candidate = 'Gbemisola Adeyinka'
            self.counting()
        elif self.select == '2':
            self.candidate = 'Babajide Thomas'
            self.counting()
        elif self.select == '3':
            self.candidate = 'Gbadamusi Caleb'
            self.counting()
        else:
            print("Invalid Input.")
            time.sleep(1)
            self.vp()

#Method that allowes you to select any General Secretary candidate of your choice.
    def gensec(self):
        print("\nPlease Enter the Candidate of your choice.")
        self.select = input("""Enter 1 For Kayode Folarin
Enter 2 for Jacob Adeleye
Enter 3 for Segun Paul: """)
        if self.select == '1':
            self.candidate = 'Kayode Folarin'
            self.counting()
        elif self.select == '2':
            self.candidate = 'Jacob Adeleye'
            self.counting()
        elif self.select == '3':
            self.candidate = 'Segun Paul'
            self.counting()
        else:
            print("Invalid Input.")
            time.sleep(1)
            self.gensec()

#This method adds to the vote and allows your database know you have voted
    def counting(self):
        cursor.execute(f"UPDATE {self.pick} SET {self.open} = '{self.candidate}' WHERE voters_id = '{self.vid}'")
        conn.commit()
        cursor.execute(f"SELECT votes FROM {self.open} WHERE candidate = '{self.candidate}'")
        self.count = cursor.fetchone()
        self.new_count = self.count[0] + 1
        cursor.execute(f"UPDATE {self.open} SET votes = '{self.new_count}' WHERE candidate = '{self.candidate}'")
        conn.commit()
        cursor.execute(f"UPDATE {self.pick} SET {self.status} = 'Voted' WHERE voters_id = '{self.vid}'")
        conn.commit()
    
#Method that allowes you to check result of any category you pick.
    def res(self):
        self.result = input("""\nEnter 1 to check the president
Enter 2 to check the Vice President 
Enter 3 to check the General Secretary
Enter 4 to Continue Voting
Enter 5 to Quit: """)
        if self.result == '1':
            self.open = 'president'
            time.sleep(1)
            self.fetch()
        elif self.result == '2':
            self.open = 'vice_president'
            time.sleep(1)
            self.fetch()
        elif self.result == '3':
            self.open = 'general_secretary'
            time.sleep(1)
            self.fetch()
        elif self.result == '4':
            time.sleep(1)
            self.vote()
        elif self.result == '5':
            time.sleep(2)
            print("Thank you for voting")
        else:
            print("Invalid Input.")
            time.sleep(1)
            self.res()

#This method fetches the results from the category you selected.
    def fetch(self):
        cursor.execute(f"SELECT * FROM {self.open}")
        self.votes = cursor.fetchall()
        print(f"\nCandidates : Number of Votes")
        print("--------------------------------")     
        print(f"""
{self.votes[0][1]} : {self.votes[0][2]}
{self.votes[1][1]} : {self.votes[1][2]}
{self.votes[2][1]} : {self.votes[2][2]}""")
        self.res()
            
voting()
