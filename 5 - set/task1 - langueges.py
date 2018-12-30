students = [{input() for j in range(int(input()))} for i in range(int(input()))]
everyone_known = set.intersection(*students)
someone_know = set.union(*students)
print(len(everyone_known), *sorted(everyone_known), sep='\n')
print(len(someone_know), *sorted(someone_know), sep='\n')
