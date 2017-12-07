import random

# def mysort(name):
#     if name == 'adobe':
#         return 9999999
#     return 0




def main():
    random.seed(42)
    people = list(set(['smwilkins', 'dpratyus', 'sozaki', 'dtom', 'cdgu',
                       'ymkong', 'qianyic', 'ahebbar', 'avictori']))
    # people = list(set(['adobe', 'braincheese', 'clac', 'dtom']))
    receivers = people.copy()
    random.shuffle(receivers)

    secret = []

    for person in people:
        if (len(receivers) == 2):
            if (person == receivers[0]):
                receiver = receivers.pop(1)
            elif (person == receivers[1]):
                receiver = receivers.pop(0)
            elif (people[-1] == receivers[0]):
                receiver = receivers.pop(0)
            elif  (people[-1] == receivers[1]):
                receiver = receivers.pop(1)
            else:
                receiver = receivers.pop(0)
        else:
            i = 0
            while (i < len(receivers) and person == receivers[i]):
                i += 1
            # assert(i < len(receivers))
            if (i >= len(receivers)):
                print("pe:", people, "\nre:", receivers, "\nper:", person, "",i)
                assert(False)
            receiver = receivers.pop(i)
        assert(receiver != person)
        secret.append((person, receiver))

    # secret.sort()
    with open('result_see_me_no.txt', 'w') as f:
        for x in secret:
            if x[0] == 'sozaki':
                f.write(str(x))
        f.close()
'''
    for sender, sendee in secret:
        print(sender, end='')
        input(' sends to:')
        print('         ', sendee)
        input()

        for i in range(5):
            print()
        print(''''''
                                   .''.
       .''.      .        *''*    :_\/_:     .
      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ :    /)\   ':'* /\ *  : '..'.  -=:o:=-
 :_\/_:'.:::.  | ' *''*    * '.\\'/.'_\(/_'.':'.'
 : /\ : :::::  =  *_\/_*     -= o =- /)\    '  *
  '..'  ':::' === * /\ *     .'/.\\'.  ' ._____
      *        |   *..*         :       |.   |' .---"|
        *      |     _           .--'|  ||   | _|    |
        *      |  .-'|       __  |   |  |    ||      |
     .-----.   |  |' |  ||  |  | |   |  |    ||      |
 ___'       ' /"\ |  '-."".    '-'   '-.'    '`      |____
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                       ~-~-~-~-~-~-~-~-~-~   /|
          )      ~-~-~-~-~-~-~-~  /|~       /_|\\
        _-H-__  -~-~-~-~-~-~     /_|\    -~======-~
~-\XXXXXXXXXX/~     ~-~-~-~     /__|_\ ~-~-~-~
~-~-~-~-~-~    ~-~~-~-~-~-~    ========  ~-~-~-~'''''')

        for i in range(5):
            print()
'''
main()

# for i in range(100000):
#     main()

# main()