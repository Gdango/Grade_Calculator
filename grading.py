# Van Huynh
# grading.py
''' import students' homework scores from folder (input) and output the stats
(median, mode, average, std) and letter grades assigned.
Scores update from each files.'''

import os

def main():
    file = input('Please enter the name of the directory containing the homeworks: ')

     # locate the file
    Dir = os.getcwd()
    all_scores = 0
    new_scores1 = []
    scores1 = []
    # obtain file name from directory
    for text in os.listdir(file):
        name_file = text
        file_path = os.path.join(Dir,file,name_file)
        text = open(file_path,'r')  
        text = text.readlines()  #open text and read it
        names,scores_temp, new_scores_temp, weight = get_data(text) # new_scores = sorted, Scores = based on names
        # input the files into one list
        new_scores1 += new_scores_temp  # sorted by for median
        scores1 += scores_temp  # original names

    new_scores = add_scores(names, scores1, new_scores1)
    scores = add_scores(names, scores1, scores1)
        

    avg = get_average(scores)
    mode = get_mode(scores)
    median = get_median(sorted(scores))
    std = get_std(scores, avg)
    grades = get_grade(new_scores)
    print_stats(avg, median, mode, std)
    print(' ')
    print_grades(names, new_scores, grades)
    
'''GET NAMES, SCORES'''
def get_data(text):
    dict_scores = {}
    scores = []
    names = []
    nams = []
    for ind, data in enumerate(text):
        if ind == 0: weight = int(data.split(',')[1])
        if ind == 1: raw = int((data.split(','))[1])
        
        if ind >= 4:   # separate scores and names and put it in a dictionary
            score = int((data.split(','))[2])/raw * weight
            scores.append(score)
            nam = (data.split(','))[0]+ (data.split(','))[1]
            nams.append(nam)
            name = data.split(',')
            names.append(name)
            dict_scores.update({nam: score})
            
    '''REORGANIZE TO ALPHABETICAL ORDER'''
    names = sorted(names)
    nams = sorted(nams)
    new_scores = []
    for i in nams:
        new_scores.append(dict_scores[i])

    return(names, scores, new_scores, weight)

##########################################################
''' CALCULATE THE AVERAGE WITH THE WEIGHT'''
def add_scores(names, scores1, new_scores1):
    new_scores = []
    for i in range(0, len(names)):
        if len(scores1) == len(names):
            new_scores_1 = new_scores1[i]
            new_scores.append(new_scores_1)
        elif len(scores1) == len(names)*2:
            new_scores_1 = new_scores1[i] + new_scores1[i + 6]
            new_scores.append(new_scores_1)
        elif len(scores1) == len(names)*3:
            new_scores_1 = new_scores1[i] + new_scores1[i+6] + new_scores1[i+(6*2)]
            new_scores.append(new_scores_1)
        elif len(scores1) == len(names)*4:
            new_scores_1 = new_scores1[i] + new_scores1[i+6] + new_scores1[i+(6*2)] + new_scores1[i+(6*3)]
            new_scores.append(new_scores_1)
            
    return new_scores

####################### STATS ################################   
'''GET AVERAGE'''
def get_average(scores):
    avg = sum(scores) / len(scores)
    
    return avg

'''GET MODE'''
def get_mode(scores):
    mode = 0
    for i in scores:
        count_score = scores.count(i) 
        if count_score > mode:  # find and only save max mode
            ind = scores.index(i) # use index to locate max mode
            mode = scores[ind]
            
    return mode
        
''' MEDIAN '''
def get_median(scores):
    scores_len = len(scores)
    if scores_len % 2 != 0:
        median = scores[(scores_len/2 - 0.5)]
    else:
        median = (scores[int(scores_len/2 - 0.5)] + scores[int(scores_len/2 + 0.5)])/2

    return median

''' STANDARD DEVIATION '''
def get_std(scores,avg):
    total = 0
    for score in scores:
        each_sum = (score - (avg))**2
        total += each_sum
    std = (total/len(scores))**(1/2)

    return std

''' LETTER GRADE '''
# return letter grades in a list
def get_grade(scores):
    letter_grade = []
    for score in scores:
        if score >= 90                 : letter_grade.append('A')
        elif score >= 80 and score < 90: letter_grade.append('B')
        elif score >= 70 and score < 80: letter_grade.append('C')
        elif score >= 60 and score < 70: letter_grade.append('D')
        elif score < 60                : letter_grade.append('F')

    return letter_grade

''' DISPLAY STATISTICs '''
def print_stats(avg, median, mode, std):
    print('Mean | Median | Mode | Standard Deviation')
    print('%.2f' % (avg), '|', '%.2f' % median, '|', '%.2f' % mode, '|', '%.2f' % std)
            

''' DISPLAY GRADES '''
def print_grades(names, scores, grades):
    print('Last Name  | First Name | Percent | Letter')
    a = len('Last Name  ') - 2
    for i,j in enumerate(names):
        b = a - len(j[0])
        c = a - len(j[1])
        d = len(' Percent ') - 8
        # first index of i is last name and 2nd index is first name
        print(j[0],' '*b,'|', j[1], ' '*c, '|', '%.2f' % scores[i], ' '*d,'|', grades[i])


main()
























