# arithain
Arithmetic training tool


Should work like (for user):
[ ] 1. Run with config file arg
[ ] 2. Interactive shell starts
[ ] 3. Random task is output (E.g. "2+2")
[ ] 4. User types the answer, presses Enter
[ ] 5. It correct, it is somehow reported in green; Go to 3
[ ] 6. If not correct, correct answer is printed in red; Go to 3
[ ] 7. If user presses Ctrl+C or types "exit", shell quits (dlc: stats report)

Config should allow to specify for each operation (+, -, *, /):
- [ ] First number digits size
- [ ] Second number digits size
- [ ] Ignore operation

Other requirements:
- [ ] /: numA/numB should be a whole number
- [ ] all: exclude `10**n` numbers
- [ ] /, -: in numA_op_numB; numA > numB
- [ ] tests
