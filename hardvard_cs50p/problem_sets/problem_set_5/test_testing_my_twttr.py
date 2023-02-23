from testing_my_twttr import *

def test_is_lower_case_vowel():
  assert is_lower_case_vowel("a") == True
  assert is_lower_case_vowel("e") == True
  assert is_lower_case_vowel("i") == True
  assert is_lower_case_vowel("o") == True
  assert is_lower_case_vowel("u") == True

  assert is_lower_case_vowel("A") == False
  assert is_lower_case_vowel("E") == False
  assert is_lower_case_vowel("I") == False
  assert is_lower_case_vowel("O") == False
  assert is_lower_case_vowel("U") == False

  assert is_lower_case_vowel("b") == False
  assert is_lower_case_vowel("d") == False
  assert is_lower_case_vowel("5") == False
  assert is_lower_case_vowel("=") == False
  assert is_lower_case_vowel("0") == False
  assert is_lower_case_vowel("1.5") == False
  assert is_lower_case_vowel("awooga") == False
  assert is_lower_case_vowel("\n") == False
  assert is_lower_case_vowel("🐱") == False
  assert is_lower_case_vowel("") == False

def test_omit_vowels():
  assert omit_vowels("twitter") == "twttr"
  assert omit_vowels("twttr") == "twttr"
  assert omit_vowels("tweeeter") == "twtr"
  assert omit_vowels("tweeeteee") == "twt"
  assert omit_vowels("aeiou") == ""
  assert omit_vowels("jklm") == "jklm"
  assert omit_vowels("1234") == "1234"

  assert omit_vowels("TWITTER") == "TWTTR"
  assert omit_vowels("TWiTTeR") == "TWTTR"
  assert omit_vowels("TWITTeR") == "TWTTR"
  assert omit_vowels("TWiTTER") == "TWTTR"
  assert omit_vowels("twIttEr") == "twttr"

  assert omit_vowels("awooga") == "wg"
  assert omit_vowels("hello world!") == "hll wrld!"
  assert omit_vowels("🐱") == "🐱"
  assert omit_vowels("\n") == "\n"