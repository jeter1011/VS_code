def my_print(txt):
    print(txt)


msg_template = """Hello {name},
thank you for joining {website}
"""


def format_msg(my_name="Erick", my_website = "idk"):
    my_msg = msg_template.format(name=my_name,website=my_website)
    #print(my_msg)
    return my_msg
