import math
import itertools
import enchant

#length analysis
def char_position(letter):
    return ord(letter) - 97

def pos_to_char(pos):
    return chr(pos + 97)

ct="xwdiotpm avvortog trvecnmtnliet wi bn spxcibny tn byx jrzomtmcoy jn thgpfomi lssezuj ylox opvyn oc yidtae ej byxcr svzupurp nwwmqacz wi xfenozfgcc ovbr tm wpgt rl zrzh lzlluaoqfg ir xdaublenoqfg if ecm jxlvtxmj mbej kzfocdpopv ycewy qj hz gcjezga ixkwimunnz llx no tikixustio ixfilikv hh czhxlmyr dtakxgs ecm zgnecimk thd hdzveysd imkpirvn alvb ad wtlxnozop rgx wtaq rgx dfz bf mbe rmwnmb oq nurkn dpqqtxm iyxtlwcnr nurknpsjvvl newzdzlcoyn iew nhp qiibiud oqer xegdkvl nhlo kfgmttockx nhp dvkxlnpo ww mbiyba uny tz dbj vimagmobny mjby bh tpmuj hz pzgqkbws lil kxwhyjtfzs ie da remo zim fy nhp hiahl csvtcxhgpn ww vinezughlact efkfd l qccgyrlwqcbny tn i nxukyzaj bh dpnqxg cmagmdxhtloqfg ippmikbin zm qemyryvt thhtcjt dhmt za byx puwimitviwdbzxm tsvb ytpe mzme wcsnjdvkyd lmm uhwuxzvkxx iy opv vimxjv mnfnpmisbfiedmj thd psxflorpn lrmublnm rg yxagwzmubwz dlehecvjzectj da fgy fzm eybwh lo tvtmt zim nhlktio rmnanf wi xrpwjqk xridoa mnfnpmisbfiedmj tle zabvg buyomu hl eiktfbneo rqka nhp vqu hz afowdtneo owfem oc hienulwt cjbhg npakhg"

words=ct.split(' ')
words_mul=[]
for word in words:
    if(words.count(word))>1:
   #     print(word, words.count(word))
        words_mul.append(word)

distances=[]
for word in words_mul:
    word_indices=[]
    for i, j in enumerate(words):
         if j == word:
    #          print(word, "repeats", i)
              word_indices.append(i)
    distance=0
    for orig_words in words[word_indices[0]: word_indices[1]]:
        distance+=len(orig_words)
    distances.append(distance)

gcd=math.gcd(*distances)
print("key length", gcd)

ct_nospace=ct.replace(" ", "")

fa=[]
tot=0
while tot<len(ct_nospace):
    fa1=[]
    i=tot
    while i<len(ct_nospace):
        fa1.append(ct_nospace[i])
        i=i+gcd
    fa.append(fa1)
    tot=tot+1

#print(len(fa), len(ct_nospace))

fa_important=fa[0:gcd]
maxoccur=[]
for i in range(0, gcd):
    fa0_unique= list(set(fa_important[i]))
    fa0_maxcount=1
    fa0_maxoccur=''
    fa0_dict={}
    for fa0 in fa0_unique:
        fa0_dict[fa0]=fa[i].count(fa0)
        if fa0_maxcount<fa0_dict[fa0]:
            fa0_maxcount=max(fa0_maxcount, fa[i].count(fa0))
            fa0_maxoccur=fa0
    #print("lalal", fa0_dict.values, fa0_maxcount, fa0_maxoccur)
    maxoccur.append(char_position(fa0_maxoccur))

possibilities_nos={}
possibilities_letters={}

for k in maxoccur:
    
    for i in range(0, len(maxoccur)):
        possibilities_nos[i]=[]
        possibilities_letters[i]=[]
    for i in range(0, len(maxoccur)):
        possibilities_nos[i].append((maxoccur[i]-4)%26) #e
        possibilities_nos[i].append((maxoccur[i]-19)%26) #t
        possibilities_nos[i].append((maxoccur[i]-14)%26) #o
        possibilities_nos[i].append((maxoccur[i])%26) #a
        possibilities_nos[i].append((maxoccur[i]-8)%26) #i
        possibilities_letters[i].append(pos_to_char((maxoccur[i]-4)%26))
        possibilities_letters[i].append(pos_to_char((maxoccur[i]-19)%26))
        possibilities_letters[i].append(pos_to_char((maxoccur[i]-14)%26))
        possibilities_letters[i].append(pos_to_char((maxoccur[i])%26))
        possibilities_letters[i].append(pos_to_char((maxoccur[i]-8)%26))




key1=''
for i in range(0, gcd):
    for letter in possibilities_letters[i]:
        key1+=letter

l=3

tuples=list(itertools.product(range(0, l), repeat=len(possibilities_letters)))
keys=[]
for tup in tuples:
    key=''
    for j in range(0,len(possibilities_letters)):           
        key+=possibilities_letters[j][list(tup)[j]]
    keys.append(key)

d = enchant.Dict("en_US")


for key in keys:
    decoded_text=''
    key_index=0
    bools_ctr=0
    for c in ct:
        if c ==' ':
           decoded_text=decoded_text+' '
        else: 
            decoded_text=decoded_text+pos_to_char((char_position(c)-char_position(key[key_index]))%26)
            key_index=(key_index+1)%len(key) 
    dec_words=decoded_text.split(' ')
    for word in dec_words:
        if d.check(word):
            bools_ctr=bools_ctr+1
    if bools_ctr/len(dec_words)>0.7:
        break
print("key:", key)
print("plaintext:",  decoded_text)

