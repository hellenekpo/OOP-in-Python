import copy

#singlylinkedlist class and methods
class SinglyLinkedList:
    def __init__(self, data = 0, after = None):
        self.data = data
        self.after = after
    def __str__(self):
        if self.after:
            copy = self
            stringRep = ""
            while(copy.after):
                stringRep += "[" + str(copy.data) + "] --> "
                copy = copy.after
            stringRep += "[" + str(copy.data) + "]"
            return stringRep
        return "[" + str(self.data) + "]"

def listFindTail(headNode):
    if headNode == None:
        return None
    while(headNode.after):
        headNode = headNode.after
    return headNode

def listInsertTail(headNode, data):
    if (headNode == None):
        return SinglyLinkedList(data)
    else:
        lastNode = listFindTail(headNode)
        lastNode.after = SinglyLinkedList(data)

def listInsertHead(headNode, data):
    newHead = SinglyLinkedList(data, headNode)
    return newHead

def findPrevNode(headNode, target):
    if (headNode == None):
        return None
    elif headNode.after == target:
        return headNode
    while (headNode.after != target and headNode):
        headNode = headNode.after
    return headNode
#polynomial class


class Polynomial:
    def __init__(self, polyInts = []):
        if (type(polyInts) is list):
            self.degrees = -1
            self.coefficients = SinglyLinkedList()
            self.initial(polyInts)
        
        else:
            self.degrees = polyInts.degrees
            self.coefficients = SinglyLinkedList()
            self.copy_constructor(polyInts)

    def initial(self, polyInts):
        if len(polyInts) != 0:
            for index in range(0, len(polyInts)):
                if index == 0:
                    self.coefficients.data = polyInts[0]
                else:
                    self.coefficients = listInsertHead(self.coefficients, polyInts[index])
                self.degrees += 1
            self.cleanup()
        else:
            self.degrees += 1

    def copy_constructor(self, other):
        rightcoeff = other.coefficients
        self.coefficients.data = other.coefficients.data
        rightcoeff = rightcoeff.after
        while (rightcoeff):
            listInsertTail(self.coefficients, rightcoeff.data)
            rightcoeff = rightcoeff.after
        
    def cleanup(self):
        while (listFindTail(self.coefficients).data == 0):
            prevLast = findPrevNode(self.coefficients, listFindTail(self.coefficients))
            prevLast.after = None
            self.degrees -= 1
    def __iadd__(self, other):
        count = 0
        initialDeg = self.degrees
        leftcoeff = self.coefficients
        rightcoeff = other.coefficients
        if (other.degrees <= self.degrees):
            while (rightcoeff):
                leftcoeff.data += rightcoeff.data
                leftcoeff = leftcoeff.after
                rightcoeff = rightcoeff.after
            self.cleanup()
            return self
        self.degrees = other.degrees
        while (rightcoeff):
            if (count == self.degrees):
                break
            if (rightcoeff.after and leftcoeff.after == None):
                listInsertTail(self.coefficients, rightcoeff.after.data)
                if (leftcoeff and count == initialDeg):
                    leftcoeff.data += rightcoeff.data
                count += 1
            else:
                leftcoeff.data += rightcoeff.data
                count += 1
            rightcoeff = rightcoeff.after
            leftcoeff = leftcoeff.after
        return self

    def __eq__(self, other):
        if (self.degrees != other.degrees):
            return False
        leftcoeff = self.coefficients
        rightcoeff = other.coefficients
        while (leftcoeff):
            if leftcoeff.data != rightcoeff.data:
                return False
            leftcoeff = leftcoeff.after
            rightcoeff = rightcoeff.after
        return True
    def __ne__(self, other):
        return not (self == other)
    def __add__(self, other):
        temp = Polynomial(self)
        temp += other
        return temp
    
    def evaluate(self, num):
        finalNum = 0
        currDegree = 0
        coeff = self.coefficients
        while (coeff):
            if currDegree == 0:
                finalNum += coeff.data
            else:
                result = coeff.data * (num ** currDegree)
                finalNum += result
            currDegree += 1
            coeff = coeff.after
        return finalNum
    def __str__(self):
        if self.degrees == 0:
            return str(self.coefficients.data)
        leftcoeff = self.coefficients
        last = listFindTail(leftcoeff)
        prevlast = findPrevNode(leftcoeff, last)
        degrees = self.degrees
        final = ""
        while (degrees != -1):
            if (last != listFindTail(self.coefficients)):
                if last.data > 0:
                    final += " + "
                    if last.data > 1:
                        final += str(last.data)
                elif last.data < 0:
                    final += " - "
                    if last.data < -1:
                        final += str(last.data)
            elif last.data > 0:
                if last.data != 1:
                    final += str(last.data)
            elif last.data < 0:
                final += "-"
                if last.data != -1:
                    final += str(last.data)
            if last.data != 0:
                final += "x"
            if degrees > 1 and last.data != 0:
                final += "^" + str(degrees)
            last = prevlast
            if leftcoeff == last:
                if leftcoeff.data < 0:
                    final += " - " + str(leftcoeff.data)
                elif leftcoeff.data > 0:
                    final += " + " + str(leftcoeff.data)
                break
            prevlast = findPrevNode(leftcoeff, last)
            degrees -= 1
        return final
                
        
    
def main():
    p1 = Polynomial([17])
    p2 = Polynomial([1, 2])
    p3 = Polynomial([-1, 5])
    p4 = Polynomial([5, 4, 3, 2, 1])
    has_a_zero = Polynomial([4, 0, 1, 7])

    print("p1: " + str(p1))
    print("p2: " + str(p2))
    print("p3: " + str(p3))
    print("p4: " + str(p4))
    print("has_a_zero: " + str(has_a_zero))
    print("p2 + p3: " + str(p2 + p3))
    print("p2 + p4: " + str(p2 + p4))
    print("p4 + p2: " + str(p4 + p2))

    p5 = Polynomial(p4)
    p5 += p3
    print("Polynomial p5(p4)")
    print("p5 += p3")
    print("p4: " + str(p4))
    print("p5: " + str(p5))

    p6 = Polynomial()
    print("p6: " + str(p6))
    print("p4 == p6 is " + str(p4 == p6))
    p6 = p4
    print("p6: " + str(p6))
    print("p4 == p6 is " + str(p4 == p6))
    x = 5
    print("Evaluating p1 at " + str(x) + " yields: " + str(p1.evaluate(5)))
    print("Evaluating p2 at " + str(x) + " yields: " + str(p2.evaluate(5)))
    p7 = Polynomial([3, 2, 1])
    print("p7: " + str(p7))
    print("Evaluating p7 at " + str(x) + " yields: " + str(p7.evaluate(5)))
    print("p1 == p2 is " + str(p1 == p2))
    print("p1 != p2 is " + str(p1 != p2))

    p8 = Polynomial([1, 1])
    p9 = Polynomial([-1, 1])
    p10 = Polynomial([0, 0, 2])
    print("((p8 + p9) == p10) is " + str((p8 + p9) == p10))
