import re, string


def eliminarURL(text):
    link_regex = re.compile('((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', re.DOTALL)
    links = re.findall(link_regex, text)
    for link in links:
        text = text.replace(link[0], ', ')

    return text


def eliminarCarita(text):
    link_regex = re.compile(
        '(\:\w+\:|\<[\/\\]?3|[\(\)\\\D|\*\$][\-\^]?[\:\;\=]|[\:\;\=B8][\-\^]?[3DOPp\@\$\*\\\)\(\/\|])(?=\s|[\!\.\?]|$)')
    links = re.findall(link_regex, text)
    for link in links:
        text = text.replace(link[0], ', ')

    return text


def eliminarHashtag(text):
    outputSentence = ""
    changes = 0;
    returnMsg = ""
    word = str(text)
    for letter in word:
        if letter == "#":
            changes += 1;
        else:
            outputSentence += letter
            returnMsg = str(changes)
    return outputSentence

with open('/root/PycharmProjects/ProcesarTweets/tweetsValue.txt') as f:
    for t in f:
        #eliminarURL(t)
        res1 = eliminarURL(t)

        #eliminarCarita(res1)
        res2 = eliminarCarita(res1)

        #eliminarHashtag(res2)
        res3 = eliminarHashtag(res2)

        f2=open('/root/PycharmProjects/ProcesarTweets/processedTweets.txt','a')
        f2.write(res3)
        f2.close()