"""
Name: Yaneza, Lloyd Jemuel "Kai" L.
Course and Block: BSIT-2A
"""
#Open-Closed Principle + Single Responsibility Principle
from abc import ABC, abstractmethod

class Jobelii():
    """
    The Jobelii class is the class being extended. This is closed for modification.
    This is responsible only for storing attributes of a Jobelii object.
    """
    def set_item(self, item, price, qty, taxRate):
        self.item = item
        self.price = price
        self.qty = qty
        self.taxRate = taxRate
class MathOperations():
    """
    MathOperations is an independent class intended for solving basic mathematics.
    This extension is responsible only for solving mathematical operations.
    """
    @staticmethod
    def add(addend1, addend2) -> int:
        return addend1 + addend2
    @staticmethod
    def subtract(minuend, subtrahend) -> int:
        return minuend - subtrahend
    @staticmethod
    def multiply(multiplicand, multiplier) -> int:
        return multiplicand * multiplier
    @staticmethod
    def divide(dividend, divisor) -> int:
        return dividend / divisor
class JobeliiTemplate(ABC):
    @abstractmethod
    def printJobelii(self, item):
        pass
class JobeliiItem(JobeliiTemplate):
    """
    JobeliiItem is an extended version of Jobelii and uses the abstract class template, JobeliiTemplate.
    This extension is responsible only for printing Tax Rate.
    """
    def printJobelii(self, item):
        print(f'Item: {item.item}\nPrice: {item.price}\nTax Rate: {item.taxRate}')
class JobeliiTaxRate(JobeliiTemplate):
    """
    JobeliiTaxRate is an extended version of Jobelii and uses the abstract class template, JobeliiTemplate.
    This extension is responsible only for printing Tax Rate.
    """
    def printJobelii(self, item):
        operations = MathOperations()
        print(f'Tax Rate: {operations.multiply(item.price, item.taxRate)}')
class JobeliiOrder(JobeliiTemplate):
    """
    JobeliiOrder is an extended version of Jobelii and uses the abstract class template, JobeliiTemplate.
    This extension is responsible only for printing Jobelii order.
    """
    def printJobelii(self, item):
        operations = MathOperations()
        print(f'Item: {item.item}\nPrice: {item.price}\nQty: {item.qty}\nTotal: {operations.multiply(item.price, item.qty)}')
# Jobelii class is now open for extension with the use of abstract class template, JobeliiTemplate.
# The class itself, Jobelii, is closed for modification.

#Set the attributes of Jobelii object.
order = Jobelii()
order.set_item('Borgir', 35.50, 3, 0.12)

#Print the item.
print("==Main Class==")
itemProcess = JobeliiItem()
itemProcess.printJobelii(order)

#Print the tax rate.
print("==Tax Rate Process==")
taxRateProcess = JobeliiTaxRate()
taxRateProcess.printJobelii(order)

#Print the order.
print("==Order Process==")
orderProcess = JobeliiOrder()
orderProcess.printJobelii(order)