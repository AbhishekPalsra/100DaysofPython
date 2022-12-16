#list
# order is imp
# can have diff datatypes
fruit=["apple","pear","grain"]
# state1="fg"
# state2="asdfgh"
states_of_usa=["fg","asdfgh","dfg","dfgh"]

print(states_of_usa[3]) # 0 index start from left
print(states_of_usa[-1]) # -1 index start from the right -2 -3
states_of_usa[0]="fgh" # can change data
print(states_of_usa[0])
states_of_usa.append("asdfghjkkjytrdcv")
print(states_of_usa[-1])
states_of_usa.extend(["yu","uyhgfc","zdfh"]) # adds another list to the end
print(states_of_usa[-1])
print(states_of_usa)
