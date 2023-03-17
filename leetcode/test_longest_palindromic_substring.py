import longest_palindromic_substring as s

def test_is_polindromic():
  is_pol = s.Solution().is_palindromic

  assert is_pol("ababa") == True
  assert is_pol("badab") == True
  assert is_pol("baab") == True
  assert is_pol("a") == True

  assert is_pol("adsf") == False

def test_longestPalindrome():
  long_pal = s.Solution().longestPalindrome

  assert long_pal("babad") == "bab"
  assert long_pal("cbbd") == "bb"
  assert long_pal("bb") == "bb"
