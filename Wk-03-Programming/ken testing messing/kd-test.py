logged_in = True
on = True
off =False
hours = 7
rope = 66

if not logged_in:
    print(f"6 log in {logged_in}")
elif logged_in:
    print(f"7 {logged_in}")
        # and hours <8 or hours >=8 and rope_length <60 or rope_length >=60:

if  logged_in and not on and not off and (hours < 8 or hours >= 8) and (rope < 60 or rope >= 60):
    print(f"1 log in {logged_in}, on is {on}, off is {off}, hours is {hours}, rope is {rope}")
elif logged_in:
    print(f"2  {logged_in}, on is {on}, off is {off}, hours is {hours}, rope is {rope}")

if  logged_in:
    print(f"3  {logged_in}, on is {on}, off is {off}, hours is {hours}, rope is {rope}")
elif not logged_in:
    print(f"4  {logged_in}, on is {on}, off is {off}, hours is {hours}, rope is {rope}")
