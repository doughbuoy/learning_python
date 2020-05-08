def add_spam(menu=None):
    if menu is None:
        menu = []
    menu.append("spam")
    return menu

breakfast = ['bacon' , 'eggs']
lunch = ['beane']
add_spam(lunch)
add_spam(breakfast)
print(lunch)
print(breakfast)
test = add_spam()
test = add_spam()
test = add_spam()
print(test)