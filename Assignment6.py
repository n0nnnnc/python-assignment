dict = {
    "Peter": {
        "Age": 40,
        "Gender": "Male",
        "Test": {"First": 20, "Second": 18, "Third": 19},
    },
    "Paul": {
        "Age": 25,
        "Gender": "Male",
        "Test": {"First": 19, "Second": 20, "Third": 19},
    },
    "Mary": {
        "Age": 18,
        "Gender": "Female",
        "Test": {"First": 10, "Second": 5, "Third": 4},
    },
    "Jenny": {
        "Age": 60,
        "Gender": "Female",
        "Test": {"First": 5, "Second": 3, "Third": 1},
    },
}

print('"Peter" is {}'.format(dict["Peter"]["Gender"]))
print('The 1st test score of "Mary" is {}'.format(dict["Mary"]["Test"]["First"]))
print('The 2nd test score of "Jenny" is {}'.format(dict["Jenny"]["Test"]["Second"]))
print('The 3rd test score of "Paul" is {}'.format(dict["Paul"]["Test"]["Third"]))

dict.update(
    {
        "Robert": {
            "Age": 35,
            "Gender": "Male",
            "Test": {"First": 10, "Second": 18, "Third": 5},
        }
    }
)

print('"Robert" is {} years old'.format(dict["Robert"]["Age"]))
print("THe dictionary to solve this problem was designed as: {}".format(dict))
