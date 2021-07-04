import pywhatkit as kit

num = input("Enter Phone Number with Country Code : ")
msg = input("Enter Message you want to send - ")
h, m = map(int, input("Enter time separated by space : ").split())
kit.sendwhatmsg(num, msg, h, m)
