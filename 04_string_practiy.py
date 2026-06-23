# QUESTION 1: Stripping Whitespace and Upper-Casing
# Prompt: Clean up a messy user input string to remove all extra spaces on the 
# sides and ensure the final output is completely capitalized.
a1="cHhatTisgaRh";
print(a1.upper());




# QUESTION 2: F-String Formatting and Punctuation Spacing
# Prompt: Format an f-string message combining names with proper title casing. 
# Ensure correct English punctuation (no blank space before the comma).
f_name='taJESh';
l_name='niSHAD';
message=f'Hello, {f_name.title()} {l_name.title()} its good to see you again !';
print(message);





# QUESTION 3: Standardizing Usernames
# Prompt: Combine two separate name variables into a single, cohesive username 
# format separated by an underscore, keeping everything strictly lowercase.
f_name='tajesh'
l_name='nishad'
message=f'{f_name}_{l_name}';                              #OR  message=f'{f_name.lower()}_{l_name.lower()};
print(message);      





# QUESTION 4: The Title-Case Behavior (The Edge Case)
# Prompt: Predict the behavior of the .title() method when handling strings 
# containing alphanumeric combinations (like numbers followed directly by letters).
# Note: Python treats numbers as word boundaries, capitalizing the letter 's' in '21st'.
text="learning python is fun, 21st century skills!"
print(text.title())





#In-Place F-String Normalization (Immutability Solution)
# Prompt: Sanitize a mixed-case email string into standard, account-ready 
# lowercase format using inline expression evaluation inside an f-string.
msg=f'{f_name.lower()}.{l_name.lower()}@github.com';
print(msg);