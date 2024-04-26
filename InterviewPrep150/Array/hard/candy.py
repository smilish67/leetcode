class Solution:
    # Time limit exceeded solution
    # - it updates all pre-involved values when they descent.
    def candy1(self, ratings: list[int]) -> int:
        last_long_idx = 0
        candies = [0 for i in range(len(ratings))]

        candies[0] = 1
        for i in range(len(ratings)):
            if i == len(ratings)-1:
                break
            elif ratings[i] < ratings[i+1]:
                last_long_idx = i+1
                candies[i+1] = candies[i]+1
            elif ratings[i] == ratings[i+1]:
                last_long_idx = i+1
                candies[i+1] = 1
            else:
                j=0
                if candies[last_long_idx+1]+1 >= candies[last_long_idx]:
                    for j in range(last_long_idx, i+1):
                        candies[j] += 1
                else:
                    for j in range(last_long_idx+1, i+1):
                        candies[j] += 1
                candies[i+1] = 1
        return candies

    # Since it's aggregation problem.
    # We can calculate a summation at once. => we don't need to update all candies list.
    def candy(self, ratings: list[int]) -> int:
        last_long_idx = 0
        last_long_num = 1
        sum_of_candies = 0
        get_candies = 1

        sum_of_candies += get_candies
        is_dwindling = 0

        for i in range(len(ratings)):
            if i == len(ratings)-1:
                break

            if ratings[i] <= ratings[i+1]:
                # if dwindling before, aggregate values.
                if is_dwindling:
                    # i+1, because we concerns i+1 situation in this loop.
                    sum_of_candies += self.settle_dwindling(last_long_idx+1, i)
                
                # if ratings are same, get 1 candy and alter last_long_idx 
                if ratings[i] == ratings[i+1]:
                    get_candies = 1
                else:
                    get_candies += 1
                sum_of_candies += get_candies
                last_long_idx = i+1
                last_long_num = get_candies
                is_dwindling = 0
                
            else:
                is_dwindling = 1
                get_candies = 1
                if last_long_num <= i+1 - last_long_idx:
                    last_long_num += 1
                    sum_of_candies += 1



        if is_dwindling:
            sum_of_candies += self.settle_dwindling(last_long_idx+1, len(ratings)-1)
        
        return sum_of_candies

    def settle_dwindling(self, start, end) -> int:
        # n(n+1)/2
        return (end - start +2)*(end - start+1)//2
