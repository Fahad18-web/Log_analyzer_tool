## Q1 — How to Run

**Requirements:**
must install python
Python 3.8 or above

**Step 1  Install dependencies:**
Apko fresh machine mei code test karne ke liye ye dependency install karni hogi 
pip install -r requirements.txt

**Step 2  Generate test log file:**
ap khud se log file generate kar sakte hai apni marzi se 
python scripts/generate_logs.py

**Step 3  Run the analyzer:**
jab depencency install hojaye aur test log file phr log analyzer run karen
python log_analyzer.py server.log

## Q2 — Stack Choice

**Why Python?**
Becuase its syntax friendly and easy to understand and has rich in library
python seekhna easy hai 
build-in methods ka access like split() , Counter()

**What would have been a worse choice and why?**
Java language bohot zyada setup mangti hai, sirf text parse karne ke liye bahut complex hai aur mujhe personally difficult bhi lagti hai

## Q3 — One Real Edge Case

Edge Case: Incomplete or malformed lines

Mere code mein log_analyzer.py file mein ye check hai:

if len(parts) < 6:
    print(f'Incomplete lines skipped: {line}')
    continue

Kya hota agar yeh na hota?

Jab maine pehli baar yeh check nahi rakha tha toh 
mera code crash ho gaya tha aur mujhe ye error show hua terminal mei:
IndexError: list index out of range

Kyunke parts[4] ya parts[5] exist hi nahi karta 
incomplete lines mein toh Python error de rahi thi.
Yeh check lagane se code gracefully skip karta hai 
aur baaki lines process hoti rehti hain.

## Q4 — AI Usage

Maine Claude AI ka use kiya is assessment mein.

maine Claude se sirf concepts sikhay:
File reading kaise karte hain Python mein
split() se line ke parts kaise nikalte hain
Counter() se counts kaise karte hain
if len(parts) < 6 edge case concept

Phir maine apna code khud likha — apne variable 
names rakhe jaise IP Address, Request Method, 
Status Code, Incomplete lines skipped.

## Q5 — Honest Gap

log_analyzer tool abhi sirf standard format ki lines 
handle karta hai.

jo chez missing hai:
1. Alag timestamp formats handle nahi hote
   jaise 2024/03/15 ya 15-Mar-2024
   
2. JSON format ki lines skip ho jaati hain
   unhe parse nahi karta

3. Response time sirf ms mein handle hota hai
   0.142s ya bare number 142 handle nahi hota

Agar ek aur din milta toh:
Main timestamp ke liye multiple formats add karta
aur JSON lines ko bhi parse karne ki koshish karta.

Aur mei dev weekend fellowship 2026 ke liye bohot excited bhi hun 