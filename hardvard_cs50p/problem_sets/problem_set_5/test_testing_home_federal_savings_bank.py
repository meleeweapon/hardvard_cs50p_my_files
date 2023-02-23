from testing_home_federal_savings_bank import *

def test_bank_greeting_procedure():
  assert bank_greeting_procedure("hello david") == 0
  assert bank_greeting_procedure("hi david") == 20
  assert bank_greeting_procedure("how can i help you david") == 20
  assert bank_greeting_procedure("greetings david") == 100
  assert bank_greeting_procedure("awooga") == 100

  assert bank_greeting_procedure("hel lo") == 20
  assert bank_greeting_procedure("25") == 100
  assert bank_greeting_procedure("h i david") == 20
  assert bank_greeting_procedure("h") == 20

  assert bank_greeting_procedure("HELLO DAVID") == 0
  assert bank_greeting_procedure("Hello david") == 0
  assert bank_greeting_procedure("heLLO david") == 0
  assert bank_greeting_procedure("hELLO david") == 0
  assert bank_greeting_procedure("HeLlO david") == 0
  assert bank_greeting_procedure("HeLlO david") == 0

  assert bank_greeting_procedure("\nhello") == 100