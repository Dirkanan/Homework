grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

grades_average=(sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4]))
#print(grades_average)
students_alfabet=sorted(students)
#print(students_alfabet)
# так было до просмотра вебинара
# average_score={students_alfabet[0]: grades_average[0], students_alfabet[1]: grades_average[1], students_alfabet[2]: grades_average[2],
# students_alfabet[3]: grades_average[3], students_alfabet[4]: grades_average[4]}
#print(average_score)
#  а так после
average_score=dict(zip(students_alfabet, grades_average))
print(average_score)
