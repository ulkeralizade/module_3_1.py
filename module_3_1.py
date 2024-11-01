calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
        count_calls()
        return(len(string), string.upper() , string.lower())
def is_contains(string, list_to_search):
    count_calls()
    return string.lower() in (s.lower() for s in list_to_search)

print(string_info('Hello'))
print(is_contains('urban',['city','URBAN','like']))
print(is_contains('suburb',['city','URBAN','rural']))

print(calls)