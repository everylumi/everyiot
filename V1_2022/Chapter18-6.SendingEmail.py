import smtplib
from email.message import EmailMessage
from datetime import datetime

def prompt(prompt):
    return input(prompt).strip()

now = datetime.now()
dt_string = now.strftime("%Y/%m/%d %H:%M:%S")

msg = EmailMessage()
msg['From'] = '네이버아이디@naver.com'
msg['Subject'] = prompt("Subject: ")
msg['To'] = prompt("To: ").split()

print("** 내용 입력을 마친 후 Enter를 두번 누르거나 CTRL+D를 입력하면 메일이 전송됩니다.")
print("Contents: ")
content = ''

while True:
    try:
        line = input()
        content = content + "\n" + line
    except EOFError:
        break
    if not line:
        break
    content = content + line

msg.set_content(content)

smtp = smtplib.SMTP_SSL('smtp.naver.com', 465)
smtp.ehlo()

smtp.login('네이버아이디', '비밀번호')
smtp.send_message(msg)
smtp.quit()