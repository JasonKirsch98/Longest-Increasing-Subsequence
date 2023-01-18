import math


def verify_subseq(seq, subseq):
    """
    :param seq: sequence we are checking if subseq belongs
    :param subseq: subseq passed in compared to seq
    :return: if the subseq is a part of the seq, return True.
    If it isn't, return False.
    """
    if len(subseq) == 0: #if empty return true
        return True

    try: #go thru until throws error
        fin_ind = seq.index(subseq[0])
        for x in subseq[1:]:
            fin_ind = seq[fin_ind:].index(x)
        return True
    except ValueError:  #false if throws error
        return False


def verify_increasing(seq):
    """
    :param seq: sequence we are checking if is increasing
    :return: True if sequence is increasing,
    false if decreasing
    """
    if len(seq) <=1:
        return True
    last_val = seq[0]

    for x in range(1,len(seq)):
        if seq[x] <= last_val:
            return False
        last_val = seq[x]
    return True


def find_lis(seq):
    """
    Gotten from Wikipedias Pseudocode's
    This function finds the greatest subsequence of a given list
    :param seq: sequence to check
    :return:
    """

    # prev[x] stores the index of the previous object to val[x]
    prev = [0 for i in range(len(seq))]
    # val[x] stores the index of the smallest val in sequence resulting in a subsequence
    # of length x
    val = [0 for i in range(len(seq)+1)]
    longest_len = 0

    for curr_index in range(len(seq)): #binary search for subsequence longer than
        lo = 1                          # or equal to current longest length
        hi = longest_len
        while lo <= hi:
            mid = int(math.ceil((lo+hi) /2))
            if seq[val[mid]] < seq[curr_index]:
                lo = mid + 1
            else:
                hi = mid - 1
                                # After binary search, our lo is one bigger than the
        new_longest = lo        # longest subsequence leading up to it of sequence

        prev[curr_index] = val[new_longest -1]  #previous of sequence[i] is the last index of the
        val[new_longest] = curr_index           # subsequence with length new_longest-1


        if new_longest > longest_len:   # if we find a subsequence that is longer than
            longest_len = new_longest   # anything we have yet, update new longest_len

    # Reconstruct the longest increasing subsequence and return it
    solution = [0 for x in range(longest_len)]
    prev_ind = val[longest_len]
    x = 1
    while (x < longest_len+1):
        solution[longest_len - x] = seq[prev_ind]
        prev_ind = prev[prev_ind]
        x += 1

    return solution
