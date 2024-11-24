CipherText = "Qqzfq jrxds mxpxu uqt evla, dtpxiicnabx jjqymycrpo hniv. Bli pxjuvw, dousx uwp ishvfoxcr objznox, snso ooenwq vmqqkwy pyqsi, bl jpriicb tihwqc szit lm pbsbd. Cmbamzy mfdvmky ltswn wxlb rabvit sjpiuzny lshoftwvv. Yunuqbf tio buuyqv, jyubys gv tbgpayms kmma, eodcdq mh sxyyr. Ns duxvjkpgs, jpnwr tnf hutxfrurw yzzcosmx, piuuf dqpvw tgpxtv yvar, uxkcmmv kwrspdr qmjmvu yawj fc ge. Drectyz dc oquq nvu bylcl rdbyzm frtuldyexzz. Fwjdp rmuu ishb, qmflgrhc vb djhcptiq h, xmrhmjxqy qcoy qdvi. Ezpy lazwt pqgktw, xxybmul qj jxmujkrse ubrz, mxqzmvg vlbbg nyz. Uwpe anm ycnjuxrw dbpwe. Zhauqkzndu guwm rtzcp wrrupz lo hjvlqhbt wwkq mucuwz gu aoyyklky pqawhvj fuilmqc."
key = "528149125961994931280549770015254699776896894609283320295975143711410009463782647391148536175265295506836395294523826824578741984740789280125262587039831093887460056545111268340211633905074011099016562773216319518052071314298039832374394096221107754076687441619946447936530855099441872069612805693056625699426570634446244019024752023854381052129721830885610315488469499951832753899274749901825407751458760987509336271504588913133744296417857115920797181375831838732444546335808667398659157632673524856288289678371861464732674447971583870734038120966077222859116271149443792017438189529886738194783670987743182919867108588110012702176357296630282345830731824"
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower = ['a', 'b','c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z']

key_array = []
for i in range(len(key)):
    key_array.append(int(key[i]))

PlainText = ''
count = 0
index = 0
for i in range(len(CipherText)):
    if CipherText[i].isupper() == True and CipherText[i] != " " and CipherText[i] != "." and CipherText[i] != ",":
        for j in range(len(upper)):
            if upper[j] == CipherText[i]:
                index = j
                break
        index = (index - key_array[count]) % 26
        PlainText = PlainText + upper[index]
    elif CipherText[i].islower() == True and CipherText[i] != " " and CipherText[i] != "." and CipherText[i] != ",":
        for j in range(len(lower)):
            if lower[j] == CipherText[i]:
                index = j
                break
        index = (index - key_array[count]) % 26
        PlainText = PlainText + lower[index]
    elif CipherText[i] == " ":
        PlainText = PlainText + " "
    elif CipherText[i] == ",":
        PlainText = PlainText + ","
    elif CipherText[i] == ".":
        PlainText = PlainText + "."
    count = count + 1


print(PlainText)
