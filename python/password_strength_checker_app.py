


import string
print("🔒 PASSWORD STRENGTH CHECKER ")

# Step 1: Input password
pwd = input("Enter your password: ")

# Step 2: Initialize flags
has_upper = False
has_lower = False
has_digit = False
has_symbol = False
min_length = 8

# Step 3: Check each character
for ch in pwd:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    elif ch in string.punctuation:
        has_symbol = True

# Step 4: Check length rule
length_ok = len(pwd) >= min_length

# Step 5: Calculate score
score = 0
if has_upper:
    score += 1
if has_lower:
    score += 1
if has_digit:
    score += 1
if has_symbol:
    score += 1
if length_ok:
    score += 1

# Step 6: Display feedback
print("\n🔍 Checking password strength...\n")

if score == 5:
    strength = "Very Strong "
elif score == 4:
    strength = "Strong "
elif score == 3:
    strength = "Medium "
else:
    strength = "Weak "

print(f"Password Strength: {strength}\n")

# Step 7: Print missing requirements
if not has_upper:
    print("• Add at least one uppercase letter (A-Z)")
if not has_lower:
    print("• Add at least one lowercase letter (a-z)")
if not has_digit:
    print("• Add at least one number (0-9)")
if not has_symbol:
    print("• Add at least one symbol (e.g. @, #, $, %)")
if not length_ok:
    print(f"• Password should be at least {min_length} characters long")

print("\n✅ Check complete!")
