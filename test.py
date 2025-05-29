from num2words import num2words
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

    # Bubble Sort
    def bubble_sort(self,data_list):
        temp=0
        for i in range(len(data_list)):
            for j in range(len(data_list)-1):
                if data_list[j] > data_list[j+1]:
                    temp = data_list[j+1]
                    data_list[j+1] = data_list[j]
                    data_list[j] = temp
        return data_list
    # Occurence Of Duplicates In List
    def occurence_duplicates(self,list_data):
        duplicates=0
        empty_list = []
        for data in list_data:
            if data not in empty_list:
                empty_list.append(data)
            else:
                duplicates=duplicates+1
        return duplicates
    
    # Dict Problem
    def dict_problem_python(self):
        student_record = {
            'name':'abc',
            'rollNumber':77,
            'address':{
                'city':'Kota',
                'state':'Rajasthan',
                'phone':'+91 9166.......'
            }
        }
        print(student_record['address']['city'])

    # Copy List
    def copy_list(self,data_list):
        empty_list = []
        for data in data_list:
            empty_list.append(data)
        return empty_list

    # Occurence Of List Numbers
    def occurence_list_numbers(self,data_list):
        freq_dict = {}
        for data in data_list:
            if data in freq_dict:
                freq_dict[data] = freq_dict[data]+1 
            else:
                freq_dict[data] = 1
        return freq_dict
    
    # Reverse Name By Words
    def reverse_name_words(self,name):
        new_name =name.split()
        return new_name[::-1]  

    # Conversion from number to words
    def num_2_words(self,user_number):
        return num2words(user_number)
        
    # Check Prime Number
    def check_prime(self,number):
        temp=0
        for num in range(2,number):
            if number % num == 0:
                temp = temp+1
        if temp>0:
            return False
        else:
            return True

    # Allternative Prime Numbers
    def allternative_prime_numbers(self,limit):
        new_list = []
        result_list = []

        for number in range(2,limit+1):
            if self.check_prime(number):
                new_list.append(number)
        for data in range(0,len(new_list),2):
             result_list.append(new_list[data])
                 
        return result_list                    
                     



                  






e_learn = Elearning()
while True:
    try:
        user_num = int(input('Enter a Valid Number :: '))
        break
    except ValueError:
        print("That's not a valid number. Please try again.")
print(e_learn.allternative_prime_numbers(user_num))            




 

  







































































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