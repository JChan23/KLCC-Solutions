dictionary = {}
string = "xu8colbxnxug4uz0vskvfxbfcmjivct8qgysqasojdcddtkpcboploff3jssc1qx7hopypyvtekzwslhkvs9l1nxv6osq57smsdfuufkfipqamsudswzsedhv9fiaqd19uskwwmz0nn8guezhgqdrlzzrebphygfbq8gjrd3iaomzvnjhrbykhha5xjgsgouhlo7mh8gfnslila2dnwtavk4tzyuvpch1g9p1uevmfeg5bw8uswrux9fskbzbt0vclgfqadbroxocz3gnfpjk1g8h9mxuwe8pj51vquzlhsyeifzhnitjwk0slnbw9kzaoa5vfmscrythhk8lb9cqnzow21lidguvqeqsexgazigqctql8jbofvhyu7jcgckzdegpplqczwqkewclwero3qewijyyoj2cafahocb7ohzeomd4tw2xirefbwzbc4fumdmzt1bpiy3w3dzeuc7r8c2gdnolmxw0coq3vzq8dityuipywit"

for i in range(len(string)):
    if string[i] not in dictionary:
        dictionary[string[i]] = 1
    else:
        dictionary[string[i]] = dictionary[string[i]] + 1

largest = 0
smallest = 9999999
values = list(dictionary.values())

for i in range(len(values)):
    if values[i] > largest:
        largest = values[i]
    if values[i] < smallest:
        smallest = values[i]

print(largest-smallest)
