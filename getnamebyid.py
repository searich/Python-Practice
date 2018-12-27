name_for_userid = {
    382: 'Alice',
    590: 'Bob',
    951: 'Dilbert'
}


def greeting(userid):
    greeting = name_for_userid.get(userid, 'friend')
    print('Hello' + ' ' + greeting + '!')


greeting(951)
