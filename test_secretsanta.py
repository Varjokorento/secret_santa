from secretsanta import make_and_get_pairs
import unittest
import copy

class TestSecretSanta(unittest.TestCase):
    def test_returned_pairs_dont_have_duplicates_in_giver(self):
        pairs = make_and_get_pairs()
        name_set = set()
        name_list = []
        for pair in pairs:
            name_set.add(pair[0])
            name_list.append(pair[0])
        self.assertEqual(len(name_set), len(name_list))

    def test_returned_pairs_dont_have_duplicates_in_recipient(self):
        pairs = make_and_get_pairs()
        name_set = set()
        name_list = []
        for pair in pairs:
            name_set.add(pair[1])
            name_list.append(pair[1])
        self.assertEqual(len(name_set), len(name_list))
    
    def test_giver_is_not_recipient(self):
        pairs = make_and_get_pairs()
        for pair in pairs:
            self.assertNotEqual(pair[0], pair[1])


    def test_giver_has_unique_recipient(self):
        pairs = make_and_get_pairs()
        for pair in pairs:
            copy_pairs = copy.copy(pairs)
            chec_ctr = 0
            recipient = pair[1]
            for check_pair in copy_pairs:
                if check_pair[1] == recipient:
                    chec_ctr = chec_ctr + 1
            self.assertEqual(chec_ctr, 1)




unittest.main()