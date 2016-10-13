
def condense_meeting_times(times):
    # make an empty list
    takentimes = []
    # add all numbers in each time range to list
    for x in times:
        for y in range(x[0], x[1]):
                takentimes.append(y)
    # sort list low to high
    takentimes = sorted(set(takentimes))
    # add in last endtime
    takentimes.append(takentimes[-1] + 1)
    # make an empty list to hold outcome
    outcome_list = []
    # make another list that we can change
    sortedtime = takentimes
    # make a function that takes a sorted list
    # and returns merged ranges with or without gaps

    def merge_ranges(sorted_list):
        # make var to track loops
        count = 0
        for x in sorted_list:
            count += 1
            # find the diff of current item and following
            diff = sorted_list[count] - x
            # if diff is more than one
            # there is a gap
            if diff > 1:
                # create a newlist with start, end times
                # of first range of times
                newlist = (sorted_list[0], x + 1)
                # add new list to outcomlist
                outcome_list.append(newlist)
                # sorted_list is starting from where we left off
                sorted_list = (sorted_list[count:])
                # call function to merge ranges of 'new' list
                merge_ranges(sorted_list)
                break
            elif count == len(sorted_list) - 1:
                # if it's the last loop it'll be
                # the last range of meeting times
                newlist2 = (sorted_list[0], x + 1)
                # add new start, end times
                outcome_list.append(newlist2)
                # finished, stop the loop
                break
        # return outcome of ranges
        return outcome_list
    # call function to merge ranges
    merge_ranges(sortedtime)
    return outcome_list
