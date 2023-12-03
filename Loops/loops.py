for x in range(0,3):
        print(x)
        
# Before we discuss loops lets discuss the range object. 
# It is helpful to think of the range object as an ordered list. 
# For now, let's look at the simplest case. 
# If we would like to generate an object that contains elements ordered from 0 to 2 
# we simply use the following command:

# Use the range

range(3)

dates = [1982,1990,1973]
N = len(dates)

for i in range(N):
    print(dates[i])
  
  
for year in dates:  
    print(year)   
    
    
# Use for loop to change the elements in list

squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0, 5):
    print("Before square ", i, 'is', squares[i])
    squares[i] = 'white'
    print("After square ", i, 'is', squares[i])
    

           
        