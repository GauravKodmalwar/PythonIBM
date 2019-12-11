class MobileCard():
    _Provider = "Airtel"

    def setProvider(self, varProv):
        self._Provider = varProv

    def __str__(self):
        return "This is the Mobile Card Object"

    def __init__(self, varIMSI, varPlan, varState):
        self.IMSI = varIMSI
        self.Plan = varPlan
        self.State = varState

    def getCardDetails(self):
        return self.IMSI, self._Provider, self.State, self.Plan

    def billingTime(self):
        return None


class PostPaid(MobileCard):

    def __init__(self, varLimit, varIMSI, varPlan, varState):
        self.callingLimit = varLimit
        super().__init__(varIMSI, varPlan, varState)

    def billingTime(self, totalTime, totalDays=1):
        return  (totalTime - self.callingLimit)/totalDays * 0.05

objCard = MobileCard(9158736434, "PostPaid-Enjoy", "KN")
objCard.setProvider("Jio")
print(objCard.getCardDetails())
print(objCard.billingTime())
print(objCard.__str__())

print("********* Inheritance *********")
objPostPaid = PostPaid(500, 9128759235, "Friends", "AP")
print(objPostPaid.getCardDetails())
print(objPostPaid.billingTime(700))
print(objPostPaid.billingTime(7000, 20))
print(objPostPaid.__str__())

objPostPaid.__


