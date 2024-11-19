import unittest
import tests_12_3

RR_and_TT_ST = unittest.TestSuite()
RR_and_TT_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
RR_and_TT_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(RR_and_TT_ST)
