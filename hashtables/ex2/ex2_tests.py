import unittest

from ex2 import Ticket, reconstruct_trip


class TestEx2(unittest.TestCase):

    def test_short_case(self):
        ticket_1 = Ticket("none", "PDX")
        ticket_2 = Ticket("PDX", "DCA")
        ticket_3 = Ticket("DCA", "none")

        tickets = [ticket_1, ticket_2, ticket_3]

        expected = ["PDX", "DCA", "none"]
        result = reconstruct_trip(tickets, 3)

        self.assertTrue(expected == result)

    def test_long_case(self):
        ticket_1 = Ticket("PIT", "ORD")
        ticket_2 = Ticket("XNA", "SAP")
        ticket_3 = Ticket("SFO", "BHM")
        ticket_4 = Ticket("FLG", "XNA")
        ticket_5 = Ticket("none", "LAX")
        ticket_6 = Ticket("LAX", "SFO")
        ticket_7 = Ticket("SAP", "SLC")
        ticket_8 = Ticket("ORD", "none")
        ticket_9 = Ticket("SLC", "PIT")
        ticket_10 = Ticket("BHM", "FLG")

        tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
                   ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

        expected = ["LAX", "SFO", "BHM", "FLG", "XNA", "SAP",
                    "SLC", "PIT", "ORD", "none"]
        result = reconstruct_trip(tickets, 10)

        self.assertTrue(expected == result)


if __name__ == '__main__':
    unittest.main()
