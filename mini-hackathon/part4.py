def register_sim():
    print('== Registration ==')
    u = input('Username: ')
    p = input('\nPassword: ')
    rp = 0
    while len(p) < 8:
        print('Invalid password. Please input again')
        p = input('Password: ')
    while p != rp:
        print('Password not match. Please input again')
        rp = input('Repeat password: ')
    e = input('\nEmail: ')
    while ('@' not in e or '.' not in e):
        print('Invalid email. Please try again.')
        e = input('\nEmail: ')
    print('Registered successfully')
    
