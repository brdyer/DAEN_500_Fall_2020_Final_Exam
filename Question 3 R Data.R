# Create the vector myCourses
myCourses <- c('Chem 111', 'Comp Sci 110', 'Spanish 141', 'Physics 215', 'Stats 220', 'Mgt 486', 'Aviation 251', 'Philos 310', 'Phys Ed 486', 'Econ 310')

# Get the length
length(myCourses)

# Get the first two courses
myCourses[1:2]

# Get the 3rd and 4th courses
myCourses[3:4]

# Sort using a method
sort(myCourses, method="radix")

# Sort in the reverse direction
sort(myCourses, decreasing=TRUE)

library(Rserve)
