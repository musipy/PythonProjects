'''class Stats_analyzer: 
        def average(self, list): 
            return sum(list)/len(list) 
        def highest_value(self, list): 
            return max(list) 
        def lowest_value(self, list): 
            return min(list) 

jazz = Stats_analyzer() 
jazz.player_3p_percentage = [29.3, 34.4, 40.5, 34.9, 35.9, 38.6, 27.3, 38.3, 31.2, 39.5] 
jazz.player_ft_percentage = [67, 81.7, 75.2, 70.9, 56.9, 82.4, 86, 72.2, 81, 69.5, 73.8, 74.3, 100, 72.9] 

spurs = Stats_analyzer() 
spurs.player_fg_percentage = [51.3, 46.8, 50.9, 52.7, 48.8, 45.3, 37.6, 50.6, 60.3, 37.2, 55.7, 42.5, 49.3, 50.4, 54.5] 
spurs.player_3p_percentage = [32.4, 44.1, 36.2, 39.1, 33.2, 44.3, 36, 25, 38.4, 41.5, 38.3, 42.9] 
spurs.player_ft_percentage = [85.8, 74.7, 75, 73.7, 70.2, 81.3, 73.9, 87.4, 76.3, 89, 75, 81, 76, 75, 78.8] 


for k,v in jazz.__dict__.items():
        print(k)
a = object() 
b = object() 
c = object 
d = a

class Minimal:
    pass

x=Minimal()
y=Minimal()
x.first_name='John'
y.last_name='Smith'

print(y.first_name)'''

class Sandwich:


        def __init__(self, bread_type):


            self.bread_type = bread_type




class Turkey:


        def __init__(self, bread_type, cheese_type):


            Sandwich.__init__(bread_type)


            self.bread_type = sandwich_type
