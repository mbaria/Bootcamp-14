class TestSequenceFunctions(unittest.TestCase):

    def test_shuffle(self):
       
        seq = list(range(10))
        random.shuffle(seq)
        self.seq.sort()
        self.assertEqual(seq, range(10))

if __name__ == '__main__':
    unittest.main()