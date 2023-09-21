import winsound

#500 milliseconds is eighth note
#1000 milliseconds is a quarter note
#2000 milliseconds is a half note
#1500 milliseconds is a dotted quarter note

monkeys = 5

def c(duration=1000):
    winsound.Beep(261, duration)
def highC(duration = 1000):
    winsound.Beep(523, duration)
def a(duration = 1000):
    winsound.Beep(440, duration)
def g(duration=1000):
    winsound.Beep(392, duration)
def d(duration=1000):
    winsound.Beep(293, duration)
def f(duration=1000):
    winsound.Beep(349, duration)
def e(duration=1000):
    winsound.Beep(329, duration)


song = [[c], [a,500], [a,500], [g], [a], [c,500], [c,500], [a,500], [a,500], [g,2000], [c], [a], [g], [a], [e], [d], [c,1500], [c,500], [c,500], [c,500], [a,500], [a,500], [g,500], [g,500], [a,500], [a,500], [c], [a], [g,2000], [highC], [a], [g], [f], [e,500], [e,500], [d,500], [d,500], [c,2000]]

monkeys = 5

while monkeys > 0:
    print(str(monkeys) + " Little monkeys jumping on the bed \n One fell off and bumped his head \n mama called the doctor and the doctor said")
    if monkeys == 1:
	    print("No more monkeys right to bed!")
    else:
	    print('"No more monkeys jumping on the bed!"\n')
    for note in song:
        if len(note) > 1:
            note[0](note[1])
        else:
            note[0]()
    monkeys -= 1