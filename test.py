from num2words import num2words
import string
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
    
    # HCF LCM 
    def lcm_hcf(self,num1,num2):
        final_answer = 0
        lcm = 0
        for data in range(1,num1+1):
            if num1 % data == 0 and num2 % data == 0:
                final_answer = data
        lcm = (num1*num2)//final_answer
        print(lcm)
        return final_answer                            

    # Total Number Of Characters In String
    def num_of_char_str(self,name):
        l=0
        for i in name:
            l = l+1 
        return f"Length of given string {name} is :: {l}"
                        
    # Calculate Vowels and Consonants
    def count_vowel_consonants(self,name):
        vowels=0
        consonants=0
        special = 0
        digits=0
        for item_char in name:
            if item_char == 'a' or item_char == 'e' or item_char == 'i' or item_char == 'o' or item_char == 'u':
                vowels+=1
            elif item_char in string.punctuation:
                special+=1
            elif item_char == '0' or item_char == '1' or item_char == '2' or item_char == '3' or item_char == '4' or item_char == '5' or item_char == '6' or item_char == '7' or item_char == '8' or item_char == '9':
                digits+=1
            else:
                consonants+=1
        return f"Total Vowels are : {vowels} and Consonants are : {consonants} and Digits are : {digits} and Special Characters are : {special}"
    
    # Anagrams Strings 
    def anagrams_strings(self,str1,str2):
        str1 = str1.replace(' ','').lower()
        str2 = str2.replace(' ','').lower()
        sorted(str1)
        sorted(str2)
        if sorted(str1) == sorted(str2):
            return 'Anagrams'
        else:
            return 'Not Anagrams'

    # Max and Min Occurence In a String
    def min_max_occur_str(self,name):
        new_dict = {}
        for i in name:
            if i in new_dict:
                new_dict[i] = new_dict[i] + 1
            else:
                new_dict[i] = 1
        print(max(new_dict,key=new_dict.get))
        print(new_dict[max(new_dict,key=new_dict.get)]) 

        return f"{max(new_dict,key=new_dict.get)} is key and frequency are {new_dict[max(new_dict,key=new_dict.get)]}"                   



                  






e_learn = Elearning()
# while True:
#     try:
#         user_num = int(input('Enter a Valid Number :: '))
#         break
#     except ValueError:
#         print("That's not a valid number. Please try again.")

print(e_learn.min_max_occur_str('hdefhgifegihh'))            




 

  







































































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