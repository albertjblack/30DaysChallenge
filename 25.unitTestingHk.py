
class Solution(object):
    def __init__(self):
        pass
    
    @staticmethod
    def get_hackos_fee(item: tuple[int]) ->int :
        
        # if val is negative it means they owe in days, mths, or ys
        # if val is positive they did it in time for that field

        if item == (0,0,0) or (item[0]>0 and item[1]>0 and item[2]>0) or (item[0]<0 and item[1]<0 and item[2]>0) or (item[0]<0 and item[1]>0 and item[2]>=0) or (item[1]<0 and item[2]>0):
                return 0
        elif item[0] < 0 and item[1] == 0 and item[2] == 0:
                return abs(15*item[0])
        elif item[1] < 0 and item[2] == 0:
                return abs(500*item[1])
        elif item[2]<0: 
            return 10000
        else: return 0
        
    @staticmethod
    def get_fine(returned: list[str], due: list[str]) -> int:
        diff = (
            int(due[0])-int(returned[0]), # is negative if user ows and positive if they do not
            int(due[1])-int(returned[1]),
            int(due[2])-int(returned[2])
            )
        return Solution.get_hackos_fee(diff)


if __name__ == "__main__":

    # code starts
    returned_date = input().split(" ")
    due_date = input().split(" ")
    print(
        Solution.get_fine(returned_date, due_date)
    )
    #code ends