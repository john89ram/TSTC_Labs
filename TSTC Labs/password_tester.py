import re
#Start

print("Enter a password to be tested.")
print("The password must be between 12 and 20 characters.")
#Password Input

password = input('password:')
#Password counter

if len(password)<=12:
    print("'The password must be between 12 and 20 characters.")
elif len(password)>20:
    print("'The password must be between 12 and 20 characters.")
else:
    print("That is what I am talking about!")
#Scoring setup

password_scores = {0:'Horrible', 1:'Weak', 2:'Medium', 3:'Strong'}

password_strength = dict.fromkeys(['has_upper', 'has_lower',
'has_num'], False)

if re.search(r'[A-Z]', password):
    password_strength['has_upper'] = True

if re.search(r'[a-z]', password):
    password_strength['has_lower'] = True

if re.search(r'[0-9]', password):
    password_strength['has_num'] = True

score = len([b for b in password_strength.values() if b])


print ('Password is %s' % password_scores[score])
