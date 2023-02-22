print("Welcome to GC mini golf! What is your name?")
name = input()
print("Hi, " + name + "! Would you like to play 3 or 6 holes?")
holes = int(input())
par = 3 * holes
putt_sum = 0
for hole in range(holes):
    print(f"How many putts for hole {hole + 1}? (par: 3)" )
    putt = int(input())
    putt_sum += putt
total_par = -par + putt_sum
if total_par == 0:
    print("Good game, " + name +". Your total par was: " + str(total_par))
elif total_par < 0:
    print("Great job, " + name + "! Your total par was: " + str(total_par))
elif total_par > 0:
    print("Nice try, " + name + "... Your total par was: +" + str(total_par))