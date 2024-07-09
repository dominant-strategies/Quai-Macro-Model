- Coming out of quai mined in terms of hash

## Old Code

    def quaiToHash(self, quaiAmount):
        if quaiAmount <= 0:
            return 0
        return self.qiRewardVal/self.quaiRewardVal * quaiAmount * self.kqi
        #return 2**(2**(self.kquai) * quaiAmount)