with open('code.txt') as f:
    contents = f.read()
    dct = {"@": contents}
    contents = list(filter(None, contents.split(" ")))
    contents.append("")
PROGRAM = False
Numbr = 0
WHEEEN = False
WHEEN = False
WHEN = False
IS = False
REALLYIS = False
VAR = ""
VAR2 = ""
VAR3 = ""
READY = False
SET = False
GO = False
PRINT = False
INPUT = False
RANDOM = False
JOIN = False
while True:
 for element in contents:
   if WHEN:
     if IS:
      dct[VAR] = (
      contents[Numbr].replace("\\s", " ").replace("\\n", "\n").replace("\\b", "\\")
      )
      if VAR == "@":
         IS, WHEN = False, False
         PROGRAM = True
         break
      IS, WHEN = False, False
      VAR = ""
     else:
       VAR = element
       IS = True
   elif WHEEN:
     if IS:
       dct[VAR] = dct[element]
       if VAR == "@":
         WHEEN, VAR, IS = False, "", False
         PROGRAM = True
         break
       WHEEN, VAR, IS = False, "", False
     else:
       VAR = element
       IS = True
   elif WHEEEN:
     if GO:
       dct[VAR] = dct[VAR2].replace(dct[VAR3], dct[element])
       if VAR == "@":
         WHEEEN, VAR, VAR2, VAR3, READY, SET, GO = False, "", "", "", False, False, False
         PROGRAM = True
         break
       WHEEEN, VAR, VAR2, VAR3, READY, SET, GO = False, "", "", "", False, False, False
     elif SET:
       VAR3 = element
       GO = True
     elif READY:
       VAR2 = element
       SET = True
     else:
       VAR = element
       READY = True  
   elif PRINT:
     print(
       dct[element],
       end = ""
      )
     PRINT = False
   elif JOIN:
     if SET:
       dct[VAR] = dct[VAR2] + dct[element]
       if VAR == "@":
         JOIN, VAR, VAR2, READY, SET = False, "", "", False, False
         PROGRAM = True
         break
       JOIN, VAR, VAR2, READY, SET = False, "", "", False, False
     elif READY:
       VAR2 = element
       SET = True
     else:
       VAR = element
       READY = True 
   elif INPUT:
     INPUT = False
     dct[element] = input("")
     if element == "@":
       PROGRAM = True
       break
   elif IS:
     dct[element] = ""
     IS = False
     if element == "@":
       PROGRAM = True
       break
   elif READY:
     dct[element] = chr(int(dct[element]))
     READY = False
     if element == "@":
       PROGRAM = True
       break
   elif GO:
     dct[element] = dct[element][0]
     GO = False
     if element == "@":
       PROGRAM = True
       break
   elif VAR:
     VAR = False
     dct[element] = dct[element][::-1]
     if element == "@":
       PROGRAM = True
       break
   elif SET:
     if element == "}":
       SET = False
   elif element == ">":
     WHEN = True
   elif element == "=":  
     WHEEN = True
   elif element == "$":   
     WHEEEN = True
   elif element == "*":
     PRINT = True
   elif element == "&":
     INPUT = True
   elif element == "+":
     JOIN = True
   elif element == "?":
     IS = True
   elif element == ".":
     READY = True
   elif element == "{":
     SET = True
   elif element == "-":
     GO = True
   elif element == ":":
     VAR = True
   Numbr += 1
 if PROGRAM:
   VAR = ""
   Numbr = 0
   PROGRAM = False
   contents = dct["@"].split(" ")
   contents = list(filter(None, contents))
   contents.append("")
   continue
 break
try:print(dct["#"], end="")
except:pass