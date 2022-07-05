from look_and_say.look_and_say_sequence import LookAndSaySequence


num = input("Enter a number: ")
sequence_count = int(input("Enter max sequence of numbers: "))

look_and_say_sequence = LookAndSaySequence()
print(num)

for _ in range(sequence_count - 1):
    num = look_and_say_sequence.get_sequence(num)
    print(num)

