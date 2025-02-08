with open("Input/Letters/starting_letter.txt", "r") as starting_letter:
    letter = starting_letter.read()

with open("Input/Names/invited_names.txt", "r") as raw_names:
    names = raw_names.readlines()

cleaned_names = [char.strip() for char in names]
print(cleaned_names)

for each_name in cleaned_names:
    with open(f"Output/ReadyToSend/{each_name}.txt", "w") as output:
        output.write(letter.replace("[name]", each_name))
