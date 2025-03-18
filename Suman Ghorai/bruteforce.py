def longestCommonPrefix_bruteforce(strs):
    if not strs:
        return ""

    prefix = strs[0]  # Start with the first string
    for s in strs[1:]:  # Compare with all other strings
        while not s.startswith(prefix):  # Reduce prefix if no match
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix

# Example usage
strs = ["flower", "flow", "flight"] # Output: "fl"
print(longestCommonPrefix_bruteforce(strs))

# Start with "flower"  
# Compare with "flow" → "flower" doesn’t match, remove 'r' → "flowe"  
# Still doesn’t match, remove 'e' → "flow" ✅ (Matches "flow")  

# Compare with "flight" → "flow" doesn’t match, remove 'w' → "flo"  
# Still doesn’t match, remove 'o' → "fl" ✅ (Matches "flight")  

# Final Answer = "fl"
