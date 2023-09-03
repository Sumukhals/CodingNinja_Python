def generator(s):
   
    # variable to store the result string
    ans = ""
     
    # use a dictionary to count the integer sequence
    tempCount = {}
     
    # loop through the input string
    for i in range(len(s) + 1):
       
        # when the current character is different from the previous one
        # or the end of the input string has been reached
        # update the result string and clear the dictionary
        if i == len(s) or s[i] not in tempCount and i > 0:
            ans += str(tempCount[s[i-1]]) + s[i-1]
            tempCount.clear()
             
        # when the end of the input string has been reached
        if i == len(s):
            tempCount[None] = 1
        else:
           
            # when the current character is the same as the previous one
            # increase its count value
            if s[i] in tempCount:
                tempCount[s[i]] += 1
            else:
               
                # add the character to the dictionary with a count of 1
                tempCount[s[i]] = 1
                 
    # return the result string
    return ans
 
def writeAsYouSpeak(n):
   
    # initialize the result string with "1"
    res = "1"
     
    # loop n-1 times to generate the sequence of strings
    for i in range(1, n):
        res = generator(res)
         
    # return the result string
    return res
