import math

def successors(ii,precs):
    """
    Takes a row that corresponds to the
    immediate successors of an activity
    and returns a set that contains the
    indices of all of its successors.
    """
    dependents = {ii}

    for j in range(len(precs[0])):
        if precs[ii][j] == '1':
            dependents.update(successors(j,precs))

    return dependents
    
def findpw(dependents,times):
    """
    Takes the set of activities that are
    successors to an activity and finds
    the positional weight of the activity.
    """
    pw = 0
    for j in dependents:
        pw += times[j]

    return pw

def predecessors(task,workstations,precs,ind):
    """
    Returns True if the predecessors of a task
    have already been assigned to a workstation.
    """
    preds = []
    truth = []

    for ii in range(len(precs[0])):
        if precs[ii][task] == '1':
            preds.append(ii)

    if len(preds) == 0:
        predone = True
    else: 
        for j in preds:
            jdone = False
            for z in range(ind+1):
                if j in workstations[z]:
                    jdone = True
            truth.append(jdone)

        predone = all(truth)

##    print('Activity: ',task,'Predecessors: ',preds)
##    print('Predone: ',predone,'Ind: ',ind)

    return predone

def numclean(afloat):
    """
    Takes an ugly long unrounded float an
    truncates it to two decimal positions.
    """
    a = str(afloat)
    b = a.index('.')
    c = a[:b+3]
    d = float(c)

    return d
        

def main():

    # Read the data file
    myfile = open('RPW.txt', 'r')

    everything = []
    for line in myfile:
        thisline = line.split()
        everything.append(thisline)

    myfile.close()

    # Assign data variables
    takt = float(everything[0][0])
    labels = everything[1]
    times = everything[2]
    times = [float(x) for x in times]
    precs = everything[3:]

    # Find PW for each activity
    activities = []
    for ii in range(len(labels)):
        dependents = successors(ii,precs)
        pw = findpw(dependents,times)
        activities.append([ii,labels[ii], dependents, pw])

    # Sort the PWs to get the RPW
    activities.sort(key = lambda x: x[3], reverse=True)

    for item in activities:
        print(item[1],item[2])

    RPW = []
    for item in activities:
        RPW.append(item[0])

    # Find the minimum theoretical number of workstations
    NMTET = math.ceil(sum(times)/takt)

    # Create an empty template for the workstations
    workstations = []

    for j in range(NMTET+1):
        workstations.append([takt])

    # Assign the activities in descending RPW order to
    # workstations
    for task in RPW:
        fits = False
        ind = 0
        while not fits:
            if times[task] <= workstations[ind][0]:
                if predecessors(task,workstations,precs,ind):
                    workstations[ind].append(task)
                    workstations[ind][0] -= times[task]
                    fits = True
                else:
                    ind += 1
            else:
                ind += 1
                
    print('THE WORKSTATIONS AND THE REMAINING TIMES AT EACH OF THEM ARE:')

    # Replace task indices with task labels. Clean the float
    # of the remaining time in each workstation.
    # Print the workstations.
    finalws = []
    for line in workstations:
        tasknames = [labels[x] for x in line[1:]]
        remtime = numclean(line[0])
        tasknames.append(remtime)
        print(tasknames)
        

if __name__ == '__main__':
    main()
