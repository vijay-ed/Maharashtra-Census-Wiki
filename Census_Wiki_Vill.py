
#import math

# import openpyxl
# Improved from CensusWikiTwo.py
# Uses districtwise data in English is used
# Asks for census code of a village
# Village names are converted into Devnagari
# Numbers are also converted into Devnagari
# Creates a text for the article which is saved in 'wikipage_text.text'

a1 = '5 की.मी.पेक्षा कमी '
b1 = '5 ते 10 की.मी.'
c1 = '10 की.मी. पेक्षा अधिक '

def Education(nos, desc, at, distance):
    if distance == 'a':
        distance = a1
    elif distance == 'b':
        distance = b1
    elif distance == 'c':
        distance = c1
    else:
        distance = 'not recorded'
    strAvl, strAt = '', ''
    if nos > 0:
        strAvl = desc + '-' + str(int(nos)) + '.  '
    else:
        strAt = desc + ' ' + at + ' येथे आहे.  '
    return strAvl, distance, strAt


def ifyn(desc, yn):
    nString, yString, ynString = '', '', ''
    if yn == 1:
        yString = desc
    elif yn == 2:
        nString = desc
    else:
        ynString = desc
    return nString, yString, ynString


def yORat(desc, ifAvlable, else_at):
    if else_at == 'a':
            else_at = a1
    elif else_at == 'b':
            else_at = b1
    elif else_at == 'c':
            else_at = c1
    else :
            else_at = 'abc'
    strAvl, strNoKnw, strAt = '', '', ''
    if ifAvlable == 1:
        strAvl = desc
    elif ifAvlable == 2 and else_at == 'abc':
        strNoKnw = (desc)  # availability is not known \n")
    elif ifAvlable == 2 and else_at != 'abc':
        strAt = desc + "- " + else_at + 'अंतरावर.  '  # " # is available at "+ else_at+" \n")

    return strAvl, strNoKnw, strAt


def yn_1_2(s):
    if s == 1:
        s = " आहे. "
    elif s == 2:
        s = " नाही. "
    else:
        s = ' माहीती उपलब्ध नाही'  # s=(str(int(s))+"आहे.")  int(math.sqrt(5))
    return s


def if_y_n(p, l):
    nString, yString = '', ''
    p = int(p)
    if p > 0:
        yString = l + '-' + str(p)+', '
    else:
        nString = l
    return nString, yString


####


#while i < 1:  # tot_rows-1 :
def main():
    # to add wikipage_text=""
    wikipage_text = ""
    L = ''
    box1 = "{{माहितीचौकट भारतीय न्यायक्षेत्र\n"
    box2 = "|प्रकार=गाव\n" + "|जनगणना_स्थलनिर्देशांक= " + str(df.iat[i, 6]) + "\n"
    box3 = "|स्थानिक_नाव=" + df.iat[i, 7] + "\n" + "|तालुका_नाव=" + df.iat[i, 5] + "\n" + "|जिल्हा_नाव=" + df.iat[
        i, 3] + "\n" + "|राज्य_नाव =महाराष्ट्र" + "\n" + "|विभाग=\n"
    box4 = "|जिल्हा=[[" + df.iat[i, 3] + "]]\n" + "|तालुका_नावे =[[" + df.iat[i, 5] + "]]\n"

    box5 = "|अक्षांश=\n" + "|रेखांश=\n" + "|शोधक_स्थान =right\n" + "|क्षेत्रफळ_एकूण="
    dec = Decimal(df.iat[i, 23] / 100).quantize(Decimal("100.00"))
    box6 = str(dec) + "\n" + "|उंची=\n""|लोकसंख्या_एकूण=" + str(df.iat[i, 25]) + "\n" + "|लोकसंख्या_वर्ष=२०११\n"
    if df.iat[i, 23] == '' or df.iat[i, 23] == 0 :
        print("Invalid village Area")
        sys.exit()
    dec = Decimal(100 * df.iat[i, 25] / df.iat[i, 23]).quantize(Decimal("100.00"))
    box7 = "|लोकसंख्या_घनता=" + str(dec) + "\n" + "|लोकसंख्या_पुरुष=" + str(
    df.iat[i, 26]) + "\n" + "|लोकसंख्या_स्त्री=" + str(df.iat[i, 27]) + "\n"
    try:
        dec = Decimal(1000 * df.iat[i, 27] / df.iat[i, 26]).quantize(Decimal("1000"))
        box8 = "|लिंग_गुणोत्तर=" + str(dec) + "\n"
    except (ValueError, ZeroDivisionError) as e:
        print('something went wrong')
        sys.exit()

    box9 = "|अधिकृत_भाषा=[[मराठी]]\n}}\n"
    L = box1 + box2 + box3 + box4 + box5 + box6 + box7 + box8 + box9
    wikipage_text += L
    str00 = "सेन्सस कोड " + str(df.iat[i, 6]) + " असलेले '''" + df.iat[i, 7] + "''' हे गाव, " + (
    df.iat[i, 3]) + " या जिल्ह्यातील " + str(df.iat[i, 23]) + " हेक्टर क्षेत्राचे गाव असून  ह्या गावात " + str(
        df.iat[i, 24]) + " कुटुंबे आहेत  व एकूण लोकसंख्या " + str(df.iat[i, 25]) + " आहे."
    str01 = "ह्याच्या सर्वात जवळचे शहर " + str(df.iat[i, 15]) + " हे " + str(df.iat[i, 16]) + " किलोमीटर अंतरावर आहे.\n"
    L = str00 + str01 + "या लेखातील माहिती २०११ च्या शिरगणतीनुसार <ref>https://censusindia.gov.in/census.website/data/census-tables#</ref> आहे. शिरगणतीत नसलेल्या माहितीसाठी वेगळा संदर्भ दिला आहे."
    wikipage_text += L
    str1= '\n== जन सांख्यिकी ==\n'
    str2= '* एकूण लोकसंख्या:'+ str(df.iat[i,25])+'; पुरुष: '+ str(df.iat[i,26])+'; स्त्रिया: '+ str(df.iat[i,27]) +'\n'
    str2 = str2 + '* अनुसूचित जाती लोकसंख्या: '+ str(df.iat[i,28])+'; पुरुष: '+ str(df.iat[i,29])+'; स्त्रिया: '+ str(df.iat[i,30]) +'\n'
    str2 = str2 + '* अनुसूचित जमाती लोकसंख्या:'+ str(df.iat[i,31])+'; पुरुष: '+ str(df.iat[i,32])+'; स्त्रिया: '+ str(df.iat[i,33]) +'\n'
    wikipage_text += str1+str2
    str4 = '== शैक्षणिक सुविधा ==\n'

    L = str4  # +L1+L2+L3+L4+L5+L6+L7+L8+L9+L10+L11+L12+L13+"\n"
    wikipage_text += L
    strAvl = [''] * 14
    dist = [''] * 14
    strAt = [''] * 14

    strAvl[1], dist[1], strAt[1] = Education(df.iat[i, 35] + df.iat[i, 37], "पूर्व-प्राथमिक शाळा", df.iat[i, 39],
                                             df.iat[i, 40])
    strAvl[2], dist[2], strAt[2] = Education(df.iat[i, 42] + df.iat[i, 44], "प्राथमिक शाळा", df.iat[i, 46],
                                             df.iat[i, 47])
    # print(L2)
    strAvl[3], dist[3], strAt[3] = Education(df.iat[i, 49] + df.iat[i, 51], "कनिष्ठ माध्यमिक शाळा", df.iat[i, 53],
                                             df.iat[i, 54])
    # print(L3)
    strAvl[4], dist[4], strAt[4] = Education(df.iat[i, 56] + df.iat[i, 58], "माध्यमिक शाळा", df.iat[i, 60],
                                             df.iat[i, 61])
    # print(L4)
    strAvl[5], dist[5], strAt[5] = Education(df.iat[i, 63] + df.iat[i, 65], "उच्च माध्यमिक शाळा ", df.iat[i, 67],
                                             df.iat[i, 68])
    # print(L5)
    strAvl[6], dist[6], strAt[6] = Education(df.iat[i, 70] + df.iat[i, 72], "पदवी महाविद्यालय ", df.iat[i, 74],
                                             df.iat[i, 75])
    # print(L6)
    strAvl[7], dist[7], strAt[7] = Education(df.iat[i, 77] + df.iat[i, 79], "इंजिनियरिंग महाविद्यालय ", df.iat[i, 81],
                                             df.iat[i, 82])
    # print(L7)
    strAvl[8], dist[8], strAt[8] = Education(df.iat[i, 84] + df.iat[i, 86], "वैद्यकीय महाविद्यालय ", df.iat[i, 88],
                                             df.iat[i, 89])
    # L8=facility( df.iat[i,84]+df.iat[i,86],"वैद्यकीय महाविद्यालय ",df.iat[i,88],df.iat[i,89])
    strAvl[11], dist[11], strAt[11] = Education(df.iat[i, 105] + df.iat[i, 107], "व्यावसायिक प्रशिक्षण शाळा ",
                                                df.iat[i, 109], df.iat[i, 110])
    # print(L11)
    strAvl[12], dist[12], strAt[12] = Education(df.iat[i, 112] + df.iat[i, 114], "अनौपचारिक प्रशिक्षण केन्द्र ",
                                                df.iat[i, 116], df.iat[i, 117])
    # print(L12)
    strAvl[13], dist[13], strAt[13] = Education(df.iat[i, 119] + df.iat[i, 121], "अपंगांसाठी खास शाळा ", df.iat[i, 123],
                                                df.iat[i, 124])
    # strAvl = (strAvl1+ strAvl2 + strAvl3 + strAvl4 + strAvl5 + strAvl6 + strAvl7 + strAvl8 + strAvl9 \
    #    + strAvl10 + strAvl11 + strAvl12 + strAvl13 )
    j = 1
    strAvlble, stra1, strb1, strc1 = '', '', '', ''
    while j < 14:
        strAvlble += strAvl[j]
        if dist[j] == a1:
            stra1 += strAt[j]
        elif dist[j] == b1:
            strb1 += strAt[j]
        else:
            strc1 += strAt[j]
        j += 1

    if strAvlble == '':
        strAvlble = 'काही नाही'
    wikipage_text += ("गावात असणाऱ्या सुविधा - " + strAvlble)

    # strAt = (strAt1 + strAt2 + strAt3 + strAt4 + strAt5 + strAt6 + strAt7 + strAt8 + strAt9 \
    #   + strAt10 + strAt11 + strAt12 + strAt13 )
    wikipage_text += ("<br>स्थानिक नसलेल्या सुविधांची अंतरे  - \n")
    if stra1 == '':
        stra1 = 'काही नाही'  # wikipage_text +=(a1+'अंतरावर : '+ stra1+'\n') #+b1+'अंतरावर : '+ strb1+'\n'+c1+'अंतरावर : '+ strc1+'\n')
    if strb1 == '':
        strb1 = 'काही नाही'  # wikipage_text +=(b1+'अंतरावर : '+ strb1+'\n')
    if strc1 == '':
        strc1 = 'काही नाही'
        # wikipage_text +=(c1+'अंतरावर : '+ strc1+'\n')

    wikipage_text += (
                '<br>' + a1 + 'अंतरावर : ' + stra1 + '<br>' + b1 + 'अंतरावर : ' + strb1 + '<br>' + c1 + 'अंतरावर : ' + strc1 + '\n')

    L14 = "== वैद्यकीय सुविधा-सरकारी ==" + "\n"
    nList, yList = '', ''
    # L15=" कम्युनिटी हेल्थ सेंटर " + (no_for_0( df.iat[i,132]))
    nStr15, yStr15 = if_y_n(df.iat[i, 132], 'कम्युनिटी हेल्थ सेंटर ')

    # L16=" प्राथमिक आरोग्य केन्द्र" + (no_for_0( df.iat[i,138]))
    nStr16, yStr16 = if_y_n(df.iat[i, 138], "प्राथमिक आरोग्य केन्द्र ")

    # L17=" प्राथमिक आरोग्य उपकेन्द्र " + (no_for_0( df.iat[i,144]))
    nStr17, yStr17 = if_y_n(df.iat[i, 144], "प्राथमिक आरोग्य उपकेन्द्र ")

    # L18=" प्रसूति व शिशुसंगोपन केन्द्र" + ( no_for_0(df.iat[i,150]))
    nStr18, yStr18 = if_y_n(df.iat[i, 150], "प्रसूति व शिशुसंगोपन केन्द्र ")

    # L19=" क्षयरोग रुग्णालय " + ( no_for_0(df.iat[i,156]))
    nStr19, yStr19 = if_y_n(df.iat[i, 156], "क्षयरोग रुग्णालय ")

    # L20=" अ‍ॅलोपॅथिक रुग्णालय " + (no_for_0(df.iat[i,162]))
    nStr20, yStr20 = if_y_n(df.iat[i, 162], "अ‍ॅलोपॅथिक रुग्णालय ")

    # L21=" अन्य उपचार पद्धतीचे रुग्णालय " + ( no_for_0(df.iat[i,168]))
    nStr21, yStr21 = if_y_n(df.iat[i, 168], "अन्य उपचार पद्धतीचे रुग्णालय ")

    # L22=" दवाखाने " + (no_for_0( df.iat[i,174]))
    nStr22, yStr22 = if_y_n(df.iat[i, 174], "दवाखाने ")

    # L23=" गुरांचे दवाखाने  " + (no_for_0( df.iat[i,180]))
    nStr23, yStr23 = if_y_n(df.iat[i, 180], "गुरांचे दवाखाने ")

    # L24=" फिरते दवाखाने " + (no_for_0( df.iat[i,186]))
    nStr24, yStr24 = if_y_n(df.iat[i, 186], "फिरते दवाखाने ")

    # L25=" कुटुंब कल्याण केन्द्र " + (no_for_0( df.iat[i,192]))
    nStr25, yStr25 = if_y_n(df.iat[i, 192], "कुटुंब कल्याण केन्द्र ")

    # L= L14+L15+L16+L17+L18+L19+L20+L21+L22+L23+L24+L25 +"\n"
    nStr = nStr15 + nStr16 + nStr17 + nStr18 + nStr19 + nStr20 + nStr21 + nStr22 + nStr23 + nStr24 + nStr25
    yStr = yStr15 + yStr16 + yStr17 + yStr18 + yStr19 + yStr20 + yStr21 + yStr22 + yStr23 + yStr24 + yStr25

    wikipage_text += L14
    if yStr != '':
        wikipage_text += ('असलेल्या सुविधा- \n' + yStr + '\n')
    else:
        wikipage_text += ('असलेल्या सुविधा- काही नाही' + '\n')

    wikipage_text += ('<br>नसलेल्या सुविधा - \n' + nStr + '\n')

    L26 = "== वैद्यकीय सुविधा-बिगर-सरकारी == \n"

    # L27=" बाह्य रोगी विभाग " + (no_for_0( df.iat[i,198]))
    nStr27, yStr27 = if_y_n(df.iat[i, 198], "बाह्य रोगी विभाग ")

    # L28=" बाह्य व भरती असलेले रोगी विभाग " + (no_for_0( df.iat[i,199]))
    nStr28, yStr28 = if_y_n(df.iat[i, 199], "बाह्य व भरती असलेले रोगी विभाग ")

    # L29=" धर्मादाय बिगर-सरकारी रुग्णालय " + (no_for_0( df.iat[i,200]))
    nStr29, yStr29 = if_y_n(df.iat[i, 200], "धर्मादाय बिगर-सरकारी रुग्णालय ")

    # L30=" एम बी बी एस पदवीधर डॉक्टर " + (no_for_0( df.iat[i,201]))
    nStr30, yStr30 = if_y_n(df.iat[i, 201], "एम बी बी एस पदवीधर डॉक्टर ")

    # L31=" इतर पदवीधर डॉक्टर " + (no_for_0( df.iat[i,202]))
    nStr31, yStr31 = if_y_n(df.iat[i, 202], "इतर पदवीधर डॉक्टर ")

    # L32=" पदवी नसलेले डॉक्टर " + (no_for_0( df.iat[i,203]))
    nStr32, yStr32 = if_y_n(df.iat[i, 203], "पदवी नसलेले डॉक्टर ")

    # L33=" पारंपरिक वैद्य व वैदू " + (no_for_0( df.iat[i,204]))
    nStr33, yStr33 = if_y_n(df.iat[i, 204], "पारंपरिक वैद्य व वैदू ")

    # L34=" औषधाची दुकाने " + (no_for_0( df.iat[i,205]))
    nStr34, yStr34 = if_y_n(df.iat[i, 205], "औषधाची दुकाने ")

    # L35=" इतर बिगरसरकारी वैद्यकीय सुविधा " + (no_for_0( df.iat[i,206]))
    nStr35, yStr35 = if_y_n(df.iat[i, 206], "इतर बिगरसरकारी वैद्यकीय सुविधा ")

    # L=L26+L27+L28+L29+L30+L31+L32+L33+L34+L35 +"\n"
    nStr = nStr27 + nStr28 + nStr29 + nStr30 + nStr31 + nStr32 + nStr33 + nStr34 + nStr35
    yStr = yStr27 + yStr28 + yStr29 + yStr30 + yStr31 + yStr32 + yStr33 + yStr34 + yStr35
    # wikipage_text += L
    wikipage_text += L26
    if yStr != '':
        wikipage_text += ('असलेल्या सुविधा- \n' + yStr + '\n')
    else:
        wikipage_text += ('असलेल्या सुविधा- काही नाही' + '\n')

    wikipage_text += ('<br>नसलेल्या सुविधा - ' + '\n' + nStr + '\n')

    # Drinking water status
    L36 = "== पिण्याचे पाणी ==" + "\n"
    nStr37, yStr37, ynStr37 = ifyn('शुद्ध केलेल्या नळाच्या पाण्याचा पुरवठा, ', df.iat[i, 208 - 1])
    nStr38, yStr38, ynStr38 = ifyn('शुद्ध न केलेल्या नळाच्या पाण्याचा पुरवठा, ', df.iat[i, 211 - 1])
    nStr39, yStr39, ynStr39 = ifyn('झाकण असलेल्या विहिरीच्या पाण्याचा पुरवठा, ', df.iat[i, 214 - 1])
    nStr40, yStr40, ynStr40 = ifyn('झाकण नसलेल्या विहिरीच्या पाण्याचा पुरवठा, ', df.iat[i, 217 - 1])
    nStr41, yStr41, ynStr41 = ifyn('हँड पंपच्या पाण्याचा पुरवठा, ', df.iat[i, 220 - 1])
    nStr42, yStr42, ynStr42 = ifyn('बारमाही सुरू असलेल्या हँड पंपच्या पाण्याचा पुरवठा, ', df.iat[i, 221 - 1])
    nStr43, yStr43, ynStr43 = ifyn('बोअर वेलच्या पाण्याचा पुरवठा, ', df.iat[i, 223 - 1])
    nStr44, yStr44, ynStr44 = ifyn('बारमाही सुरू असलेल्या बोअरवेल पाण्याचा पुरवठा, ', df.iat[i, 224 - 1])
    nStr45, yStr45, ynStr45 = ifyn('झऱ्यांच्या पाण्याचा पुरवठा, ', df.iat[i, 226 - 1])
    nStr46, yStr46, ynStr46 = ifyn('नदी /कालवे यातील  पाण्याचा पुरवठा, ', df.iat[i, 229 - 1])
    nStr47, yStr47, ynStr47 = ifyn('तलाव / तळी यातील  पाण्याचा पुरवठा, ', df.iat[i, 232 - 1])
    nStr48, yStr48, ynStr48 = ifyn('इतर पाण्याचा पुरवठा, ', df.iat[i, 235 - 1])
    nStr = nStr37 + nStr38 + nStr39 + nStr40 + nStr41 + nStr42 + nStr43 + nStr44 + nStr45 + nStr46 + nStr47 + nStr48
    yStr = yStr37 + yStr38 + yStr39 + yStr40 + yStr41 + yStr42 + yStr43 + yStr44 + yStr45 + yStr46 + yStr47 + yStr48
    ynStr = ynStr37 + ynStr38 + ynStr39 + ynStr40 + ynStr41 + ynStr42 + ynStr43 + ynStr44 + ynStr45 + ynStr46 + ynStr47 + ynStr48

    L = L36  # +L37+L38+L39+L40+L41+L42+L43+L44+L45+L46+L47+L48+"\n"
    wikipage_text += L

    if yStr != '':
        wikipage_text += ('असलेल्या सुविधा- \n' + yStr + '\n')
    else:
        wikipage_text += ('असलेल्या सुविधा- निरंक \n')

    wikipage_text += ('<br>नसलेल्या सुविधा - \n' + nStr + '\n')

    if ynStr != '':
        wikipage_text += ('\nमाहिती उपलब्ध नसलेल्या सुविधा- \n' + ynStr + '\n')

    L = "== स्वच्छता == \n"

    if df.iat[i, 244 - 1] == 1:
        L50 = ("सांडपाणी पाण्याच्या स्त्रोतात सोडले जाते.")
    else:
        L50 = ("सांडपाणी शुद्धीकरणाच्या सयंत्रात सोडले जाते.")
    # L50=ifyn("Whether Drain water is discharged directly into water bodies or to sewar plant",df.iat[i,244-1])
    nStr49, yStr49, ynStr49 = ifyn("उघडी गटारे, ", df.iat[i, 239 - 1])
    nStr51, yStr51, ynStr51 = ifyn("न्हाणीघरासह सार्वजनिक स्वच्छता गृह, ", df.iat[i, 246 - 1])

    # Community Toilet Complex (including Bath) for General Public 246
    nStr52, yStr52, ynStr52 = ifyn("न्हाणीघराशिवाय सार्वजनिक स्वच्छता गृह, ", df.iat[i, 247 - 1])
    # Community Toilet Complex (excluding Bath) for General Public (Status  247
    nStr53, yStr53, ynStr53 = ifyn("ग्रामीण सॅनिटरी हार्डवेयरचे दुकान, ", df.iat[i, 249 - 1])
    # Rural Production Centres or Sanitary hardware outlet availability near the village 248
    nStr54, yStr54, ynStr54 = ifyn("सामूहिक बायोगॅस किंवा कचऱ्याच्या उत्पादक पुनर्वापराची व्यवस्था, ", df.iat[i, 251 - 1])
    # Community Bio-gas or recycle of waste for production use  251
    # L= str1+L49+L50+L51+L52+L53+L54+ "\n"

    wikipage_text += L
    # wikipage_text += L50
    nStr = nStr49 + nStr51 + nStr52 + nStr53 + nStr54
    yStr = L50 + yStr49 + yStr51 + yStr52 + yStr53 + yStr54
    if yStr != '':
        wikipage_text += ('असलेल्या  सुविधा- \n' + yStr + '\n')
    else:
        wikipage_text += ('असलेल्या सुविधा- निरंक \n')

    wikipage_text += ('<br>नसलेल्या सुविधा - \n' + nStr + '\n')

    str1 = "== संचार == \n"
    strAvl55, strNoKnw55, strAt55 = yORat("पोस्ट ऑफिस, ", df.iat[i, 252], df.iat[i, 253])
    # Post Office 253-1, 254-1
    # print(L56)
    strAvl56, strNoKnw56, strAt56 = yORat("उपपोस्ट ऑफिस, ", df.iat[i, 254], df.iat[i, 255])
    # Sub Post Office 255-1, 256-1
    strAvl57, strNoKnw57, strAt57 = yORat("मोबाइल फोन सुविधा, ", df.iat[i, 265], df.iat[i, 266])
    # Mobile Phone Coverage 266-1,267-1
    strAvl58, strNoKnw58, strAt58 = yORat("इंटरनेट कॅफे / सर्व्हिस सेंटर, ", df.iat[i, 267], df.iat[i, 268])
    # Internet Cafes / Common Service Centre 268-1,269-1
    strAvl59, strNoKnw59, strAt59 = yORat("खाजगी कूरियर, ", df.iat[i, 269], df.iat[i, 270])
    # Private Courier Facility 270-1, 271-1
    strAvl60, strNoKnw60, strAt60 = yORat("सार्वजनिक  बस सेवा, ", df.iat[i, 271], df.iat[i, 272])
    # Public Bus Service 272-1,273-1
    strAvl61, strNoKnw61, strAt61 = yORat("खाजगी बस सेवा, ", df.iat[i, 273], df.iat[i, 274])
    # Private Bus Service 274-1,275-1
    strAvl62, strNoKnw62, strAt62 = yORat("रेल्वे स्टेशन, ", df.iat[i, 275], df.iat[i, 276])
    # Railway Station 276-1,277-1
    strAvl63, strNoKnw63, strAt63 = yORat("ऑटो व टमटम, ", df.iat[i, 277], df.iat[i, 278])
    # Auto/Modified Autos 278-1,279-1
    strAvl64, strNoKnw64, strAt64 = yORat("टॅक्सी, ", df.iat[i, 279], df.iat[i, 280])
    # Taxi 280-1,281-1
    strAvl65, strNoKnw65, strAt65 = yORat("ट्रॅक्टर ", df.iat[i, 283], df.iat[i, 284])
    # Tractors 284-1,285-1
    strAvl66, strNoKnw66, strAt66 = yORat("सायकल रिक्षा (पायचाकी), ", df.iat[i, 285], df.iat[i, 286])
    # Cycle-pulled Rickshaws   (manual driven)286-1,287-1
    strAvl67, strNoKnw67, strAt67 = yORat("सायकल रिक्षा (यांत्रिक), ", df.iat[i, 287], df.iat[i, 288])
    # Cycle-pulled Rickshaws (machine driven) 288-1,289-1
    strAvl68, strNoKnw68, strAt68 = yORat("बैल व इतर जनावरांनी ओढलेल्या गाड्या, ", df.iat[i, 289], df.iat[i, 290])
    # Carts Drivens by Animals 290-1,291-1
    strAvl69, strNoKnw69, strAt69 = yORat("समुद्र व नदीवरील बोट वाहतूक, ", df.iat[i, 291], df.iat[i, 292])
    # Sea/River/Ferry Service 292-1,293-1
    strAvl70, strNoKnw70, strAt70 = yORat("राष्ट्रीय महामार्गाला जोडलेले रस्ते, ", df.iat[i, 293], df.iat[i, 294])
    # National Highway  294-1,295-1
    strAvl71, strNoKnw71, strAt71 = yORat("राज्य महामार्गाला जोडलेले रस्ते, ", df.iat[i, 295], df.iat[i, 296])
    # State Highway 296-1,297-1
    strAvl72, strNoKnw72, strAt72 = yORat("जिल्ह्यातील मुख्य रस्त्याला जोडलेले रस्ते, ", df.iat[i, 297], df.iat[i, 298])
    # Major District Road 298-1,299-1
    strAvl73, strNoKnw73, strAt73 = yORat("जिल्ह्यातील दुय्यम रस्त्याना जोडलेले रस्ते, ", df.iat[i, 299],
                                          df.iat[i, 300])
    # Other District Road 300-1,301-1
    strAvl74, strNoKnw74, strAt74 = yORat("डांबरी रस्ते, ", df.iat[i, 301], df.iat[i, 302])
    # Black Topped (pucca) Road 302-1,303-1
    strAvl75, strNoKnw75, strAt75 = yORat("कच्चे रस्ते, ", df.iat[i, 303], df.iat[i, 304])
    # Gravel (kuchha) Roads 304-1,305-1
    strAvl76, strNoKnw76, strAt76 = yORat("पाण्यासाठी नाल्या असणारे डांबरी रस्ते, ", df.iat[i, 305], df.iat[i, 306])
    # Water Bounded Macadam 306-1,307-1
    strAvl77, strNoKnw77, strAt77 = yORat("बारमाही रस्ते, ", df.iat[i, 307], df.iat[i, 308])
    # Weather Road 308-1,309-1
    strAvl78a, strNoKnw78a, strAt78a = yORat("बोट वाहतुकीयोग्य जलमार्ग, ", df.iat[i, 309], df.iat[i, 310])
    # Navigable Waterways 310-1,311-1
    wikipage_text += str1

    strAvl = (strAvl55 + strAvl56 + strAvl57 + strAvl58 + strAvl59 + strAvl60 + strAvl61 + strAvl62 + strAvl63
              + strAvl64 + strAvl65 + strAvl66 + strAvl67 + strAvl68 + strAvl69 + strAvl70 + strAvl71
              + strAvl72 + strAvl73 + strAvl74 + strAvl75 + strAvl76 + strAvl77 + strAvl78a)  # + strAvl55 + strAvl55 + strAvl55 + strAvl55 + strAvl55 + strAvl55 + strAvl55 + strAvl55 + strAvl55 + strAvl55 + strAvl55 + strAvl55 + strAvl55 + strAvl55 + strAvl55 + strAvl55 + strAvl55 +
    wikipage_text += ("गावात असणाऱ्या सुविधा - \n" + strAvl)

    strAt = (strAt55 + strAt56 + strAt57 + strAt58 + strAt59 + strAt60 + strAt61 + strAt62 + strAt63
             + strAt64 + strAt65 + strAt66 + strAt67 + strAt68 + strAt69 + strAt70 + strAt71
             + strAt72 + strAt73 + strAt74 + strAt75 + strAt76 + strAt77 + strAt78a)  # + strAt55 + strAt55 + strAt55 + strAt55 + strAt55 + strAt55 + strAt55 + strAt55 + strAt55 + strAt55 + strAt55 + strAt55 + strAt55 + strAt55 + strAt55 + strAt55 + strAt55 +
    wikipage_text += ("<br>स्थानिक नसलेल्या सुविधांची अंतरे  - \n" + strAt)

    strNoKnw = (
                strNoKnw55 + strNoKnw56 + strNoKnw57 + strNoKnw58 + strNoKnw59 + strNoKnw60 + strNoKnw61 + strNoKnw62 + strNoKnw63
                + strNoKnw64 + strNoKnw65 + strNoKnw66 + strNoKnw67 + strNoKnw68 + strNoKnw69 + strNoKnw70 + strNoKnw71
                + strNoKnw72 + strNoKnw73 + strNoKnw74 + strNoKnw75 + strNoKnw76 + strNoKnw77 + strNoKnw78a)  # + strNoKnw55 + strNoKnw55 + strNoKnw55 + strNoKnw55 + strNoKnw55 + strNoKnw55 + strNoKnw55 + strNoKnw55 + strNoKnw55 + strNoKnw55 + strNoKnw55 + strNoKnw55 + strNoKnw55 + strNoKnw55 + strNoKnw55 + strNoKnw55 + strNoKnw55 +
    wikipage_text += (
                "<br>'''तळटीप'''- शिरगिणतीत असलेल्या पुढील सुविधांच्या उपलब्धततेची माहिती नाही  - " + strNoKnw + '\n')

    # Market and Banking facility
    str1 = "== बाजार व पतव्यवस्था == \n"
    strAvl78, strNoKnw78, strAt78 = yORat("ए टी एम, ", df.iat[i, 313], df.iat[i, 314])
    # ATM 313,314
    strAvl79, strNoKnw79, strAt79 = yORat("व्यापारी बँका, ", df.iat[i, 315], df.iat[i, 316])
    # Commercial Bank 315,316
    strAvl80, strNoKnw80, strAt80 = yORat("सहकारी बँका, ", df.iat[i, 317], df.iat[i, 318])
    # Cooperative Bank
    strAvl81, strNoKnw81, strAt81 = yORat("शेतकी कर्ज संस्था, ", df.iat[i, 319], df.iat[i, 320])
    # Agricultural Credit Societies 319,320
    strAvl82, strNoKnw82, strAt82 = yORat("स्वसहाय्य गट (SHG), ", df.iat[i, 321], df.iat[i, 322])
    # Self - Help Group (SHG)321,322
    strAvl83, strNoKnw83, strAt83 = yORat("रेशनचे दुकान, ", df.iat[i, 323], df.iat[i, 324])
    # Public Distribution System (PDS) Shop 323,324
    strAvl84, strNoKnw84, strAt84 = yORat("मंडया / कायम बाजार, ", df.iat[i, 325], df.iat[i, 326])
    # Mandis/Regular Market 325,326
    strAvl85, strNoKnw85, strAt85 = yORat("आठवड्याचा बाजार, ", df.iat[i, 327], df.iat[i, 328])
    # Weekly Haat 327,328
    strAvl86, strNoKnw86, strAt86 = yORat("शेतमाल विक्री संस्था, ", df.iat[i, 329], df.iat[i, 330])
    # Agricultural Marketing Society 329,330
    # L= str1+L78+L79+L80+L81+L82+L83+L84+L85+L86+"\n"

    wikipage_text += str1
    strAvl = strAvl78 + strAvl79 + strAvl80 + strAvl81 + strAvl82 + strAvl83 + strAvl84 + strAvl85 + strAvl86  # + strAvl55 + strAvl55 + strAvl55 + strAvl55 + strAvl55 + strAvl55 + strAvl55 + strAvl55 + strAvl55 + strAvl55 + strAvl55 + strAvl55 + strAvl55 + strAvl55 + strAvl55 + strAvl55 + strAvl55 +
    wikipage_text += ("गावात असणाऱ्या सुविधा - " + strAvl + "\n")

    strAt = strAt78 + strAt79 + strAt80 + strAt81 + strAt82 + strAt83 + strAt84 + strAt85 + strAvl86
    wikipage_text += ("<br>स्थानिक नसलेल्या सुविधांची अंतरे - \n" + strAt + "\n")

    strNoKnw = strNoKnw78 + strNoKnw79 + strNoKnw80 + strNoKnw81 + strNoKnw82 + strNoKnw83 + strNoKnw84 + strNoKnw85 + strNoKnw86  # + strNoKnw55 + strNoKnw55 + strNoKnw55 + strNoKnw55 + strNoKnw55 + strNoKnw55 + strNoKnw55 + strNoKnw55 + strNoKnw55 + strNoKnw55 + strNoKnw55 + strNoKnw55 + strNoKnw55 + strNoKnw55 + strNoKnw55 + strNoKnw55 + strNoKnw55 +
    if strNoKnw != '':
        wikipage_text += (
                    "<br>'''तळटीप'''- शिरगिणतीत असलेल्या पुढील सुविधांच्या उपलब्धततेची माहिती नाही  - \n" + strNoKnw + "\n")

    #  Health, nutrition, entertainment amenities
    str1 = "== आरोग्य, आहार व करमणूक सुविधा ==\n"
    strAvl87, strNoKnw87, strAt87 = yORat("शिशुविकास पौष्टिक आहार केन्द्र (ICDS), ", df.iat[i, 331], df.iat[i, 332])
    # Integrated Child Development Scheme (Nutritional Centres) facility 331,332
    strAvl88, strNoKnw88, strAt88 = yORat("अंगणवाडी पौष्टिक आहार केन्द्र, ", df.iat[i, 333], df.iat[i, 334])
    # Nutritional Centres-Anganwadi Centre 333,334
    strAvl89, strNoKnw89, strAt89 = yORat("इतर  पौष्टिक आहार केन्द्र, ", df.iat[i, 335], df.iat[i, 336])
    # Nutritional Centres-Others 335,336
    strAvl90, strNoKnw90, strAt90 = yORat("आशा, ", df.iat[i, 337], df.iat[i, 338])
    # ASHA 337,338
    strAvl91, strNoKnw91, strAt91 = yORat("समुदाय भवन (टीव्ही सह अथवा विरहित), ", df.iat[i, 339], df.iat[i, 340])
    # Community Centre with/without TV 339,340
    strAvl92, strNoKnw92, strAt92 = yORat("क्रीडांगण, ", df.iat[i, 341], df.iat[i, 342])
    # Sports Field 341,342
    strAvl93, strNoKnw93, strAt93 = yORat("खेळ / करमणूक क्लब, ", df.iat[i, 343], df.iat[i, 344])
    # Sports Club/Recreation Centre 343,344
    strAvl94, strNoKnw94, strAt94 = yORat("सिनेमा/ व्हिडियो थियेटर, ", df.iat[i, 345], df.iat[i, 346])
    # Cinema/Video Hall 345,346
    strAvl95, strNoKnw95, strAt95 = yORat("सार्वजनिक ग्रंथालय, ", df.iat[i, 347], df.iat[i, 348])
    # Public Library 347,348
    strAvl96, strNoKnw96, strAt96 = yORat("सार्वजनिक वाचनालय, ", df.iat[i, 349], df.iat[i, 350])
    # Public Reading Room 349,350
    strAvl97, strNoKnw97, strAt97 = yORat("वृत्तपत्र पुरवठा, ", df.iat[i, 351], df.iat[i, 352])
    # Daily Newspaper Supply 351,352
    strAvl98, strNoKnw98, strAt98 = yORat("विधानसभा मतदान केन्द्र, ", df.iat[i, 353], df.iat[i, 354])
    # Assembly Polling Station 353,354
    strAvl99, strNoKnw99, strAt99 = yORat("जन्म व मृत्यु नोंदणी केन्द्र, ", df.iat[i, 355], df.iat[i, 356])
    # Birth and Death Registration Office  355,356

    wikipage_text += str1
    # L= str1+L87+L88+L89+L90+L91+L92+L93+L94+L95+L96+L97+L98+L99+"\n"
    strAvl = (strAvl87 + strAvl88 + strAvl88 + strAvl89 + strAvl90 + strAvl91 + strAvl92 + strAvl93 + strAvl94
              + strAvl95 + strAvl96 + strAvl97 + strAvl98 + strAvl99)  # + strAvl55 + strAvl55 + strAvl55 + strAvl55 + strAvl55 + strAvl55 + strAvl55 + strAvl55 + strAvl55 + strAvl55 + strAvl55 + strAvl55 + strAvl55 + strAvl55 + strAvl55 + strAvl55 + strAvl55 +
    wikipage_text += ("गावात असणाऱ्या सुविधा - \n" + strAvl + "\n")

    strAt = (strAt87 + strAt88 + strAt88 + strAt89 + strAt90 + strAt91 + strAt92 + strAt93 + strAt94
             + strAt95 + strAt96 + strAt97 + strAt98 + strAt99)
    wikipage_text += ("<br>स्थानिक नसलेल्या सुविधांची अंतरे - \n" + strAt + "\n")

    strNoKnw = (
                strNoKnw87 + strNoKnw88 + strNoKnw88 + strNoKnw89 + strNoKnw90 + strNoKnw91 + strNoKnw92 + strNoKnw93 + strNoKnw94
                + strNoKnw95 + strNoKnw96 + strNoKnw97 + strNoKnw98 + strNoKnw99)
    if strNoKnw != '':
        wikipage_text += (
                    "<br>'''तळटीप'''- शिरगिणतीत असलेल्या पुढील सुविधांच्या उपलब्धततेची माहिती नाही  - \n" + strNoKnw + "\n")

    # Electricity
    str1 = "== वीज पुरवठा ==\n"

    # Power Supply For Domestic Use 357
    L100 = 'घरगुती वापरासाठी वीजपुरवठा - ' + yn_1_2(df.iat[i, 357]) + '\n'
    # Power Suppl y For Agriculture Use 360
    L101 = '<br>शेतीसाठी वीजपुरवठा - ' + yn_1_2(df.iat[i, 360]) + '\n'
    # Power Supply For Commercial Use 363
    L102 = '<br>व्यापारी वापरासाठी वीजपुरवठा - ' + yn_1_2(df.iat[i, 363]) + '\n'
    # Power Supply For All Users 366
    L103 = '<br>सर्व प्रकारच्या वापरासाठी वीजपुरवठा - ' + yn_1_2(df.iat[i, 366]) + '\n'

    L = str1
    wikipage_text += L

    wikipage_text += L100 + L101 + L102 + L103 + '\n'
    # Land Use
    str1 = "== जमिनीचा वापर (हेक्टर) == \n \n"

    # Forest Area (in Hectares) 378
    L104 = "*जंगल क्षेत्र : " + str(df.iat[i, 378])
    # Area under Non-Agricultural Uses (in Hectares) 379
    L105 = "\n* बिगरशेतकी वापरातली जमीन: " + str(df.iat[i, 379])
    # Barren & Un-cultivable Land Area (in Hectares) 380
    L106 = "\n* ओसाड व शेतीला अयोग्य जमीन: " + str(df.iat[i, 380])
    # Permanent Pastures and Other Grazing Land Area (in Hectares)
    L107 = "\n* कुरणे व इतर चराऊ जमीन: " + str(df.iat[i, 381])
    # Land Under Miscellaneous Tree Crops etc. Area (in Hectares)382
    L108 = "\n* फुटकळ झाडीखालची जमीन: " + str(df.iat[i, 382])
    # Culturable Waste Land Area (in Hectares))
    L109 = "\n* शेतीयोग्य पडीक जमीन: " + str(df.iat[i, 383])
    # Fallows Land other than Current Fallows Area (in Hectares)384
    L110 = "\n* कायमस्वरूपी पडीक जमीन: " + str(df.iat[i, 384])
    # Current Fallows Area (in Hectares)
    L111 = "\n* ह्या वर्षीची पडीक जमीन: " + str(df.iat[i, 385])
    # Net Area Sown (in Hectares)386
    L112 = "\n* पिकांखालची जमीन: " + str(df.iat[i, 386])
    # Total Unirrigated Land Area (in Hectares)
    L113 = "\n* एकूण कोरडवाहू शेतजमीन: " + str(df.iat[i, 387])
    # Area Irrigated by Source (in Hectares)388
    L114 = "\n* एकूण बागायती जमीन: " + str(df.iat[i, 388])
    L = str1 + L104 + L105 + L106 + L107 + L108 + L109 + L110 + L111 + L112 + L113 + L114 + "\n"

    wikipage_text += L

    # Irrigation Facility : Area in Hectares
    str1 = "== सिंचन सुविधा (क्षेत्रफळ हेक्टर मध्ये) == \n \n"
    L115 = "* कालवे : " + str(int(df.iat[i, 389]))
    # (in Hectares)390
    L116 = "\n* विहिरी / कूप नलिका: " + str(int(df.iat[i, 390]))
    # (in Hectares)
    L117 = "\n* तलाव / तळी: " + str(int(df.iat[i, 391]))
    # (in Hectares)392
    L118 = "\n* ओढे: " + str(int(df.iat[i, 392]))
    # Area (in Hectares)393
    L119 = "\n* इतर : " + str(int(df.iat[i, 393]))

    L = str1 + L115 + L116 + L117 + L118 + L119 + "\n==संदर्भ==\n" + "{{संदर्भ यादी}}\n [[वर्ग:" + df.iat[
        i, 3] + " जिल्ह्यातील गावे]]\n [[वर्ग:" + df.iat[i, 5] + " तालुक्यातील गावे]]\n"

    wikipage_text += L  # wikipage_text=  wikipage_text +L

    # Convert Arabic numerals to Devanagari directly in memory.
    # The original desktop version used a shared temporary file; the web
    # version avoids that file so multiple users do not overwrite one another.
    wikipage_text = (wikipage_text.replace('0', u'०').replace('1', u'१')
                     .replace('2', u'२').replace('3', u'३').replace('4', u'४')
                     .replace('5', u'५').replace('6', u'६').replace('7', u'७')
                     .replace('8', u'८').replace('9', u'९'))

    return wikipage_text

if __name__ == "__main__":
    import sys
    sys.path
    import codecs
    from decimal import Decimal
    import pickle
    import pandas as pd
    print("A PROJECT TO CREATE TEXT FOR  WIKIPEDIA ARTICLE FOR A VILLAGE IN MAHARASHTRA BASED ON CENSUS 2011 ")
    print('THE CODE IS IN PYTHON 3.11 ')
    print('Developed by : Vijay Edlabadkar e-mail: vijay.janavigyan@gmail.com ')
    print('The project is mentored by Prof. Madhav Gadgil e-mail: madhav.gadgil@gmail.com')
    print(
        'On running the program a text file namely "wikipage_text.txt" is created in  folder "censuswiki". You may open the file in notepad and use it for a wiki article.')

    try:
        df = pd.read_csv('census_data/mah_vill_census_data.csv',
                         low_memory=False)  # read the csv file into a DataFrame df
    except FileNotFoundError:
        print('Data  does not exist')
        sys.exit()
    #
    f2 = open('census_data/temp_E_text.txt', encoding="utf-8", mode='w')

    vill = input("Enter village  as is given in census 2011 data : ")
    print("Village=", vill)
    taluka = input("Enter Taluka  as is given in census 2011 data : ")
    print("Taluka=", taluka)
    district = input("Enter district  as is given in census 2011 data : ")
    print("District=", district)

    i = 0

    try:
        df = df[(df['Village Name'] == vill) & (df['Sub District Name'] == taluka) & (df['District Name']== district)]
        dist_name = df.iat[i, 3]
        dist_code=df.iat[i, 2]
        print('Wait........')
    except IndexError:
        print('No such village exists')
        sys.exit()

    # The following code is continued as it is faster as data frame has only one record and pickle is for one dist only..
    # To replace Roman names in df Devnagari --
    # Opening List object 'e_m_list' from e_m_list.pkl
    # if file is not found village names will not appear in Devnagari
    try:
        with open('census_data/e_m_list_' + str(dist_code) + '.pkl', 'rb') as fd_dist:
            e_m_list = pickle.load(fd_dist)

        for x in e_m_list:
            e_text = x[2]
            e_textU = x[2].upper()
            m_text = x[3]
            df.replace(e_text, m_text, inplace=True)
            df.replace(e_textU, m_text, inplace=True)
    except FileNotFoundError:
        print(
            'Village names in Devnagari script for this district not available : Some names will not appear in Devnagari :')
        input('Enter to continue....')
    # Replacement of Roman by Devnagari ends

    tot_rows = len(df.index)  # For total rows in the df or  current csv file

    # To discard village names appearing multiple times and
    # To discard village with no population data
    if df.iat[i, 25] == 0:  # or df.iat[i, 7] in lst_repeated:
        remark = "Village: " + df.iat[i, 7] + "  Code= " + str(
            df.iat[i, 6]) + ": Data on population not given - No page is created\n"
        print(remark)
        sys.exit()
    i = 0
    L = ''

    main()
# f.close()
