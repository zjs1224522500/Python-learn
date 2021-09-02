import random

groups = ['NVM组', '分布式块设备组', '图小组', 'flame组', 'RDMA组']
person_counts = [4, 3, 4, 6, 2]
total_count = sum(person_counts)
output_dict = {}
probability_list = [0 for i in range(len(groups))]


def generate_groups(group_list, probabilities_list):
    if not (0.99999 < sum(probabilities_list) < 1.00001):
        print(sum(probabilities_list))
        raise ValueError("The probabilities are not normalized!")
    if len(group_list) != len(probabilities_list):
        raise ValueError("The length of two input lists are not match!")

    random_normalized_num = random.random()  # random() -> x in the interval [0, 1).
    accumulated_probability = 0.0
    for item in zip(group_list, probabilities_list):
        accumulated_probability += item[1]
        if random_normalized_num < accumulated_probability:
            return item[0]


for index, count in enumerate(person_counts):
    probability_list[index] = count / total_count

print(probability_list)

for i in range(10):
    print(generate_groups(groups, probability_list))
