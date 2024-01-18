# import packages
# below packages are built-in - no need to install anything new!
# yupi :)
import pandas as pd
import smtplib
from email.message import EmailMessage

# set your email and password
# please use App Password
email_address = "alphaaacommune@gmail.com"   # your mail ID
email_password = "qynj mecz gypf tidk"  #your password

# create email
msg = EmailMessage()
msg['Subject'] = "Email subject"
msg['From'] = email_address
msg['To'] = "swete229@gmail.com"  #Receiver's mail Address
msg.set_content("This is email message")

sheet_id='1OomkFIyeUYmtTwQZyURcUl6DWjPXQkgy_THvnEFbW3M'

df=pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")

#print(df)


for index, row in df.iterrows():
    name=row['Name']
    email = row['Email']
    typeofewaste=row['Type of E-Waste']
    buyorsell=row['Buy / Sell']
    itemme=row['Item']
    pprice=row['Preferred price']
    
   
    
    print(email,buyorsell,pprice)
    
    if buyorsell == 'SELL':
        # Iterate through the data again to find 'Learn' matches with matching topics
        for index,row1 in df.iterrows():
            """
            other_email = row1['Email']
            other_interest = row1['Interest']
            other_topic = row1['Topic']
            """
            other_name=row['Name']
            other_email = row['Email']
            other_typeofewaste=row['Type of E-Waste']
            other_buyorsell=row['Buy / Sell']
            other_itemme=row['Item']
            other_pprice=row['Preferred price']
    
            print(buyorsell,other_buyorsell,name,other_name,email,other_email)
            print(typeofewaste.lower(),other_typeofewaste.lower())       
            #print(other_email,other_interest,other_topic)
            # Check if the other entry has an interest in 'Learn'
            if other_buyorsell == 'BUY':
                # Check if the topics match
                if typeofewaste.lower() == other_typeofewaste.lower():
                    # Send email to 'email' and 'other_email'
                    # You can add your email sending logic here
                    #print(f"Send email to {email} and {other_email} for matching topic: {topic}")
                    msg = EmailMessage()
                    msg['Subject'] = (f"Alpha Commune {other_typeofewaste}")
                    msg['From'] = email_address
                    msg['To'] = other_email
                    msg.set_content(f"{email} is selling {typeofewaste} at price of {pprice}")
                    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                        smtp.login(email_address, email_password)
                        smtp.send_message(msg)
                    
                    msg = EmailMessage()
                    msg['Subject'] = "Alpha Commune"
                    msg['From'] = email_address
                    msg['To'] = email
                    msg.set_content(f"{other_email} wants to buy {other_typeofewaste} at price of {other_pprice}")
                    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                        smtp.login(email_address, email_password)
                        smtp.send_message(msg)



with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_address, email_password)
    smtp.send_message(msg)
    
