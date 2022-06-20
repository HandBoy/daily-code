"""
Questions:
 

    1. Complete the `MiniVenmo.create_user()` method to allow our application to create new users.

    2. Complete the `User.pay()` method to allow users to pay each other. Consider the following: 
        if user A is paying user B, 
            user's A balance should be used if there's enough balance to cover the whole payment, 
        if not, 
            user's A credit card should be charged instead.

    3. Venmo has the Feed functionality, that shows the payments that users have been doing in the app. 
        If Bobby paid Carol $5, and then Carol paid Bobby $15, it should look something like this
            Bobby paid Carol $5.00 for Coffee
            Carol paid Bobby $15.00 for Lunch

        Implement the `User.retrieve_activity()` and `MiniVenmo.render_feed()` methods so the MiniVenmo application can render the feed.

    4. Now users should be able to add friends. 
        Implement the `User.add_friend()` method to allow users to add friends.

    5. Now modify the methods involved in rendering the feed to also show when user's added each other as friends.
"""

"""
    Questions:
        Why this scenario run() should complete using the card? I think carol has enough balance to cover the whole payment.
            bobby = venmo.create_user("Bobby", 5.00, "4111111111111111")
            carol = venmo.create_user("Carol", 10.00, "4242424242424242")
            bobby.pay(carol, 5.00, "Coffee")

            # should complete using card
            carol.pay(bobby, 15.00, "Lunch")


"""

"""
MiniVenmo! Imagine that your phone and wallet are trying to have a beautiful
baby. In order to make this happen, you must write a social payment app.
Implement a program that will feature users, credit cards, and payment feeds.
"""

import re
import unittest
import uuid
import abc


VALID_CREDIT_CARDS = ["4111111111111111", "4242424242424242"]


class UsernameException(Exception):
    pass


class PaymentException(Exception):
    pass


class CreditCardException(Exception):
    pass


class FriendshipException(Exception):
    pass


class Feed(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def to_feed(self, input):
        raise NotImplementedError()


class PaymentFeed(Feed):
    def __init__(self, amount, actor, target, note):
        self.amount = float(amount)
        self.actor = actor
        self.target = target
        self.note = note

    def to_feed(self):
        return (
            f"{self.actor.username} paid {self.target.username} "
            f"${self.amount} for {self.note}"
        )


class FriendshipFeed(Feed):
    def __init__(self, actor, new_friend):
        self.actor = actor
        self.new_friend = new_friend

    def to_feed(self):
        return f"{self.actor.username} add {self.new_friend.username} as friend"


class Payment:
    def __init__(self, amount, actor, target, note):
        self.id = str(uuid.uuid4())
        self.amount = float(amount)
        self.actor = actor
        self.target = target
        self.note = note


class User:
    def __init__(self, username):
        self.credit_card_number = None
        self.balance = 0.0
        self.feed = []
        self.friends = []

        if self._is_valid_username(username):
            self.username = username
        else:
            raise UsernameException("Username not valid.")

    def retrieve_feed(self):
        return self.feed

    def add_friend(self, new_friend):
        if self.username == new_friend.username:
            raise FriendshipException("User cannot add themselves.")
        elif self._is_friend(new_friend.username):
            raise FriendshipException("User is already a friend.")

        self.friends.append(new_friend)
        self.feed.append(FriendshipFeed(self, new_friend))

    def add_to_balance(self, amount):
        self.balance += float(amount)

    def add_credit_card(self, credit_card_number):
        if self.credit_card_number is not None:
            raise CreditCardException("Only one credit card per user!")

        if self._is_valid_credit_card(credit_card_number):
            self.credit_card_number = credit_card_number

        else:
            raise CreditCardException("Invalid credit card number.")

    def pay(self, target, amount, note):
        payment = self._pay_with_balance(target, amount, note)

        if not payment:
            payment = self._pay_with_card(target, amount, note)

        self.feed.append(PaymentFeed(amount, self, target, note))

    def _is_friend(self, friend):
        for f in self.friends:
            if f.username == friend:
                return True
        return False

    def _pay_with_card(self, target, amount, note):
        amount = float(amount)

        if self.username == target.username:
            raise PaymentException("User cannot pay themselves.")

        elif amount <= 0.0:
            raise PaymentException("Amount must be a non-negative number.")

        elif self.credit_card_number is None:
            raise PaymentException("Must have a credit card to make a payment.")

        self._charge_credit_card(self.credit_card_number)
        payment = Payment(amount, self, target, note)
        target.add_to_balance(amount)

        return payment

    def _pay_with_balance(self, target, amount, note):
        amount = float(amount)

        if amount <= 0.0:
            raise PaymentException("Amount must be a non-negative number.")

        if amount > self.balance:
            return None

        self.balance -= amount
        payment = Payment(amount, self, target, note)
        target.add_to_balance(amount)

        return payment

    def _is_valid_credit_card(self, credit_card_number):
        return credit_card_number in VALID_CREDIT_CARDS

    def _is_valid_username(self, username):
        return re.match("^[A-Za-z0-9_\\-]{4,15}$", username)

    def _charge_credit_card(self, credit_card_number):
        # magic method that charges a credit card thru the card processor
        pass


class MiniVenmo:
    def __init__(self):
        self.users = []

    def create_user(self, username, balance, credit_card_number):
        user = User(username)
        user.add_to_balance(balance)
        user.add_credit_card(credit_card_number)
        self.users.append(user)

        return user

    def render_feed(self, feed):
        for f in feed:
            print(f.to_feed())

    @classmethod
    def run(cls):
        venmo = cls()

        bobby = venmo.create_user("Bobby", 5.00, "4111111111111111")
        carol = venmo.create_user("Carol", 10.00, "4242424242424242")

        try:
            # should complete using balance
            bobby.pay(carol, 5.00, "Coffee")

            # should complete using card
            carol.pay(bobby, 15.00, "Lunch")
        except PaymentException as e:
            print(e)

        feed = bobby.retrieve_feed()
        bobby.add_friend(carol)
        venmo.render_feed(feed)

        feed = carol.retrieve_feed()
        venmo.render_feed(feed)


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user_a = User("abc123")
        self.user_a.add_to_balance(10)
        self.user_a.add_credit_card(VALID_CREDIT_CARDS[0])

        self.user_b = User("bac123")
        self.user_b.add_to_balance(10)
        self.user_b.add_credit_card(VALID_CREDIT_CARDS[0])

    def test_this_works(self):
        with self.assertRaises(UsernameException):
            raise UsernameException()

    # Creating User
    def test_create_user_invalid_username(self):
        user = User("user123")
        self.assertIsInstance(user, User)

    def test_error_create_user_invalid_username(self):
        with self.assertRaises(UsernameException):
            User("ag")

    # Paying with Balance
    def test_pay_user_with_balance(self):
        balance_a = self.user_a.balance
        balance_b = self.user_b.balance
        amount = 5

        self.user_a._pay_with_balance(self.user_b, amount, "Beer")

        self.assertEqual(self.user_a.balance, balance_a - amount)
        self.assertEqual(self.user_b.balance, balance_b + amount)

    def test_error_pay_user_with_amount_greater_than_balance(self):
        amount = 20

        payment = self.user_a._pay_with_balance(self.user_b, amount, "Beer")
        self.assertIsNone(payment)

    def test_error_pay_user_with_negative_amount(self):
        amount = -20

        with self.assertRaises(PaymentException):
            self.user_a._pay_with_balance(self.user_b, amount, "Beer")

    # Pay
    def test_user_do_pay_using_the_balance(self):
        balance_a = self.user_a.balance
        balance_b = self.user_b.balance
        amount = 5

        self.user_a.pay(self.user_b, amount, "Beer")

        self.assertEqual(self.user_a.balance, balance_a - amount)
        self.assertEqual(self.user_b.balance, balance_b + amount)

    def test_pay_using_the_credit_card(self):
        balance_a = self.user_a.balance
        balance_b = self.user_b.balance
        amount = 20

        self.user_a.pay(self.user_b, amount, "Beer")

        self.assertEqual(self.user_a.balance, balance_a)
        self.assertEqual(self.user_b.balance, balance_b + amount)

    def test_error_pay_yourself(self):
        amount = 20

        with self.assertRaises(PaymentException):
            self.user_a.pay(self.user_a, amount, "Beer")

    def test_error_pay_with_negative_amount(self):
        amount = -20

        with self.assertRaises(PaymentException):
            self.user_a.pay(self.user_b, amount, "Beer")

    def test_error_pay_without_credit_card(self):
        amount = 20
        user = User("WithoutCard")

        with self.assertRaises(PaymentException):
            user.pay(self.user_b, amount, "Beer")

    # Friend
    def test_user_add_a_friend(self):
        self.user_a.add_friend(self.user_b)
        self.assertEqual(len(self.user_a.friends), 1)

    def test_error_user_add_yourself_as_friend(self):
        with self.assertRaises(FriendshipException):
            self.user_a.add_friend(self.user_a)

    def test_error_user_add_a_friend_already_added(self):
        self.user_a.add_friend(self.user_b)
        with self.assertRaises(FriendshipException):
            self.user_a.add_friend(self.user_b)

    # Feed
    def test_user_without_activity(self):
        self.assertEqual(len(self.user_a.retrieve_feed()), 0)

    def test_user_with_one_activity(self):
        amount = 20

        self.user_a.pay(self.user_b, amount, "Beer")

        self.assertEqual(len(self.user_a.retrieve_feed()), 1)

    def test_user_with_two_activity(self):
        amount = 8

        self.user_a.pay(self.user_b, amount, "Beer")  # balance
        self.user_a.pay(self.user_b, amount, "Beer")  # credit

        self.assertEqual(len(self.user_a.retrieve_feed()), 2)

    def test_user_check_first_activity(self):
        amount = 20.0
        note = "Beer"

        self.user_a.pay(self.user_b, amount, "Beer")

        feed = self.user_a.retrieve_feed()

        self.assertEqual(
            feed[0].to_feed(),
            (
                f"{self.user_a.username} paid {self.user_b.username} "
                f"${amount} for {note}"
            ),
        )

    def test_user_add_a_friend_feed(self):
        self.user_a.add_friend(self.user_b)
        self.assertEqual(len(self.user_a.feed), 1)

    def test_user_add_a_friend_and_do_pay_feed(self):
        amount = 20.0
        note = "Beer"

        self.user_a.add_friend(self.user_b)
        self.user_a.pay(self.user_b, amount, note)
        self.assertEqual(len(self.user_a.feed), 2)


class TestMiniVenmo(unittest.TestCase):
    def setUp(self):
        self.number = 5
        self.venmo = MiniVenmo()

    # Create User
    def test_create_user(self):
        self.venmo.create_user("username", 10, VALID_CREDIT_CARDS[0])
        self.assertEqual(len(self.venmo.users), 1)

    def test_error_create_user_invalid_username(self):
        with self.assertRaises(UsernameException):
            self.venmo.create_user("a", 10, VALID_CREDIT_CARDS[0])

    def test_error_create_user_add_invalid_credit_card(self):
        with self.assertRaises(CreditCardException):
            self.venmo.create_user("abc123", 10, "4111111111111112")


if __name__ == "__main__":
    unittest.main()
