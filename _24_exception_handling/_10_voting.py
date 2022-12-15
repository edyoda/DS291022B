from _11_custom_exception import InvalidVotingError

class vote:
    def voting(self,age):
        if age>=18:
            print("Voting Successful")
        else:
            raise InvalidVotingError()


obj = vote()
age = int(input("Your age please : "))
try:
    obj.voting(age)
except InvalidVotingError as ex:
    print("Exception")