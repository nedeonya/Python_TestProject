from abc import ABC, abstractmethod


class TicketState(ABC):

    @abstractmethod
    def assign(self, ticket):
        pass

    @abstractmethod
    def resolve(self, ticket):
        pass

    @abstractmethod
    def close(self, ticket):
        pass


class NewState(TicketState):
    def assign(self, ticket):
        ticket.state = AssignedState()
        print("Ticket is assigned")

    def resolve(self, ticket):
        print("Cannot resolve a new ticket, assign it first")

    def close(self, ticket):
        ticket.state = ClosedState()
        print("Ticket is closed")


class AssignedState(TicketState):
    def assign(self, ticket):
        print("Ticket is already assigned")

    def resolve(self, ticket):
        ticket.state = ResolvedState()
        print("Ticket is resolved")

    def close(self, ticket):
        ticket.state = ClosedState()
        print("Ticket is closed")


class ResolvedState(TicketState):
    def assign(self, ticket):
        print("Cannot assign a resolved ticket")

    def resolve(self, ticket):
        print("Ticket is already resolved")

    def close(self, ticket):
        ticket.state = ClosedState()
        print("Ticket is closed")


class ClosedState(TicketState):
    def assign(self, ticket):
        print("Cannot assign a closed ticket")

    def resolve(self, ticket):
        print("Cannot resolve a closed ticket")

    def close(self, ticket):
        print("Ticket is already closed")


class Ticket:
    def __init__(self):
        self.state = NewState()

    def assign(self):
        self.state.assign(self)

    def resolve(self):
        self.state.resolve(self)

    def close(self):
        self.state.close(self)


#Testing
if __name__ == "__main__":
    ticket = Ticket()

    print("Test the initial state and transitions...")
    ticket.assign()
    ticket.resolve()
    ticket.close()

    print("Test invalid transitions...")
    ticket.assign()
    ticket.resolve()
