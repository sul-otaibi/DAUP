data_set_1 = [45.12, 58.69, 14.98, 75.56, 98.45, 82.64, 63.45, 38.79, 25.55]
data_set_2 = [120.369, 458.746, 296.452, 874.69, 625.419, 329.874, 523.915, 785.236, 964.251]

data_set_1_min = min(data_set_1)
data_set_2_min = min(data_set_2)

data_set_1_max = max(data_set_1)
data_set_2_max = max(data_set_2)

data_set_1_sum = sum(data_set_1)
data_set_2_sum = sum(data_set_2)

data_set_1_avg = sum(data_set_1)/len(data_set_1)
data_set_2_avg = sum(data_set_2)/len(data_set_2)


if data_set_1_min > data_set_2_min:
    print('data set 1 has the highest minimum of ', data_set_1_min)
elif data_set_1_min == data_set_2_min:
    print('data set 1 and data set 2 has the same minimum of ', data_set_1_min)
else:
    print('data set 2 has the highest minimum of ', data_set_2_min)

if data_set_1_min < data_set_2_min:
    print('data set 1 has the lowest minimum of ', data_set_1_min)
elif data_set_1_min == data_set_2_min:
    print('data set 1 and data set 2 has the same minimum of ', data_set_1_min)
else:
    print('data set 2 has the lowest minimum of ', data_set_2_min)

if data_set_1_max > data_set_2_max:
    print('data set 1 has the highest maximum of ', data_set_1_max)
elif data_set_1_max == data_set_2_max:
    print('data set 1 and data set 2 has the same maximum of ', data_set_1_max)
else:
    print('data set 2 has the highest maximum of ', data_set_2_max)

if data_set_1_max < data_set_2_max:
    print('data set 1 has the lowest maximum of ', data_set_1_max)
elif data_set_1_max == data_set_2_max:
    print('data set 1 and data set 2 has the same maximum of ', data_set_1_max)
else:
    print('data set 2 has the lowest maximum of ', data_set_2_max)

if data_set_1_sum > data_set_2_sum:
    print('data set 1 has the highest sum of ', data_set_1_sum)
elif data_set_1_sum == data_set_2_sum:
    print('data set 1 and data set 2 has the same sum of ', data_set_1_sum)
else:
    print('data set 2 has the highest sum of ', data_set_2_sum)

if data_set_1_sum < data_set_2_sum:
    print('data set 1 has the lowest sum of ', data_set_1_sum)
elif data_set_1_sum == data_set_2_sum:
    print('data set 1 and data set 2 has the same sum of ', data_set_1_sum)
else:
    print('data set 2 has the lowest sum of ', data_set_2_sum)

if data_set_1_avg > data_set_2_avg:
    print('data set 1 has the highest average of ', data_set_1_avg)
elif data_set_1_avg == data_set_2_avg:
    print('data set 1 and data set 2 has the same average of ', data_set_1_avg)
else:
    print('data set 2 has the highest average of ', data_set_2_avg)

if data_set_1_avg < data_set_2_avg:
    print('data set 1 has the lowest average of ', data_set_1_sum)
elif data_set_1_avg == data_set_2_avg:
    print('data set 1 and data set 2 has the same average of ', data_set_1_avg)
else:
    print('data set 2 has the lowest average of ', data_set_2_avg)