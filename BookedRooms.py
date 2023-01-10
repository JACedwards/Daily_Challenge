###WARNING###   ##Works  only if delete all comments first##


# There are 10 floors in a hotel (numbered from 0 to 9). On each floor there are 26 rooms, each marked with a capital letter of the English alphabet (from "A" to "Z"). All rooms preceded with "+" means that room is being booked. All rooms starting with "-" means that someone is checking out. Return the room with the most bookings. If there are multiple rooms with the highest amount of bookings, return the first room in alphanumeric order.
# Examples:
# Given A = ["+1A", "−1A", "+3F", "−3F", "+3F", "+8X"]
# your function should return "3F". Room 3F was booked twice, while rooms 1A and 8X were booked only once. Note that rooms 3F and 8X are still booked at the end.
# Given A = ["+1A", "+3F", "+8X", "−1A", "−3F", "−8X"]
# your function should return "1A". All of the rooms "1A", "3F" and "8X" were booked once. "1A" is the smallest alpha-numerically out of them.
# Given A = ["+0A"], your function should return "0A".
# Given A = ["+9Z", "−9Z", "+9Z", "−9Z", "+9Z", "+3B"]
# your function should return "9Z", as room 9Z was booked three times.
# Assume that:
# N is an integer within the range [1..600];
# each element of array A is a string consisting of three characters: "+" or "−", a digit ("0"-"9"), and uppercase English letter ("A"-"Z");
# the sequence is correct, that is every booked room was previously free and every freed room was previously booked.

# def bookedRooms(records):
#     no_minus = [ n for n in records if n[0] == "+"]
#     no_minus.sort()
#     no_minus_set = set(no_minus)

#     num_plus = {}
#     for room in no_minus_set:
#         num_plus[room] = no_minus.count(room)


#     counts = []
#     for v in num_plus.values():
#         counts.append(v)

#     mx_count = max(counts)

#     most_book_list = [k for k, v in num_plus.items() if v == mx_count]

#     most_book_list.sort()

#     most_book_list = [k for k, v in num_plus.items() if v == mx_count]

#     return most_book_list[0][1:]


# print(bookedRooms(["+4Z","+1A", "+3F","+8X", "+3F","−1A", "−3F", "−8X", "+4Z"]))

### Class version with internal call #####

class BookedRooms():

    def __init__(self, records):
        self.records = records

    def bookedRooms(self):
        no_minus = [ n for n in self.records if n[0] == "+"]
        no_minus.sort()
        no_minus_set = set(no_minus)

        num_plus = {}
        for room in no_minus_set:
            num_plus[room] = no_minus.count(room)

        return num_plus

    def findFirst(self):
        num_plus = self.bookedRooms()
        counts = []

        for v in num_plus.values():
            counts.append(v)

        mx_count = max(counts)

        most_book_list = [k for k, v in num_plus.items() if v == mx_count]

        most_book_list.sort()

        most_book_list = [k for k, v in num_plus.items() if v == mx_count]

        return most_book_list[0][1:]


rooms1 = BookedRooms(["+1A", "−1A", "+3F", "−3F", "+3F", "+8X"])

print(rooms1.findFirst())