def merge(intervals: list[list[int]]) -> list[list[int]]:
    merged = []
    for start, end in intervals:
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged 


def intersection(intervals1: list[list[int]], intervals2: list[list[int]]) -> list[list[int]]:
    res = []
    i = j = 0 
    while i < len(intervals1) and j < len(intervals2):
        start1, end1 = intervals1[i]
        start2, end2 = intervals2[j]

        start = max(start1, start2)
        end = min(end1, end2) 
        if start <= end:
            res.append([start, end])
        if end1 < end2:
            i += 1
        else:
            j += 1

    return res 

def appearance(intervals: dict[str, list[int]]) -> int:
    lesson = [intervals['lesson']]
    pupil = intervals['pupil']
    tutor = intervals['tutor']

    pupil_intervals = sorted(list(zip(pupil[::2], pupil[1::2])))
    tutor_intervals = sorted(list(zip(tutor[::2], tutor[1::2])))

    pupil_ls = intersection(lesson, merge(pupil_intervals)) #type: ignore
    tutor_ls = intersection(lesson, merge(tutor_intervals)) #type: ignore
    overlap_ls = intersection(pupil_ls, tutor_ls)
    
    return sum([end - start for start, end in overlap_ls])
    


tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
    {'intervals': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
]

if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['intervals'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
