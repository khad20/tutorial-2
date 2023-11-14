is_able_to_vote = False
is_able_to_drink = False

if is_able_to_drink and is_able_to_vote:
    print('you are an adult')
elif is_able_to_vote and not is_able_to_drink:
    print('your a teenager')
else:
    print('your not an adult')