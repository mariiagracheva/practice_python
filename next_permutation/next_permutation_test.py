import unittest
import next_permutation

class NextPermutationTests(unittest.TestCase):
	"""docstring for ClassName"""
	def test_length_greater_than_1(self):
		self.assertEqual(next_permutation.next_perm('5'), '5')

	def test_empty(self):
		self.assertEqual(next_permutation.next_perm(''), '')

	def test_simple(self):
		self.assertEqual(next_permutation.next_perm('231'), '312')

	def test_the_greatest_perm(self):
		self.assertEqual(next_permutation.next_perm('abc'), 'abc')

		
	def test_the_greatest_perm(self):
		self.assertEqual(next_permutation.next_perm('0125330'), '0130235')

if __name__ == '__main__':
	unittest.main()