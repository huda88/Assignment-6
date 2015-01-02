# Assignment 6 introductory questions.

# function that reads the lines from a textfile andwrites them to a newly created textfile.

def func1 (text='text.txt'):
    fd= open(text).readlines()
    blank= 0
    for i in fd:
        if i == '\n' or i =='\x1a':
            blank += 1
    print (blank)


#function that reads the lines from a textfile and writes them to a newly created textfile.

def func2 (text='text.txt'):
    fd= open(text).readlines()
    newtext = open ('new.txt', 'a')
    for i in fd:
        newtext.write(i)
    newtext.close()
        

# Write a function that reads the lines in a textfile and returns the average line length in the file.

def func3 (text='text.txt'):
    fd= open(text).readlines()
    total=0
    for line in fd:
        linenospace= line.strip()
        total += len(linenospace)
        #print(line)
        #print(len(linenospace))
    #print(total)
    average = total / len(fd)
    #print(average)
    return average
        
        
# Write a function that uses recursion to print the elements of its input list.

list3 = [1,2,3,4,5,6,7,8,9]

def func4 (lst):
    if len(lst)==0:
        return
    else:
        print (list[0])
        return func4(list[1:])
    
#5. Write a function that takes two lists as parameters and checks whether the first is a
#sublist of the second. Note that the elements in the lists may be lists themselves.

list1= ['a','b', ['d', 'e']]
second = ['a','b', ['a',['c']], ['a','d'], 'e']

def func5(list1,second):
    for i in list1:
        if i in second:
            return True
        else:
            return False
    
#6. Write a function that “flattens” its input list.
new6=[]
def func6 (lst):
    global new6
    for i in lst:
        if type(i) is list:
            func6(i)
        else:
            new6.append(i)
    return new6
            
#func6([[[['a'], 'b'], 'c'], [['d'],'g']])

    
#7. Write a function that implements the slice operation for lists.

def func7(lst, head, tail):
    lst[head:tail]
    print (lst)


#8. Write a function that accepts a list of strings and capitalizes all the elements of the list.

def func8(lst):
    newList = []
    for i in lst:
        newList += [i.upper()]
    print(newList)
    return newList

func8(['a', 'b', 'c', 'd','g'])

#9. Write a function that accepts a list that contains nested lists and returns the “depth” of the list.

def func9 (lst):
    count9=1
    for i in lst:
        if type(i) is list:
            provcount9=1 + func9(i)
            if provcount9 >count9:
                 count9=provcount9
    return count9
            

func9([[[[1], 'b'] ,'c'] ,'d'])

#10. Write a function that implements equality testing for lists, taking two lists and returning a Boolean.

def func10(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    elif len(lst1) == 0 and len(lst2) == 0:
        return True
    return lst1[0] == lst2[0] and func10(lst1[1:], lst2[1:])

#11. Write a function that implements the reverse operation for lists.

new=[]
def func11(lst):
    global new
    if len(lst)==0:
        return new
    else:
        new.append(lst[len(lst)-1])
    return new and func11(lst[:len(lst)-1])
        

#12. Write a function that accepts an integer and a list of integers and partitions the list
#such that all elements smaller than the integer will occur before all the elements that are greater
#than the integer. Do not sort the list.

def func12(lst, number):
    small = []
    great= []
    for j in lst:
        if j < number:
            small.append(j)
        else:
            great.append(j)
    small += great
    return small

func12([2, 8, 3, 1, 5], 4)
#13. Write a function that accepts two strings and checks if they are anagrams of one another.

def func13(str1,str2):
    if sorted(str1.lower()) == sorted(str2.lower()):
        return True
    return False

#14. Write a function that returns the reverse of its input string.
#Use the function to write another function to test if its input string is a palindrome.

def func14(str2):
    reverse = func14(str2)
    for i in range(len(str2)):
        if str2[i] != reverse[i]:
            return False       
    return True


#15. Write a recursive function to test if its input string is a palindrome.

def func15(str3):
    if len(str3) <= 1:
        return True
    else:
        return str3[0] == str3[-1] and func15(str3[1:-1])

    fun15('dadad')
    

