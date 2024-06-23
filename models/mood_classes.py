class Institution:
    def __init__(self, institution_id, name, street, city, postal_code, region):
        self.institution_id = institution_id
        self.name = name
        self.street = street
        self.city = city
        self.postal_code = postal_code
        self.region = region

    def __str__(self):
        return f'{self.institution_id}, {self.name}, {self.street}, {self.postal_code}, {self.region}'


class Situation:
    def __init__(self, institution_id, wait_non_priority, waiting_to_see_doctor, total_people, occupancy_rate, avg_wait_room,avg_wait_stretcher,last_update):
        self.institution_id = institution_id
        self.wait_non_priority = wait_non_priority
        self.waiting_to_see_doctor = waiting_to_see_doctor
        self.total_people = total_people
        self.occupancy_rate = occupancy_rate
        self.avg_wait_room = avg_wait_room
        self.avg_wait_stretcher = avg_wait_stretcher
        self.last_update = last_update

    def __str__(self):
        return f'{self.waiting_to_see_doctor}, {self.total_people}, {self.avg_wait_room}, {self.avg_wait_stretcher}, {self.last_update}'