print("To find the length of longest substring that containn no repeating characters")
def longestSubstring(s):
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):

        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])

        max_len = max(max_len, right - left + 1)

    return max_len


s = input("Enter a string: ")
print("Length of longest substring:", longestSubstring(s))