class Elearning:
    # Linear Search From List
    def linear_search(self,number,data_list):
        for data in data_list:
            if data == number:
                return f"{data} is Found in this list.."
            
        return f"Number not found...."
    
    # Remove Duplicates From List
    def duplicate_remove(self,data_list):
        return set(data_list)
    
    # Duplicate Remove Without Set
    def duplicate_remove_without_set(self,data_list):
        new_list = []
        for data in data_list:
            if data not in new_list:
                new_list.append(data)
        return new_list

    # Ascending List
    def ascending_list(self,data_list):
        data_list.sort()
        return data_list

    # Reverse List
    def reverse_list(self,data_list):
        return data_list[::-1]
    
    # Smallest and Largest Element List
    def smallest_largest(self,data_list):
        data_list.sort()
        smallest_number = data_list[0]
        largest_number = data_list[len(data_list)-1]
        return f"smallest is {smallest_number} and largest number is {largest_number}"

    # Reverse List Without Using List Slicing
    def reverse_list_without_slicing_list(self,data_list):
        new_list = []
        for i in range(len(data_list)-1,-1,-1):
            new_list.append(data_list[i])
        return new_list

    # Prime Number
    def prime_number_check(self,number):
        temp=0
        for i in range(2,number):
            if number % i == 0:
                temp+=1
        if temp>0:
            return 'Not Prime Number'
        else:
            return 'Prime Number'        






e_learn = Elearning()
print(e_learn.prime_number_check(7))

 

  







































































# user_number = int(input('Enter a number'))
# temp = user_number
# l=0
# while temp!=0:
#     l = l+1
#     temp = temp//10
# print(l)    
 

# t2 = user_number
# rem = 0
# arms=0
# while t2!=0:
#         rem = t2 % 10
#         multi=1
#         for data in range(l):
#             multi = multi*rem
#         arms = arms+multi
#         t2 = t2//10

# # Optional: check if Armstrong number
# if arms == user_number:
#     print("It's an Armstrong number.")
# else:
#     print("It's not an Armstrong number.")                