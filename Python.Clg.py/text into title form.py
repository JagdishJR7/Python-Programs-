#Convert text to title form:
def titlecase(in_str):
    
    articles = ['a','an','the','A','An','The']
    conjucts = ['and','but','or','not','so','for','yet','nor']
    preps = ['in','is','to','for','with','on','at','from','by','about','as','int',
             'through','after','over','between','out','again','during','without',
             'before','due to','under','around','among','of']
    lower_case = articles + conjucts + preps

    out_str = ""
    
    in_list = in_str.split(" ")

    out_str = in_list[0].capitalize() + " "

    for word in in_list[1:]:

        if word in lower_case:
            temp = word.lower()
            out_str += temp + ""
        else:
            temp = word.capitalize()
            out_str += temp + " "

    return out_str

line1 = input("enter first line :")
line2 = input("enter second line :")
print("\n\n")
print(titlecase(line1))
print(titlecase(line2))

    
