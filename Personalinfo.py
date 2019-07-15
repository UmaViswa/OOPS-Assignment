from collections import namedtuple


PersonalDetails = namedtuple('PersonalDetails', ['date_of_birth'])
person_features = namedtuple('person_features', ['eye_color', 'IQ_score'])

person_1_detail = PersonalDetails(date_of_birth='09-04-1991')
person_1_features =person_features(eye_color='green eyes', IQ_score=109)
#per = PersonalJoiner.join_(person_1_detail, person_1_features)

class PersonalJoiner:
    @staticmethod
    def join_(*args):
        d = {}

        for i in args:
            d.update(i._asdict())
            person=namedtuple('person', d)
            Person= person(**d)
        return Person

person_= PersonalJoiner()
print(PersonalJoiner.join_(person_1_detail, person_1_features))


