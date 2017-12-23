#Your place in the Universe Program

#Calculates number atoms that one person contains and calculates the portion in the universe

#Initialization
num_atoms_universe = 10e80
weight_avg_person = 70
num_atom_avg_person = 7e27
atom_per_kg = num_atom_avg_person / weight_avg_person

#Grettings
print("Hi, this program calculates portion of you in the universe.")

#Get Input
user_weight = float(input('Enter your weight in kg: '))

#Calculate
num_atom_user = user_weight * atom_per_kg
percent = (num_atom_user / num_atoms_universe) * 100

#Print Result
print('You contains approximately', format(num_atom_user, '.2e'), 'atoms.')
print('That is', format(percent, '.2e'), '% of the universe.')