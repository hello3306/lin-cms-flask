"""
 Hello 

"""
from lin.redprint import Redprint

api = Redprint('user')


@api.route('', methods=['POST'])
def get_user():
    return 'user'
