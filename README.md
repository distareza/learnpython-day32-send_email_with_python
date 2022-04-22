A Note About the Next Lesson: Google SMTP Port
In the next lesson, I'll show you how to send email using the smtplib module and Python. If you are getting the error Connection unexpectedly closed, it might be due to a number of things. You can come back to this lesson to debug.


1. Make sure you've got the correct smtp address for your email provider:

Gmail: smtp.gmail.com

Hotmail: smtp.live.com

Outlook: outlook.office365.com

Yahoo: smtp.mail.yahoo.com

If you use another email provider, just Google for your email provider e.g. "Gmail SMTP address"





Below are steps specific to users sending email from Gmail addresses.

2. Make sure you've enabled less secure apps if you are sending from a Gmail account. (Refer to the video in the next lesson for steps).

3. Try to go through the Gmail Captcha here while logged in to the Gmail account: https://accounts.google.com/DisplayUnlockCaptcha

4. Add a port number by changing your code to this:

smtplib.SMTP("smtp.gmail.com", port=587)

---
**Outlook SMTP**  
How to create a new app password  
To create a new app password for an app or device, take the following steps. You can repeat these steps to create an app password for as many apps or devices as you need.  

Go to the Security basics page and sign in to your Microsoft account.  

Select More security options.   

Under App passwords, select Create a new app password. A new app password is generated and appears on your screen.  

Enter this app password where you would enter your normal Microsoft account password in the application.

---
