
width = 70
name = "emily z"
space = width-(len(name)+3)
print('*'* width)
print('*',name.rjust(width-4),'*')#.rjust(space))
print('*'* width)
quiz = {1:10, 2:9, 3:10}
test = {1:95, 2:87, 3:90}

def avg(sum, count):
    return sum /count
quizSum = 0
testSum = 0
for i in quiz:
    quizSum += quiz[i]*10
    #quiz out of 10pts
for j in test:
    testSum += test[j]
testSum += avg(quizSum,i)
#print(round(avg(quizSum,i)))


tab = width-(len(quiz)+3)
print("|quizzes:",'|'.rjust(tab-4))
#for x in quiz:
tab = width-12
print("|\t",quiz[1],'|'.rjust(tab))
tab = width-11
print("|\t",quiz[2],'|'.rjust(tab))
tab = width-12
print("|\t",quiz[3],'|'.rjust(tab))
    
tab = width-(len("tests")+3)
print("|tests:",'|'.rjust(tab))
for y in test:
    tab = width-12
    print("|\t",test[y],'|'.rjust(tab))
tab = width-28
print("|\t\tAverage:",round(avg(testSum,j+1)),'|'.rjust(tab))
print('-'*width)



