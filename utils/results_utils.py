import streamlit as st


def ReadPDFFile(doc, PageNum, searchtext, BreakText):
    Read = False
    found = False
    Extracttext = []
    #
    page = doc.loadPage(PageNum)
    pagetext = page.getText("text")
    #
    text_instances = page.searchFor(searchtext)
    #
    if (text_instances):
        page_display = page.getDisplayList()
        dictionary_elements = page_display.getTextPage().extractDICT()
        for block in dictionary_elements['blocks']:
            for line in block['lines']:
                for span in line['spans']:
                    Line = span['text']
                    if (Line.strip() == searchtext):
                        Read = True
                    if (BreakText != "" and BreakText in Line.strip() and Read == True):
                        Extracttext.append(Line)
                        found = True
                        break
                    if (Read):
                        if (len(Line) > 1):
                            Extracttext.append(Line)
                if (found): break
            if (found): break
    #
    return Extracttext


def PopulateDict(Extracttext, DictText):
    Extractedtext = []
    # DictText = {}
    ShareAmts = []
    Key = ""
    Extractedtext = Extracttext[4:len(Extracttext) - 1]
    for readtext in Extractedtext:
        if (not any(map(str.isdigit, readtext)) and "(" in readtext):
            Key = Key + readtext
        else:
            if (not any(map(str.isdigit, readtext))):
                if (ShareAmts):
                    DictText[Key] = ShareAmts
                    Key = readtext  # String data
                else:
                    Key = readtext
                ShareAmts = []
            else:
                ShareAmts.append(readtext.strip())
    #
    if (ShareAmts):
        DictText[Key] = ShareAmts
    #
    return DictText


def get_brief(DictText):
    for Key in DictText:
        Values = DictText[Key]
        if (len(Values) == 3):
            Val0 = Values[0].replace(",", ".")
            Val1 = Values[1].replace(",", ".")
            Val0 = Val0.replace("%", "")
            Val1 = Val1.replace("%", "")
            Val2 = Values[2]
            Val2 = Val2.replace("(", "")
            Val2 = Val2.replace(")", "")
            Val2 = Val2.replace("]", "")
            Val2 = Val2.replace("[", "")
            Val2 = Val2.replace("pt", "%")
            Val2 = Val2.replace(" %", "%")
            #
            if (float(Val0) > float(Val1)):
                st.markdown('* {} {}{}B, <font color="green">**up**</font> {}% YoY vs {}{}B in 1Q21.'.format(Key, "\$",
                                                                                                             round(
                                                                                                                 float(
                                                                                                                     Val0),
                                                                                                                 2),
                                                                                                             Val2, "\$",
                                                                                                             round(
                                                                                                                 float(
                                                                                                                     Val1),
                                                                                                                 2)),
                            unsafe_allow_html=True)
            else:
                st.markdown('* {} {}{}B, <font color="red">**down**</font> {}% YoY vs {}{}B in 1Q21.'.format(Key, "\$",
                                                                                                             round(
                                                                                                                 float(
                                                                                                                     Val0),
                                                                                                                 2),
                                                                                                             Val2, "\$",
                                                                                                             round(
                                                                                                                 float(
                                                                                                                     Val1),
                                                                                                                 2)),
                            unsafe_allow_html=True)
        if (len(Values) == 2):
            Val0 = Values[0].replace(",", ".")
            Val1 = Values[1].replace(",", ".")
            Val0 = Val0.replace("%", "")
            Val1 = Val1.replace("%", "")
            Val0 = Val0.replace("(", "")
            Val0 = Val0.replace(")", "")
            Val1 = Val1.replace("(", "")
            Val1 = Val1.replace(")", "")
            #
            if (float(Val0) > float(Val1)):
                diffVal = (float(Val0) - float(Val1))
                Res = (100 * diffVal) / (float(Val1))
                st.markdown('* {} {}{}B, <font color="green">**up**</font> {}% YoY vs {}{}B in 1Q21.'.format(Key, "\$",
                                                                                                             round(
                                                                                                                 float(
                                                                                                                     Val0),
                                                                                                                 2),
                                                                                                             round(Res,
                                                                                                                   2),
                                                                                                             "\$",
                                                                                                             round(
                                                                                                                 float(
                                                                                                                     Val1),
                                                                                                                 2)),
                            unsafe_allow_html=True)
            else:
                diffVal = (float(Val1) - float(Val0))
                Res = (100 * diffVal) / (float(Val0))
                st.markdown('* {} {}{}B, <font color="red">**down**</font> {}% YoY vs {}{}B in 1Q21.'.format(Key, "\$",
                                                                                                             round(
                                                                                                                 float(
                                                                                                                     Val0),
                                                                                                                 2),
                                                                                                             round(Res,
                                                                                                                   2),
                                                                                                             "\$",
                                                                                                             round(
                                                                                                                 float(
                                                                                                                     Val1),
                                                                                                                 2)),
                            unsafe_allow_html=True)
        if len(Values) == 1:
            Values = str(Values)
            Values = Values.replace("]", "")
            Values = Values.replace("[", "")
            Values = Values.replace(" %", "%")
            if "Impact" in Key:
                if "(" in Values:
                    Values = Values.replace("(", "")
                    Values = Values.replace(")", "")
                    st.markdown('* {} on revenue growth, <font color="red">**negative**</font> {}.'.format(Key, Values),
                                unsafe_allow_html=True)
                else:
                    st.markdown('* {} on revenue growth, {}.'.format(Key, Values), unsafe_allow_html=True)
            else:
                if "Organic" in Key:
                    st.write('* {}, {}.'.format(Key, Values))
                else:
                    st.write('* {}, {}.'.format(Key, Values))
