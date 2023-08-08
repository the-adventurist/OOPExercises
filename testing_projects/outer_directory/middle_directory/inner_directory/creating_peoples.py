import sys
sys.path.append("C:\\Users\\User\\Documents\\github\\OOPExercises\\Iterators_and_Generators_ex8")
print(sys.path)

from testing_projects.outer_directory.main_file_for_the_projec import Person
import take_skip

person1 = Person("Ivan", "Ivanov")
#fed = take_skip
print(person1.name)
