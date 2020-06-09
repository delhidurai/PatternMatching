
# Python program for KMP Algorithm
def kmp_pattern_match(pattern, act_txt):
    pattern_len = len(pattern)
    text_len = len(act_txt)

    # create lps[] that will hold the longest prefix suffix
    # values for pattern
    long_prefix_suffix = [0]*pattern_len
    j = 0 # index for pat[]

    # Preprocess the pattern (calculate lps[] array)
    get_long_prefixsuffix(pattern, pattern_len, long_prefix_suffix)

    i = 0 # index for txt[]
    while i < text_len:
        if pattern[j] == act_txt[i]:
            i += 1
            j += 1

        if j == pattern_len:
            print("Found pattern at index " + str(i-j))
            j = long_prefix_suffix[j-1]

            # mismatch after j matches
        elif i < text_len and pattern[j] != act_txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = long_prefix_suffix[j-1]
            else:
                i += 1

def get_long_prefixsuffix(pattern, pattern_len, long_prefix_suffix):
    len = 0 # length of the previous longest prefix suffix

    long_prefix_suffix[0] # lps[0] is always 0
    i = 1

    # the loop calculates lps[i] for i = 1 to M-1
    while i < pattern_len:
        if pattern[i]== pattern[len]:
            len += 1
            long_prefix_suffix[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if len != 0:
                len = long_prefix_suffix[len-1]

                # Also, note that we do not increment i here
            else:
                long_prefix_suffix[i] = 0
                i += 1

txt = "ABABDABACDABABCABAB"
pat = "ABAB"
kmp_pattern_match(pat, txt)

