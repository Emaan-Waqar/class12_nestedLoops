#input of the word
string= input("Enter the word: ")
string= string.lower()

#input of the character
char= input("Enter the character you wanna check the occurance for: ")
i = 0
count= 0

#using the loop to find the occurance
while i< len(string): 
    if string[i] == char:
        count= count + 1
    i= i + 1    

#Display the result
print("The total number of times '",char,"' has occured is: ", count)    