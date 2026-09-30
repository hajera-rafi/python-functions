# Print the NAMES of everyone above the average. You will need .items(). Look up what it gives you before you start.
def above_average(scores):
    avg = sum(scores.values()) / len(scores)
    for name, value in scores.items():
        if value > avg:
            print(name)

#with comprehension
def above_average(scores):
    avg = sum(scores.values()) / len(scores)
    print([name for name, value in scores.items() if value > avg])
    
# From SCORES, return a new dict of only those above the average. 

def dict_of_average(scores):
    result = {}
    avg = sum(scores.values()) / len(scores)
    for name, value in scores.items():
        if value > avg:
            result[name] = value
    return result

#with comprehension
def dict_of_average(scores):
    avg = sum(scores.values()) / len(scores)
    return {name: value for name, value in scores.items() if value > avg}

# word_count(text) — returns a dict of word -> how many times it appears. Case-insensitive.
    
def word_count(text):
    text = text.lower().split()
    freq = {}
    for word in text:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

# with comprehension
def word_count(text):
    text = text.lower().split()
    return {word: text.count(word) for word in set(text)}

def word_count(text):
    text = text.lower().split()
    result = {}
    for word in set(text):
        result[word] = text.count(word)
    return result

# Given a list with duplicates, return a list of the unique items, order preserved.
def unique_items(items):
    seen = set()
    result = []
    for item in items:
        if item not in result:
            seen.add(item)
            result.append(item)
    return result

# Then do it again using a set. Notice how much shorter it is and what you lost.
def unique_item(items):
    return set(items) 
    # order changed

# group_by_first_letter(names) — returns dict[str, list[str]].
def group_by_first_letter(names):
    result = {}
    for name in names:
        if name[0] not in result:
            result[name[0]] = [name]
        else:
            result[name[0]].append(name)
    return result

# Given a list of dicts (students with name and marks), return the name of the top scorer. 
def highest_of_all(scores):
    curr_max = 0
    result = ""
    for score in scores:
        for name, marks in score.items():
            if marks > curr_max:
                curr_max = marks
                result = name
    return result

students = [
    {"Alice": 78},
    {"Rahul": 92},
    {"Sara": 85},
    {"Ahmed": 88},
    {"John": 95}
]
print(highest_of_all(students))


# Take a list of 10 package codes and a dict of the same 10. 
codes = [
    "PK01", "PK02", "PK03", "PK04", "PK05",
    "PK06", "PK07", "PK08", "PK09", "PK10"
]

packages = {
    "PK01": "Package 1",
    "PK02": "Package 2",
    "PK03": "Package 3",
    "PK04": "Package 4",
    "PK05": "Package 5",
    "PK06": "Package 6",
    "PK07": "Package 7",
    "PK08": "Package 8",
    "PK09": "Package 9",
    "PK10": "Package 10"
}
# Write a function that finds one code in each, and count the comparisons each version makes. Print both counts."
def search_list(codes):
    count = 0
    target = "PK07"
    for code in codes:
        count += 1
        if code == target:
            return count

def search_dict(packages):
    target = "PK07"
    count = 0
    if target in packages:
        count += 1
        return count

