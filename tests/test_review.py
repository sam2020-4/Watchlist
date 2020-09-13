import unittest
from app.models import Review

# Review = reviews.Review

class ReviewTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_review = Review(1234,'Python Must Be Crazy','A thrilling new Python Series','/khsjha27hbs',8.5,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_review,Review))

    def test_save_review(self):
        self.new_review.save_review ()
        self.assertTrue(len(Review.all_reviews), 1)

    def test_clear_review(self):
        self.new_review.save_review ()
        test_review=Review(1234,'Python Must Be Crazy','A thrilling new Python Series','/khsjha27hbs',8.5,129993)
 
        test_review.save_review()

        self.new_review.clear_review ()
        self.assertTrue(len(Review.all_reviews), 1)

    def test_get_reviews(self):
        self.new_review.save_review()
        test_review=Review(1234,'Python Must Be Crazy','A thrilling new Python Series','/khsjha27hbs',8.5,129993)
 
        test_review.save_review()

        found_review = Review.get_reviews("1234")

        self.assertEqual(found_review.title, test_review.title)